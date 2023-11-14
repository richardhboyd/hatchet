def postorderTraversal(root):
    if not root:
        return []
    
    stack = [root]
    output = []
    
    while stack:
        curr = stack.pop()
        output.append(curr.val)
        
        if curr.left:
            stack.append(curr.left)
        if curr.right:
            stack.append(curr.right)
            
    return output[::-1]
