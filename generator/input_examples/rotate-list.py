# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def rotateRight(head, k):
    if not head:
        return None
    
    # Find length of the list
    length = 1
    tail = head
    while tail.next:
        tail = tail.next
        length += 1
    
    # Calculate actual rotation based on k
    k = k % length
    if k == 0:
        return head
    
    # Rotate the list    
    curr = head
    for _ in range(length - k - 1):
        curr = curr.next
    new_head = curr.next
    curr.next = None
    tail.next = head
    
    return new_head
