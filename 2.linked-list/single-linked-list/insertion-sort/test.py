class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    """
Given 1 -> 3 -> 2 -> 4 - > null

dummy0 -> 1 -> 3 -> 2 -> 4 - > null
               |    |
              ptr toInsert
-- locate ptr = 3 by (ptr.val > ptr.next.val)
-- locate toInsert = ptr.next

dummy0 -> 1 -> 3 -> 2 -> 4 - > null
          |         |
   toInsertPre     toInsert
-- locate preInsert = 1 by preInsert.next.val > toInsert.val
-- insert toInsert between preInsert and preInsert.next

"""

    def insertion_sort(self, head):
        if head is None or head.next is None:
            return head
        dummy_head = ListNode(-1)
        dummy_head.next = head
        lk.printNode(dummy_head)
        node_to_insert = head

        while head and head.next:
            if head.val > head.next.val:
                # Locate node_to_insert
                node_to_insert = head.next

                # Locate node_to_insert_pre
                node_to_insert_pre = dummy_head
                while node_to_insert_pre.next.val < node_to_insert.val:
                    node_to_insert_pre = node_to_insert_pre.next

                head.next = node_to_insert.next

                # Insert node_to_insert between node_to_insert_pre and node_to_insert_pre.next
                node_to_insert.next = node_to_insert_pre.next
                node_to_insert_pre.next = node_to_insert
            else:
                head = head.next
        return dummy_head.next

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
    lk = LinkedList()
    lk.shift(3)
    lk.shift(6)
    lk.shift(1)
    lk.shift(0)
    lk.shift(4)
    lk.shift(2)
    lk.shift(2)

    lk.printNode(lk.head)
    lk.printNode(lk.insertion_sort(lk.head))
