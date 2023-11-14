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
        
