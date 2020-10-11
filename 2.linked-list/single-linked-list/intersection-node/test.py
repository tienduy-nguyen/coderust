class ListNode:
  def __init__(self, val, next = None):
    self.val = val
    self.next = next

class LinkedList:
  def __init__(self):
    self.head = None

  def getIntersectionNode(self,headA, headB):
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
    last = A
    while last.next != None:
      last = last.next
    last.next = B      
    LinkedList.printNode(A)

    # Find the start of the loop
    fast = slow = A
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
        print('slow: ',slow.val)
        print('fast: ',fast.val)
        if slow == fast:
            print('We found something here')
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
  lk = LinkedList()
  a = [4,1,8,4,5]
  b = [7,6,1,8,4,5]
  headA = ListNode(a[0])
  headB = ListNode(b[0])
  first = headA
  second = headB
  first.next= ListNode(a[1])
  first.next.next= ListNode(a[2])
  first.next.next.next= ListNode(a[3])
  first.next.next.next.next= ListNode(a[4])


  second.next= ListNode(b[1])
  second.next.next= ListNode(b[2])
  second.next.next.next= ListNode(b[3])
  second.next.next.next.next= ListNode(b[4])
  second.next.next.next.next.next= ListNode(b[5])
  # for i in a[1::]:
  #   print(i)
  #   first.next = ListNode(i)
  # for i in b[1::]:
  #   second.next = ListNode(i)

  LinkedList.printNode(headA)
  LinkedList.printNode(headB)

  res = lk.getIntersectionNode(headA,headB)
  LinkedList.printNode(res)
