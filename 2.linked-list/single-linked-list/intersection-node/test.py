class ListNode:
  def __init__(self, val, next = None):
    self.val = val
    self.next = next

class LinkedList:
  def __init__(self):
    self.head = None

  @staticmethod
  def getIntersectionNode(headA, headB):
    if headA is None or headB is None:
        return None

    pa = headA # 2 pointers
    pb = headB
    LinkedList.printNode(pa)
    LinkedList.printNode(pb)

    def equal(a,b):
      if a == None and b == None:
        return True
      if(a != None and b != None and a.val == b.val):
          return True
      return False

    while not equal(pa,pb):
        # if either pointer hits the end, switch head and continue the second traversal, 
        # if not hit the end, just move on to next
        pa = headB if pa is None else pa.next
        pb = headA if pb is None else pb.next
        if pa is not None:
          print("a: ", pa.val)
        else:
          print("a: None")
        if pb is not None:
          print("b: ",pb.val)
        else:
          print("b: None")
    LinkedList.printNode(pa)
    return pa 
  def getIntersectionNode2(self,A, B):
    if not A or not B: return None

    # Concatenate A and B
    LinkedList.printNode(A)
    LinkedList.printNode(B)
    last = ListNode(0)
    last.next = A
    while last.next != None:
      print(last.val)
      last = last.next
    last.next = B      
    LinkedList.printNode(last)

    # Find the start of the loop
    fast = slow = A
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
        if slow == fast:
            fast = A
            while fast != slow:
                slow, fast = slow.next, fast.next
            last.next = None
            return slow

    # No loop found
    last.next = None
    return None

  def shift(self, val):
    new_node = ListNode(val)
    new_node.next = self.head
    self.head = new_node


  @staticmethod
  def printNode(head):
    result = []
    if head is None:
      print("List node null")
    while(head):
      result.append(head.val)
      head=head.next
    print(result)

   

if __name__ == '__main__':
  a = LinkedList()
  a.shift(5)
  a.shift(4)
  a.shift(8)
  a.shift(1)
  a.shift(4)

  b = LinkedList()
  b.shift(5)
  b.shift(4)
  b.shift(8)
  b.shift(1)
  b.shift(6)
  b.shift(5)

  # LinkedList.printNode(a.head)
  # LinkedList.printNode(b.head)
  res = a.getIntersectionNode2(a.head,b.head)
  LinkedList.printNode(res)
