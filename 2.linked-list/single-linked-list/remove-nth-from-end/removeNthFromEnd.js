let removeNthFromEnd = function (head, n) {
  let slow = head;
  let fast = head;
  for (let i = 0; i < n; ++i) {
    if (!fast) return head;
    fast = fast.next;
  }
  while (fast && fast.next) {
    slow = slow.next;
    fast = fast.next;
  }
  slow.next = slow.next.next;
  return head;
};
