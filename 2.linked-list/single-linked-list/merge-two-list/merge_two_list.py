"""
The expression x and y first evaluates x; if x is false, its value is returned; otherwise, y is evaluated and the resulting value is returned.

The expression x or y first evaluates x; if x is true, its value is returned; otherwise, y is evaluated and the resulting value is returned.
"""

"""
Solution 1
If both lists are non-empty, 
I first make sure a starts smaller, 
use its head as result, and merge the remainders behind it. 
Otherwise, i.e., if one or both are empty, I just return what's there.
"""


def mergeTwoLists(self, a, b):
    if a and b:
        if a.val > b.val:
            a, b = b, a
        a.next = self.mergeTwoLists(a.next, b)
    return a or b


"""
Solution 2

First make sure that a is the "better" 
one (meaning b is None or has larger/equal value). 
Then merge the remainders behind a.
"""


def mergeTwoLists(self, a, b):
    if not a or b and a.val > b.val:
        a, b = b, a
    if a:
        a.next = self.mergeTwoLists(a.next, b)
    return a
