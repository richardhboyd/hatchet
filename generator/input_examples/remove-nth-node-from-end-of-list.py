# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0, head)
        left = dummy
        right = head
        
        # Move right pointer n steps ahead
        for i in range(n):
            right = right.next
            
        # Move both pointers until right pointer reaches the end
        while right:
            left = left.next
            right = right.next
            
        # Remove the nth node    
        left.next = left.next.next
        
        return dummy.next
