def hasPathSum(root, targetSum):
    
    if not root:
        return False
        
    if not root.left and not root.right and root.val == targetSum:
        return True
    
    return hasPathSum(root.left, targetSum - root.val) or hasPathSum(root.right, targetSum - root.val)
