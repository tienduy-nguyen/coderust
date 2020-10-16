class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        super().__init__()

    def is_same_tree(self, p: TreeNode, q: TreeNode) -> bool:

        return True