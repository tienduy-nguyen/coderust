def delete_node(head,key)
  while (head && head.next && head.val == key) do
    head = head.next
  end
  if (!head.nil?)
    return head
  end
  prev = head
  current = head.next
  while current do
    if current.val == key
      prev.next = current.next
    else
      prev = current
    end
    current = current.next
  end
  prev.next = null
  return head
end