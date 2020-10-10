let intersectionNode = function (headA, headB) {
  if (!headA || !headB) {
    return null;
  }
  let pa = headA;
  let pb = headB; // 2 pointers
  while (pa !== pb) {
    pa = pa ? pa.next : headB;
    pb = pb ? pb.next : headA;
  }
  return pa;
};
