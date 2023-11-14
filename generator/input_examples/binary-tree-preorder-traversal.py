from collections import deque

# Binary Tree Node 
class Node:
  def __init__(self, val=None): 
    self.val = val
    self.left = None
    self.right = None

# Iterative Preorder Traversal
def preorderTraversal(root: Node):
  output = []
  if not root:
    return output

  stack = deque([root])
  
  while stack:
    curr = stack.pop()
    output.append(curr.val)
    if curr.right:
      stack.append(curr.right) 
    if curr.left:
      stack.append(curr.left)

  return output

# Example Usage
root = Node(1) 
root.left = Node(2)
root.right = Node(3)

print(preorderTraversal(root)) # [1, 2, 3]
