=begin
Again, pre is the previous node,
but here I create a dummy as previous node of the head. And again, a is the current node and b is the next node. This time I go one node further and call it c.
To go from pre -> a -> b -> c to pre -> b -> a -> c, 
we need to change those three references. Here I chain the assignments, pretty much directly saying "pre points to b, which points to a, which points to c".
=end
def swap_pairs(head)
  pre = dummy = ListNode.new 0
  pre.next = head
  while a = pre.next && b = a.next
    c = b.next
    ((pre.next = b).next=a).next=c
    pre = a
  end
  return dummy.text
end 

def swap_pairs(head)
  pre = dummy = ListNode.new 0
  pre.next = head 
  while pre.next && pre.next.next
    a = pre.next
    b = b.next
    c = b.next
    pre.next,b.next, a.next = b,a,c
    pre = a
  end
  return dummy.next
end