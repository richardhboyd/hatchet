import re

def evaluate(expression):
    tokens = re.split('(\D)', expression)
    tokens = [tok.strip() for tok in tokens if tok.strip()]
    
    ops = {'+': lambda a,b: a+b, 
           '-': lambda a,b: a-b,
           '*': lambda a,b: a*b,
           '/': lambda a,b: int(a/b)}
    
    res = int(tokens[0])
    for i in range(1, len(tokens), 2):
        op = ops[tokens[i]]
        res = op(res, int(tokens[i+1]))
    return res


print(evaluate("3+2*2")) # 7 
print(evaluate("3/2")) # 1
print(evaluate("3+5/2")) # 5
