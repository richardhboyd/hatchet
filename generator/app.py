import os
import random
import string
from textwrap import dedent
from ast_comments import parse, unparse
from ast import NodeTransformer, Assign, fix_missing_locations, NodeVisitor, Attribute, Name
from collections.abc import Iterable
import boto3
import math

HOW_MANY_MB = 11
FREQUENCY_OF_ASSIGNS = 0.25 # lower is more frequent
BUCKET_NAME = os.getenv("BUCKET_NAME")

SERVICES = ["gourd", "squash","carrot","pumpkin"]
STAGES = ["Dev", "PreProd", "Prod"]
LEVELS = ["WARN", "INFO", "DEBUG", "ERROR"]
PREAMBLE = dedent(
    '''
    from timber.hatchet import Hatchet
    from timber.level import Level
    from timber.stage import Stage

    # instantiate a hatchet instance
    hatchet = Hatchet(endpoint="https://timber.acme.dev", service_name="{service_name}", stage=Stage.{stage})
    '''
)

INSTANTIATOR = dedent(
    '''
    # instantiate a hatchet instance
    hatchet = Hatchet(endpoint="https://timber.acme.dev", service_name="{service_name}", stage=Stage.{stage})
    '''
)

LOGGER = dedent(
    '''
    # use hatchet to chop logs for {variable_name}
    hatchet.chop("{log_message}", Level.{level})
    '''
)
path = os.getcwd()
full_path = f"{path}/input_examples/"

def convert_size(size_bytes):
   if size_bytes == 0:
       return "0B"
   size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
   i = int(math.floor(math.log(size_bytes, 1024)))
   p = math.pow(1024, i)
   s = round(size_bytes / p, 2)
   return "%s %s" % (s, size_name[i])

def get_file(file_path):
    with open(f"{path}/input_examples/{file_path}", 'r') as f:
        contents = f.read()
    return contents

class RewriteInterpolation(NodeTransformer):
    def generic_visit(self, node):
        if hasattr(node, 'body') and isinstance(node.body, Iterable):
            where_to_insert = []
            for index, child in enumerate(node.body):
                if isinstance(child, Assign) and isinstance(node.body[index].targets[0], (Attribute, Name)):
                    if random.random() > FREQUENCY_OF_ASSIGNS:
                        where_to_insert.append(index)
            if len(where_to_insert) > 0:
                if getattr(node, 'body') is not None:
                    where_to_insert.reverse()
                    for index in where_to_insert:
                        if isinstance(node.body[index].targets[0], Attribute):
                            variable_name = node.body[index].targets[0].attr
                        elif isinstance(node.body[index].targets[0], Name):
                            variable_name = node.body[index].targets[0].id
                        else:
                            continue # we don't try to log [Subscript, Starred, List, or Tuple]
                        comment_node = parse(LOGGER.format(
                            variable_name=variable_name,
                            log_message=f"{variable_name} was reassigned",
                            level=random.choice(LEVELS)
                            )
                        )
                        try:
                            node.body.insert(index+1, comment_node)
                        except Exception as e:
                            print(type(node))
                            print(type(node.body))
                            print(dir(node))
                            for entry in node._fields:
                                print(f"entry: {entry}, {getattr(node, entry)}")
                            raise(e)
        NodeVisitor.generic_visit(self, node)
        return node

def lambda_handler(event, context):
    request_id = context.aws_request_id
    TEST_NAME = f"big-ast-{request_id}"
    s3_client = boto3.client('s3')
    files = [f for f in os.listdir(full_path)]
    contents = [get_file(f) for f in files]
    total_bytes = 0
    file_count = 0
    while total_bytes < (1024*1024 * HOW_MANY_MB):
        comb = random.choices(contents, k=8)
        combined_python_code = ''.join(comb)

        nodes = parse(combined_python_code)
        # This is where we insert our fancy private SDK using the Python AST
        nodes = fix_missing_locations(RewriteInterpolation().visit(nodes))
        preamble_nodes = parse(PREAMBLE.format(stage=random.choice(STAGES),service_name=random.choice(SERVICES))).body
        
        pos = 0
        for i in range(len(preamble_nodes)):
            nodes.body.insert(i + pos, preamble_nodes[i])
        updated_source = unparse(nodes)
        file_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
        full_file_name = f"ast-insert-trial-001/{file_name}.py"

        s3_client.put_object(
            Body=bytes(updated_source, 'utf-8'),
            Bucket=BUCKET_NAME,
            Key=f'tests/{TEST_NAME}/Repo1/{full_file_name}'
        )

        total_bytes += len(updated_source.encode('utf-8'))
        file_count += 1
        if file_count % 100 == 0:
            print(f"file count: {file_count}, total bytes: {convert_size(total_bytes)}")
        if total_bytes > (1e+6 * HOW_MANY_MB):
            print(f"file count: {file_count}, total bytes: {convert_size(total_bytes)}")
            break
    
    return {"location": f"s3://{BUCKET_NAME}/tests/{TEST_NAME}/"}
