class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def reverse_odd(self, head):
    dummy1 = odd = ListNode(0)
    dummy2 = even = ListNode(0)
    while head:
        odd.next = head
        even.next = head.next
        odd = odd.next
        even = even.next
        head = head.next.next if even else None
    prev = None
    current = dummy2.next
    while current:
        next = current.next
        current.next = prev
        prev = current
        current = next
    odd.next = dummy2
    return dummy1.next
