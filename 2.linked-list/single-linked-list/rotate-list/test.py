class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def rotateRight(self, head, k):
        if not head:
            return head
        size, cur = 0, head
        while cur:
            size += 1
            cur = cur.next
        k %= size  # get the real nth, ignore n * loop of size, make sure k <= size
        slow = fast = head
        for _ in range(k):
            fast = fast.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next
        fast.next = head
        node = slow.next  # link with fast
        slow.next = None
        return node

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
    lk1.printNode(lk1.rotateRight(lk1.head, 2))
