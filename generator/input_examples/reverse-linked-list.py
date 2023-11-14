# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseListIterative(head):
    prev = None
    curr = head
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev

def reverseListRecursive(head):
    if not head or not head.next:
        return head
    
    new_head = reverseListRecursive(head.next)
    head.next.next = head
    head.next = None
    return new_head
