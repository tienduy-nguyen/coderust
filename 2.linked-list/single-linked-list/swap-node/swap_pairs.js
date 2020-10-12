const swap_pairs = function (head) {
  let pre = new ListNode(0);
  let dummy = pre;
  pre.next = head;
  while (pre.next && pre.next.next) {
    let a = pre.next;
    let b = a.next;
    let c = (b.next[(pre.next, b.next, a.next)] = [b, a, c]);
    pre = a;
  }
  return dummy.next;
};
