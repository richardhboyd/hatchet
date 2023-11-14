# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def insertionSortList(head):
    dummy = ListNode(0)
    curr = head
    
    while curr:
        prev = dummy
        
        # Find correct position to insert
        while prev.next and prev.next.val < curr.val:
            prev = prev.next
            
        # Insert node
        next = curr.next
        curr.next = prev.next
        prev.next = curr
        
        # Move to next node
        curr = next
        
    return dummy.next
