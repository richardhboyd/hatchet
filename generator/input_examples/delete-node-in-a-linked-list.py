def delete_node(node):
  # Since we do not have access to the head node, we cannot simply unlink
  # the given node from the list. Instead, we will copy the value and
  # next pointer from the next node into this node, effectively deleting
  # the next node

  next = node.next
  node.val = next.val
  node.next = next.next

  # Reduce the length of the list by 1
  length[0] -= 1

class ListNode:
  def __init__(self, val):
    self.val = val
    self.next = None

def build_list(vals):
  head = ListNode(vals[0])
  prev = head
  for v in vals[1:]:
    new = ListNode(v)  
    prev.next = new
    prev = new
  return head 

length = [0]
head = build_list([4,5,1,9]) 
length[0] = 4 

node = head.next.next
delete_node(node)

print_list(head) # Should print [4,5,9]
print(length[0]) # Should print 3
