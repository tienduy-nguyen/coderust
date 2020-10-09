// Iterative method
let reverse = function (head) {
  let prev = null;
  let current = head;
  let next = null;
  while (current) {
    next = current.next;
    current.next = prev;
    prev = current;
    current = next;
  }
  return prev;
};

// Recursive method
let reverse2 = function (head) {
  return _reverse(head);
};

let _reverse = function (node, prev = null) {
  if (!head) {
    return null;
  }
  const next = node.next;
  node.next = prev;
  return _reverse(next, node);
};
