class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def countNodes(root: TreeNode) -> int:
    if not root:
        return 0
    
    left_height = getHeight(root.left)
    right_height = getHeight(root.right)
    
    if left_height == right_height:
        return (2 ** left_height) - 1 + countNodes(root.right) + 1
    else:
        return (2 ** right_height) - 1 + countNodes(root.left) + 1
        
def getHeight(node):
    if not node: 
        return 0
    return 1 + getHeight(node.left)
