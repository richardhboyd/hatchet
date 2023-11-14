class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def flatten(root):
  if not root:
    return None
  
  stack = [root]
  
  prev = None
  
  while stack:
    curr = stack.pop()
    if prev:
      prev.right = curr
      prev.left = None
    if curr.right:
      stack.append(curr.right)
    if curr.left:
      stack.append(curr.left)
    prev = curr

  return root
