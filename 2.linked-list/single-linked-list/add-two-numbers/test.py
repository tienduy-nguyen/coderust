class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def add_two_numbers(self, l1, l2):
        dummy = cur = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            if l1:
                print("carry1:", carry)
                carry += l1.val
                l1 = l1.next
            if l2:
                print("carry2:", carry)
                carry += l2.val
                l2 = l2.next
            print("carry total: ", carry)
            cur.next = ListNode(carry % 10)
            cur = cur.next
            carry //= 10
        return dummy.next

    def addTwoNumbers(self, l1, l2):
        addends = l1, l2
        dummy = end = ListNode(0)
        carry = 0
        while addends or carry:
            carry += sum(a.val for a in addends)
            addends = [a.next for a in addends if a.next]
            end.next = end = ListNode(carry % 10)
            carry //= 10
        return dummy.next

    def printNode(self, head):
        result = []
        current = head
        while current:
            result.append(current.val)
            current = current.next
        print(result)

    def unshift(self, val):
        new_node = ListNode(val)
        new_node.next = self.head
        self.head = new_node


if __name__ == "__main__":
    lk1 = LinkedList()
    lk1.unshift(3)
    lk1.unshift(4)
    lk1.unshift(2)

    lk2 = LinkedList()
    lk2.unshift(4)
    lk2.unshift(6)
    lk2.unshift(5)

    lk1.printNode(lk1.head)
    lk1.printNode(lk2.head)
    lk1.printNode(lk1.add_two_numbers(lk1.head, lk2.head))
    lk1.printNode(lk1.addTwoNumbers(lk1.head, lk2.head))
