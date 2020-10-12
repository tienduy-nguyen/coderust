class ListNode:
  def __init__(self, val, next= None):
    self.val = val
    self.next = next

class Linkedlist:
  def __init__(self, head = None):
    self.head =head
  def swap_with_head(self, head, n):
    headVal = head.val
    current=head
    count = 0
    while(current and current.next):
      count += 1
      if count == n:
        head.val = current.val
        current.val = headVal
      current = current.next
    return head
  def printNode(self, head):
    result = []
    current = head
    while(current and current.next):
      result.append(current.val)
      current = current.next
    print(result)
    
  def shift(self, val):
    new_node = ListNode(val)
    new_node.next = self.head
    self.head = new_node

if __name__ == '__main__':
  print('start')
  lk = Linkedlist()
  lk.shift(5)
  lk.shift(4)
  lk.shift(3)
  lk.shift(2)
  lk.shift(1)

  lk.printNode(lk.head)
  res = lk.swap_with_head(lk.head,3)
  lk.printNode(res)
