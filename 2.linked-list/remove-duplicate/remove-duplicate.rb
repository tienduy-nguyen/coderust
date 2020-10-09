def remove_duplicate(head)
  if head.nil?
    return head
  end
  prev = head
  current = head.next
  while current do
    if current.val != prev.val
      prev.next = current
      prev = current
    end
    current = current.next
  end
  prev.next = nil
  return head
end