from collections import defaultdict

class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random

def copyRandomList(head):
    node_map = defaultdict(lambda: Node(0, None, None))
    node_map[None] = None
    
    curr = head
    while curr:
        node_map[curr].val = curr.val
        node_map[curr].next = node_map[curr.next]
        node_map[curr].random = node_map[curr.random]
        curr = curr.next
        
    return node_map[head]
