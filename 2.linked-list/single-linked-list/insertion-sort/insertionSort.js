class ListNode {
  constructor(val, next = null) {
    this.val = val;
    this.next = next;
  }
}
class LinkedList {
  constructor(head = null) {
    this.head = head;
  }
}
let insertionSort = function (head) {
  if (!head || !head.next) return head;
  // const dummyHead = { next: head };
  const dummyHead = new ListNode();
  dummyHead.next = head;
  let nodeToInsert = head;
  const nodeToInsertPre = dummyHead;
  while (head && head.next) {
    if (head.val > head.next.val) {
      // Locate nodeToInsert
      nodeToInsert = head.next;

      // Locate nodeToInsertPre
      nodeToInsertPre = dummyHead;
      while (nodeToInsertPre.next.val < nodeToInsert.val) {
        nodeToInsertPre = nodeToInsertPre.next;
      }
      head.next = nodeToInsert.next;

      // Insert nodeToInsert between nodeToInsertPre and nodeToInsertPre.next
      nodeToInsert.next = nodeToInsertPre.next;
      nodeToInsertPre.next = nodeToInsert;
    } else {
      head = head.next;
    }
  }
  return dummyHead.next;
};
