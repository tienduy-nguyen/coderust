class ListNode:
    def __init__(self, val, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def copyRandomList(self, head: "Node") -> "Node":
        # Create mirror node for each node in linked list
        cur = head
        while cur:
            # backup original next node of input linkied list
            original_next_hop = cur.next

            # create mirror node with original order
            cur.next = ListNode(cur.val, next=original_next_hop, random=None)

            # move to next position
            cur = original_next_hop
        print("First current:", end="")
        self.printNode(head)
        # Let mirror node get the random pointer
        cur = head
        while cur:
            if cur.random:
                # assign random pointer to mirror node
                cur.next.random = cur.random.next
            try:
                # move to next position
                cur = cur.next.next
            except AttributeError:
                break
        # Separate copy linked list from original linked list
        try:
            # locate the head node of copy linked list
            head_of_copy_list = head.next
            cur = head_of_copy_list

        except AttributeError:
            # original input is an empty linked list
            return None
        self.printNode(head_of_copy_list)
        self.printNode(cur)
        while cur:
            try:
                # link mirror node to copy linked list
                cur.next = cur.next.next
            except AttributeError:
                break

            # move to next position
            cur = cur.next
        return head_of_copy_list

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
    lk1.printNode(lk1.copyRandomList(lk1.head))
