# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def sortList(head):
    if not head or not head.next:
        return head
    
    # split the list into two halves
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    second = slow.next
    slow.next = None
    
    # sort each half
    left = sortList(head)
    right = sortList(second)
    
    # merge the sorted halves
    return merge(left, right)

def merge(l1, l2):
    dummy = ListNode() 
    tail = dummy
    
    while l1 and l2:
        if l1.val < l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2 
            l2 = l2.next
        tail = tail.next
        
    if l1:
        tail.next = l1
    if l2:
        tail.next = l2
        
    return dummy.next
