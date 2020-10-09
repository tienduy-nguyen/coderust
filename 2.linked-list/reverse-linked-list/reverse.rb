# Iterative method
def reverse(head)
  prev = nil
  current = head
  while(current) do
    next = current.next
    current.next = prev
    prev = current
    current = next
  end
  return prev
end

# Recursive method
def reverse(head)
  return _reverse(head)
end
def _reverse(node, prev = nil)
  if node.nil?
    return nil
  end
  next = node.next
  prev = node
  return reverse2(next, node)
end
