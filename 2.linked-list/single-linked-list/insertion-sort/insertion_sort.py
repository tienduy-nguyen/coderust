'''
Given 1 -> 3 -> 2 -> 4 - > null

dummy0 -> 1 -> 3 -> 2 -> 4 - > null
               |    |
              ptr toInsert
-- locate ptr = 3 by (ptr.val > ptr.next.val)
-- locate toInsert = ptr.next

dummy0 -> 1 -> 3 -> 2 -> 4 - > null
          |         |
   toInsertPre     toInsert
-- locate preInsert = 1 by preInsert.next.val > toInsert.val
-- insert toInsert between preInsert and preInsert.next

'''
class ListNode:
  def __init__(self, val, next = None):
    self.val = val
    self.next = next

def insertion_sort(self, head):
  if(head is None or head.next is None):
    return head
  dummy_head = ListNode(0)
  dummy_head.next = node_to_insert = head 

  while head and head.next:
    if head.val > head.next.val:
      # Locate node_to_insert
      node_to_insert = head.next

      # Locate node_to_insert_pre
      node_to_insert_pre = dummy_head
      while node_to_insert_pre.next.val < node_to_insert.val:
        node_to_insert_pre = node_to_insert_pre.next

      head.next = node_to_insert.next

      # Insert node_to_insert between node_to_insert_pre and node_to_insert_pre.next
      node_to_insert.next = node_to_insert_pre.next
      node_to_insert_pre.next = node_to_insert
    else:
      head = head.next
  return dummy_head.next
    

