def removeNthFromEnd(self, head, n):
  low = fast  = head
  for _ in range(n):
    if not fast:
      return head.next # Remove head if n > size of head
    fast = fast.next
  while fast and fast.next:
    slow, fast = slow.next, fast.next
  slow.next = slow.next.next
  return slow


# Alternative solutions
def remove_nth_from_end2(self, head, n):
