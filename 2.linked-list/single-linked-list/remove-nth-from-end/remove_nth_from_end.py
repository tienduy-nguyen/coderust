def removeNthFromEnd(self, head, n):
  low = fast  = head
  for _ in range(n):
    if not fast:
      return head
    fast = fast.next
  while fast and fast.next:
    slow, fast = slow.next, fast.next
  slow.next = slow.next.next
  return slow