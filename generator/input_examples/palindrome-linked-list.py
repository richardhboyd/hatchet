# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def isPalindrome(head: ListNode) -> bool:
    slow, fast = head, head
    stack = []
    
    while fast and fast.next:
        stack.append(slow.val)
        slow = slow.next
        fast = fast.next.next
        
    if fast:
        slow = slow.next
    
    while slow:
        top = stack.pop()
        
        if top != slow.val:
            return False
        
        slow = slow.next
        
    return True
