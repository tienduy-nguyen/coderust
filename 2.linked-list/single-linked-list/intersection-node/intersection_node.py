'''
If two linked lists have intersection, we can find two observations:

They must have same nodes after the intersection point.
L1+L2 must have same tail from the intersection point as L2 + L1. For example,
L1 = 1,2,3
L2 = 6,5,2,3

L1+L2 = 1,2,3,6,5,2,3
L2+L1 = 6,5,2,3,1,2,3
The loop same at 2, 3
'''
def intersect_node(self, headA, headB):
  if headA is None or headB is None:
    return None
  pa = headA # 2 pointers
  pb = headB

  while pa is not pb:
    # if either pointer hits the end, switch head and continue the second traversal, 
    # if not hit the end, just move on to next
    pa = pa.next if pa else headB
    pb = pb.next if pb else headA
  
  return pa
  # only 2 ways to get out of the loop, they meet or the both hit the end=None



# the idea is if you switch head, the possible difference between length would be countered. 
# On the second traversal, they either hit or miss. 
# if they meet, pa or pb would be the node we are looking for, 
# if they didn't meet, they will hit the end at the same iteration, pa == pb == None, return either one of them is the same,None