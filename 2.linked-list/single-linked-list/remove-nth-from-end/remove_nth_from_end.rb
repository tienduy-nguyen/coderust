def remove_nth_from_end(head, n)
  slow = fast = head
  for _ in 0..n-1
    return head if fast.nil?
    fast = fast.next
  end
  while fast && fast.next
    slow = slow.next
    fast = fast.next
  end
  slow.next = slow.next.next
  return head
end