class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxPathSum(root):
    max_sum = float("-inf")
    
    def dfs(node):
        nonlocal max_sum
        if not node: 
            return 0
        
        left = max(dfs(node.left), 0)
        right = max(dfs(node.right), 0)
        
        max_sum = max(max_sum, node.val + left + right)
        
        return node.val + max(left, right)
    
    dfs(root)
    return max_sum

root = TreeNode(1) 
root.left = TreeNode(2)
root.right = TreeNode(3)

print(maxPathSum(root)) # 6

root = TreeNode(-10)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(maxPathSum(root)) # 42
