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

  oddEvenList(head) {
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
  }

  printNode(head) {
    const result = [];
    while (head) {
      result.push(head.val);
      head = head.next;
    }
    console.log(result);
  }
  unshift(val) {
    const newNode = new ListNode(val);
    newNode.next = this.head;
    this.head = newNode;
  }
}

const lk = new LinkedList();
lk.unshift(5);
lk.unshift(4);
lk.unshift(3);
lk.unshift(2);
lk.unshift(1);
lk.unshift(0);
lk.printNode(lk.head);
lk.printNode(lk.oddEvenList(lk.head));
