class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def swapPairs(head):
    dummy = ListNode(0, head)
    prev, curr = dummy, head
    
    while curr and curr.next:
        next_pair = curr.next.next
        second = curr.next
        
        second.next = curr
        curr.next = next_pair
        prev.next = second
        
        prev = curr
        curr = next_pair
        
    return dummy.next
