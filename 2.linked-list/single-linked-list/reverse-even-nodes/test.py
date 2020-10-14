class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def oddEvenList(self, head):
        dummy1 = odd = ListNode(0)
        dummy2 = even = ListNode(0)
        while head:
            odd.next = head
            even.next = head.next
            odd = odd.next
            even = even.next
            head = head.next.next if even else None
        odd.next = dummy2.next
        return dummy1.next

    def printNode(self, head):
        result = []
        current = head
        while current:
            result.append(current.val)
            current = current.next
        print(result)

    def shift(self, val):
        new_node = ListNode(val)
        new_node.next = self.head
        self.head = new_node


if __name__ == "__main__":
    lk1 = LinkedList()
    lk1.shift(5)
    lk1.shift(4)
    lk1.shift(3)
    lk1.shift(2)
    lk1.shift(1)
    lk1.shift(0)

    lk1.printNode(lk1.head)
    lk1.printNode(lk1.oddEvenList(lk1.head))
