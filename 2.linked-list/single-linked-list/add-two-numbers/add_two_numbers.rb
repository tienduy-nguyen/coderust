class ListNode
  def initialize(val, next = nill)
    @val = val
    @next = next
  end
end

def add_two_numbers(l1, l2)
  dummy = cur = new ListNode(0)
  carry = 0
  while (l1 or l2 or carry)
    if l1
      carry += l1.val
      l1 = l1.next
    end
    if l2
      carry += l2.val
      l2 = l2.next
    end
    cur.next = new ListNode(carry%10)
    cur = cur.next
    carry /= 10
  end
  return dummy.next
end
