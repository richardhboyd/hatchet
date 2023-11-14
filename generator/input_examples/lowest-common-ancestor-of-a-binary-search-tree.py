class TreeNode:
    def __init__(self, val):
        self.val = val 
        self.left = None
        self.right = None

def lowestCommonAncestor(root, p, q):
    curr = root
    while curr:
        if p.val > curr.val and q.val > curr.val:
            curr = curr.right
        elif p.val < curr.val and q.val < curr.val:
            curr = curr.left
        else:
            return curr

# Example usage:
root = TreeNode(6) 
root.left = TreeNode(2)
root.right = TreeNode(8)
root.left.left = TreeNode(0)
root.left.right = TreeNode(4)
root.left.right.left = TreeNode(3)
root.left.right.right = TreeNode(5)
root.right.left = TreeNode(7)
root.right.right = TreeNode(9)

p = root.left
q = root.right.left

lca = lowestCommonAncestor(root, p, q)
print(lca.val) # Output: 6
