# Binary tree node 
class Node:
  def __init__(self, key):
    self.key = key 
    self.left = None
    self.right = None

def findLCA(root, n1, n2):
  if not root:
    return None

  if root.key == n1 or root.key == n2:
    return root

  left = findLCA(root.left, n1, n2)
  right = findLCA(root.right, n1, n2)

  if left and right:
    return root
  
  return left if left else right

# Test case
root = Node(1) 
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

n1 = 4
n2 = 7
print(findLCA(root, n1, n2).key) # 1
