class ListNode
  def initialize(val, next = nil)
    @val = val
    @next  = next
  end
end

def sortList(head)
  return head if head.nil?
  slow = head
  fast = head.next
  while fast and fast.next
    fast = fast.next.next
    slow = slow.next
  end
  start = slow.next
  slow.next = nil
  l, r = sortList(slow), sortList(start)
  return merge(l,r)
end

def merge(l, r)
  return r if l.nil?
  return l if r.nil?
  dummy = p = new ListNode(0)
  while (l && r)
    if l.val < r.val
      p.next = l
      l = l.next
    else
      p.next = r
      r = r.next
    end
    p = p.next
  end

  p.next = l.nil? ? r : l
  return dummy.next
end