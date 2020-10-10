let insertionSort = function (head) {
  if (!head || !head.next) return head;
  let sorted = head;
  head = head.next;
  sorted.next = null;
  while (head) {
    let prev = null;
    let node = sorted;
    while (node && head.val > node.val) {
      prev = node;
      node = node.next;
    }
    let insert = head;
    head = head.next;
    insert.next = node;
  }
};
