class ListNode
  def initialize(val, next = nil, prev = nil)
    @val, @next, @prev = val, next, prev
  end
end
class DoubleLinkedList
  def initialize(head=nil)
    @head=head
  end
end