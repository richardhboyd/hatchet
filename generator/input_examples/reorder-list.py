# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reorderList(head):
    if not head:
        return 
    
    # Find the middle of the list
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    # Reverse the second half
    second = slow.next
    prev = slow.next = None
    while second:
        tmp = second.next
        second.next = prev
        prev = second
        second = tmp
        
    # Merge the two halves
    first, second = head, prev
    while second:
        tmp1, tmp2 = first.next, second.next 
        first.next = second 
        second.next = tmp1
        first = tmp1
        second = tmp2
