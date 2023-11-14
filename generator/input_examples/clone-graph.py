from collections import deque

class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
        
def cloneGraph(node):
    if not node:
        return
    
    nodeCopy = Node(node.val, [])
    
    queue = deque([node])
    visited = {node: nodeCopy}
    
    while queue:
        curr = queue.popleft()
        
        for neighbor in curr.neighbors:
            if neighbor not in visited:
                neighborCopy = Node(neighbor.val, [])
                visited[neighbor] = neighborCopy
                queue.append(neighbor)
                
            visited[curr].neighbors.append(visited[neighbor])
            
    return visited[node]
