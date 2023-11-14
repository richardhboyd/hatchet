# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n = 0
        stack = []
        
        while True:
            while root:
                stack.append(root)
                root = root.left
                
            root = stack.pop()
            n += 1 
            if n == k:
                return root.val
            
            root = root.right
            
# Test case            
root = TreeNode(3) 
root.left = TreeNode(1)
root.right = TreeNode(4)
root.left.right = TreeNode(2)

k = 1
print(Solution().kthSmallest(root, k)) # 1
