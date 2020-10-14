class ListNode {
  constructor(val, next = null) {
    this.val = val;
    this.next = next;
  }
}

const oddEvenList = function (head) {
  let odd = new ListNode(0);
  let dummy1 = odd;
  let even = new ListNode(0);
  let dummy2 = even;
  while (head) {
    odd.next = head;
    even.next = head.next;
    odd = odd.next;
    even = even.next;
    head = even ? head.next.next : null;
  }
  odd.next = dummy2.next;
  return dummy1.next;
};
