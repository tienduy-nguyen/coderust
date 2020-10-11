class ListNode:
  def __init__(self, val, next = None, prev = None):
    self.val = val
    self.next = next
    self.prev = prev

class DoubleLinkedList:
  def __init__(self, head=None):
    self.head = head