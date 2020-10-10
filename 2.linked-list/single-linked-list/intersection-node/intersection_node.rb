def intersection_node(headA, headB)
  if headA.nil? || headB.nil?
    return nil
  end
  # 2 pointers for 2 list
  pa = headA
  pb = headB

  while pa != pb
    pa = pa.nil? ? headB : pa.next
    pb = pb.nil? ? headA : pb.next
  end
  return pa
end