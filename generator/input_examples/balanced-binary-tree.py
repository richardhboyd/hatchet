class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left 
    self.right = right

def isBalanced(root):
  def check(root):
    if not root:
      return 0
    
    leftHeight = check(root.left)
    if leftHeight == -1:
      return -1
    
    rightHeight = check(root.right)  
    if rightHeight == -1:
      return -1

    if abs(leftHeight - rightHeight) > 1:
      return -1
    return 1 + max(leftHeight, rightHeight)

  return check(root) != -1
