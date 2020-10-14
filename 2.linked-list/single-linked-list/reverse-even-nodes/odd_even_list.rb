class ListNode
  def initialize(val, next = nil)
    @val = val
    @next = next
  end
end

def odd_even_list(head):
  dummy1 = odd = new ListNode(0)
  dummy2 = even = new ListNode(0)
  while head
    odd.next = head
    even.next =  head.next
    odd = odd.next
    even = even.next
    head = head.next.next if even else nil
  end
  odd.next = dummy2.next
  return dummy1.next

