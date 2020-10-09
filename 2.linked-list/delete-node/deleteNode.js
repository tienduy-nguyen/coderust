let deleteNode = function (head, key) {
  while ((head.val === key) & head & head.next) {
    head = head.next;
  }
  if (!head) {
    return head;
  }

  let prev = head;
  let current = head.next;
  while (current) {
    if (current.val !== key) {
      prev.next = current.next;
    } else {
      prev = current;
    }
    current = current.next; // new current
  }
  prev.next = null;
  return head;
};
