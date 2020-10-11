class ListNode:
  def __init__(self, val, next = None):
    self.val = val
    self.next = next

class LinkedList:
  def __init__(self):
    self.head = None

  def removeNthFromEnd(self, head, n):
      fast = slow = head
      for _ in range(n):
        if not fast:
          self.printNode(head)
          return head
        fast = fast.next
      # self.printNode(fast)
      
      while fast.next:
          fast = fast.next
          slow = slow.next
      slow.next = slow.next.next
      return head
  def remove_nth_from_end2(self, head, n):
    def remove(head,n):
      if head is None: return head, 0
      node, count = remove(head.next, n)
      if node is not None: print('node: ', node.val, ' - count: ', count)
      count += 1
      head.next = node
      if count == n: 
        print('Somthing here: ', count, head.val, node.val)
        head = head.next
      return head, count
    return remove(head, n)[0] #Get head

  def count(self,head):
    def count_size(head):
      if head is None: return 0
      count = count_size(head.next) + 1
      return count
    return count_size(head)

  def shift(self, val):
    new_node = ListNode(val)
    new_node.next = self.head
    self.head = new_node

  def printNode(self,head):
    result = []
    if head is None:
      print("List node null")
    while(head):
      result.append(head.val)
      head=head.next
    print(result)

   

if __name__ == '__main__':
  lk = LinkedList()
  lk.shift(5)
  lk.shift(8)
  lk.shift(6)
  lk.shift(4)
  lk.shift(3)
  lk.shift(2)
  lk.shift(1)
  lk.shift(0)

  lk.printNode(lk.head)
  ans = lk.remove_nth_from_end2(lk.head, 2)
  lk.printNode(ans)
  # while ans is not None:
  #   print(ans.val)
  #   ans = ans.next