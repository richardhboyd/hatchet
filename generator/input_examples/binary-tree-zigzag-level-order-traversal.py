from collections import deque

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def zigzagLevelOrder(root: TreeNode):
  result = []
  if not root:
    return result
  
  queue = deque([root])
  leftToRight = True
  
  while queue:
    level = []
    for _ in range(len(queue)):
      node = queue.popleft()
      level.append(node.val)
      
      if node.left:
        queue.append(node.left)
      if node.right:
        queue.append(node.right)
        
    if not leftToRight:
      level.reverse()
      
    result.append(level)
    leftToRight = not leftToRight
    
  return result
