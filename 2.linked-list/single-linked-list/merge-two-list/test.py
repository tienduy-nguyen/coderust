class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def merge_two_lists(self, a, b):
        count = 0
        if a and b:
            if a.val > b.val:
                print("a >= b", a.val, b.val)
                a, b = b, a
                count += 1
                print("a node joined: ", end=" ")
                self.printNode(a)
            a.next = self.merge_two_lists(a.next, b)
            print("a next:", end=" ")
            self.printNode(a.next)
        print(f"Result of {count} a: ", end="")
        self.printNode(a)
        return a or b

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
    lk1.shift(2)
    lk1.shift(1)

    lk2 = LinkedList()
    lk2.shift(4)
    lk2.shift(3)
    lk2.shift(1)

    lk1.printNode(lk1.head)
    lk1.printNode(lk2.head)

    lk1.printNode(lk1.merge_two_lists(lk1.head, lk2.head))
