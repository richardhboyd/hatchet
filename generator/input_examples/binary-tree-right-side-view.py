from collections import deque

def rightSideView(root):
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        rightMost = None
        size = len(queue)
        
        for _ in range(size):
            node = queue.popleft()
            rightMost = node
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(rightMost.val)
    
    return result
