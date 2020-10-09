def remove_duplicate(self, head):
  prev = head
  current = head.next
  while current:
    if current.val != prev.val:
      prev.next = current
      prev = current
    current = current.next
  
  prev.next = None
  return head
