class ListNode:
  def __init__(self, val):
    self.val = val
    self.next = None
class LinkedList:
  def __init__(self, head=None):
    self.head = head

def insertion_sort(self, head):
  dummy_head = ListNode(0)
  dummy_head =  node_to_insert = head

  while head and head.next:
    if head.val >= head.next.val:
      # Locate node_to_insert
      node_to_insert = head.next

      # Locate node_to_insert_pre
      node_to_insert_pre = dummy_head
      while node_to_insert_pre.next.val < node_to_insert.val:
        node_to_insert_pre = node_to_insert_pre.next

      head.next = node_to_insert.next

      # Insert node_to_insert between node_to_insert_pre and node_to_insert_pre.next
      node_to_insert.next = node_to_insert_pre.next
      node_to_insert_pre.next = node_to_insert.next
    else:
      head = head.next
  return dummy_head.next
    

