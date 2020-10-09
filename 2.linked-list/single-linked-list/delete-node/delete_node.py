def delete_node(self, head, key):
  while head and head.next and head.val == key:
    head = head.next
  if head is None:
    return head
  prev = head
  current = head.next
  while current:
    if current.val == key:
      prev.next = current.next
    else:
      prev = current
    current = current.next
  prev.next = None
  return head