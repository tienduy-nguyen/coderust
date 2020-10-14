const rotateRight = function (head, k) {
  if (!head) return head;
  let size = 0;
  let current = head;
  while (current) {
    size++;
    current = current.next;
  }
  for (let i = 0; i < k; ++i) {
    fast = fast.next;
  }
  while (fast && fast.next) {
    fast = fast.next;
    slow = slow.next;
  }
  fast.next = head;
  const node = slow.next;
  slow.next = null;
  return node;
};
