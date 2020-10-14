def rorate_right(head, k)
  return head if head.nil?
  size, current = 0, head
  while (current)
    size += 1
    current = current.next
  end
  k %= size
  slow = fast = head
  for _ in 0..(k - 1)
    fast = fast.next
  end
  while (fast and fast.next)
    slow = slow.next
    fast = fast.next
  end
  fast.next = head
  node = slow.next # link with fast
  slow.next = nil # Remove after slow
  return node
end
