import collections

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def serialize(root):
    if not root:
        return '#'
    return '{} {} {}'.format(root.val, serialize(root.left), serialize(root.right))

def deserialize(data):
    vals = collections.deque(data.split())
    def rebuild():
        if vals:
            val = vals.popleft()
            if val == '#':
                return None
            node = TreeNode(int(val))
            node.left = rebuild()
            node.right = rebuild()
            return node
    return rebuild()

