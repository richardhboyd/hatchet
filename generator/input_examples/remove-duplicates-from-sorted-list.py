head = ListNode(1)
head.next = ListNode(1) 
head.next.next = ListNode(2)

new_head = deleteDuplicates(head)

# new_head will be [1, 2]
