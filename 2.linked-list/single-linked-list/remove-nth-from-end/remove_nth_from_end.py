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


# Alternative solutions: Recursive solution
def remove_nth_from_end2(self, head, n):
  def remove(head,n):
    if head is None: return head, 0
    node, count = remove(head.next, n)
    count += 1
    head.next = node
    if count == n: head = head.next # Replace node at nth by the next node
    return head, count
  return remove(head, n)[0]

