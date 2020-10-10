class ListNode
  def initialize(val, next=nil)
    @val = val
    @next = next
  end
end
class LinkedList
  def initialize(head = nil)
    @head = head
  end
  def insertion_sort(head)
    if head.nil? || head.next.nil?
      return head
    end
    dummy_head = ListNode.new(0)
    dummy_head = head.next
    node_to_insert = head.next
    while (head && head.next)
      if head.val > head.next.val
        node_to_insert = head.next
        node_to_insert_pre = dummy_head
        while(node_to_insert_pre.next.val < node_to_insert.val)
          node_to_insert_pre = node_to_insert_pre.next
        end
        head.next = node_to_insert.next

        # Insert node_to_insert between node_to_insert_pre and node_to_insert_pre.next
        node_to_insert.next = node_to_insert_pre.next
        node_to_insert_pre.next = node_to_insert
        
      else
        head = head.next
      end

    end
  end
end
