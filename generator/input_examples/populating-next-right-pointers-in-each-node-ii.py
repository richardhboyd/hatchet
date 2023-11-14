class Node:
    def __init__(self, val, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right 
        self.next = next

def connect(root):
    if not root:
        return
    
    leftmost = root
    
    while leftmost.left:
        head = leftmost
        while head:
            head.left.next = head.right 
            if head.next:
                head.right.next = head.next.left
            head = head.next
        leftmost = leftmost.left

root = Node(1, Node(2, Node(4), Node(5)), Node(3, Node(6), Node(7)))
connect(root)

# Test next pointers  
print(root.left.next.val) # 3
print(root.right.next) # None
