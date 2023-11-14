# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseBetween(head, left, right):
    if not head or left == right:
        return head
    
    prev, curr = None, head
    for i in range(left - 1):
        prev = curr
        curr = curr.next
    
    tail = curr
    for i in range(right - left):
        third = curr.next
        curr.next = prev
        prev = curr 
        curr = third
    
    if left > 1:
        head.next = prev
    else:
        head = prev
        
    tail.next = curr
    return head
