class Solution:
    def __init__(self):
        self

    def combine(self, n, k):
        res = []
        self.dfs(list(range(1, n + 1)), k, [], res)
        return res

    # backtracking, dfs: deep first search
    def dfs(self, nums, k, path, res):
        if len(path) == k:
            res.append(path)
            return
        for i in range(len(nums)):
            self.dfs(nums[i + 1 :], k, path + [nums[i]], res)


sl = Solution()
num = 5
print(sl.combine(num, 2))


# alternative solution leetcode
# backtracking iterative solution
def combine2(self, n, k):
    ans = []
    stack = []
    x = 1
    while True:
        l = len(stack)
        if l == k:
            ans.append(stack[:])
        if l == k or x > n - k + l + 1:
            if not stack:
                return ans
            x = stack.pop() + 1
        else:
            stack.append(x)
            x += 1