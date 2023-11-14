# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Definition for a binary tree node.  
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sortedListToBST(head: ListNode) -> TreeNode:
    
    # Get the mid point and make it the root
    if not head:
        return None
    
    if not head.next:
        return TreeNode(head.val)
    
    # Find midpoint using slow and fast pointer technique
    slow, fast = head, head.next.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
    # Slow is now pointing to midpoint        
    mid = slow
    # Set mid.next as None, so now we have two separate LLs 
    mid.next = None
    
    # Recursively form BST on left and right halves
    root = TreeNode(mid.val)
    root.left = sortedListToBST(head)
    root.right = sortedListToBST(mid.next)
    
    return root
