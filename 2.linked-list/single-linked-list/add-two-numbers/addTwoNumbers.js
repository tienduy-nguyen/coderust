class ListNode {
  constructor(val, next = null) {
    this.val = val;
    this.next = next;
  }
}
const addTwoNumbers = function (l1, l2) {
  let cur = new ListNode(0);
  let dummy = cur;
  let carry = 0;
  while (l1 || l2 || carry) {
    if (l1) {
      carry = l1.val;
      l1 = l1.next;
    }
    if (l2) {
      carry = l2.val;
      l2 = l2.next;
    }
    cur.next = new ListNode(carry % 10);
    cur = cur.next;
    carry /= 10;
  }
  return dummy.next;
};
