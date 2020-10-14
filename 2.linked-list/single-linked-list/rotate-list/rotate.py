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