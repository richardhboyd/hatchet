class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(lists):
    dummy = ListNode() 
    curr = dummy
    
    heap = []
    # Put the root of each linked list in the min heap
    for linked_list in lists:
        if linked_list:
            heapq.heappush(heap, (linked_list.val, linked_list))
    
    # Take the smallest node from the heap, 
    # add it to result and put the next node of that list back in heap
    while heap:
        smallest = heapq.heappop(heap)[1]
        curr.next = smallest
        curr = curr.next
        if smallest.next:
            heapq.heappush(heap, (smallest.next.val, smallest.next))
    
    return dummy.next
