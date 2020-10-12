def swap_with_head(self, head, n):
  headVal = head.val
  current=head
  count = 0
  while(current and current.next):
    count += 1
    if count == n:
      head.val = current.val
      current.val = headVal
    current = current.next
  return head
