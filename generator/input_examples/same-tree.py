p = TreeNode(1, TreeNode(2), TreeNode(3)) 
q = TreeNode(1, TreeNode(2), TreeNode(3))
print(isSameTree(p, q)) # True

p = TreeNode(1, TreeNode(2))
q = TreeNode(1, None, TreeNode(2)) 
print(isSameTree(p, q)) # False
