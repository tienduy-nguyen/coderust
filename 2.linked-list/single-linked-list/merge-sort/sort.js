class ListNode {
  constructor(val, next = null) {
    this.val = val;
    this.next = next;
  }
}

const sortList = function (head) {
  if (!head) return head;
  let slow = head;
  let fast = head.next;
  while (fast && fast.next) {
    fast = fast.next.next;
    slow = slow.next;
  }
  let start = slow.next;
  slow.next = null;
  let left = sortList(slow);
  let right = sortList(start);
  return merge(left, right);
};

const merge = function (l, r) {
  if (!l) return r;
  if (!r) return l;

  let p = new ListNode(0);
  let dummy = p;
  while (l && r) {
    if (l.val < r.val) {
      p.next = l;
      l = l.next;
    } else {
      p.next = r;
      r = r.next;
    }
    p = p.next;
  }
  p.next = l === null ? r : l;
  return dummy.next;
};
