// For sorted linkedlist
let removeDuplicate1 = function (head) {
  if (!head) {
    return head;
  }
  let prev = head;
  let current = head.next;
  while (current) {
    if (current.val !== prev.val) {
      prev.next = current;
      prev = current;
    }
    current = current.next;
  }
  prev.next = null;
  return head;
};
