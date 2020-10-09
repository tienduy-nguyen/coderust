# Iterative method

def reverse(self, head):
  prev = None
  current = head
  while current:
    next = current.next
    current.next = prev
    prev = current
    current = next
  return prev
  
# Recursive method
def reverse2(self, head):
  return self._reverse(head)

def _reverse(self, node, prev=None):
  if not node:
    return None
  next = node.next
  node.next = prev
  return self._reverse(next,node)
