def pathSum(root, targetSum):
    result = []
    
    def dfs(node, currPath, currSum):
        if not node:
            return
        
        currPath.append(node.val)
        currSum += node.val
        
        if not node.left and not node.right and currSum == targetSum:
            result.append(currPath[:])
        
        dfs(node.left, currPath, currSum)
        dfs(node.right, currPath, currSum)
        
        currPath.pop()
        
    dfs(root, [], 0)
    return result
