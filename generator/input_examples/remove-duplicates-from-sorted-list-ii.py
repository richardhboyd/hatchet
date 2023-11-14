# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteDuplicates(head):
    curr = head
    while curr and curr.next:
        if curr.val == curr.next.val:
            curr.next = curr.next.next
        else:
            curr = curr.next
            
    return head

# Test case
head = ListNode(1)
head.next = ListNode(2) 
head.next.next = ListNode(3)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(4)
head.next.next.next.next.next = ListNode(4)
head.next.next.next.next.next.next = ListNode(5)

new_head = deleteDuplicates(head)
while new_head:
    print(new_head.val) 
    new_head = new_head.next

# Prints:
# 1
# 2 
# 5
