# leetcode: https://leetcode.com/problems/combination-sum/
class Solution:
    def __init__(self):
        super().__init__()

    def combine_sum(self, candidates, target):
        res = []
        self.dfs(candidates, target, [], res)
        return res

    def dfs(self, nums, target, path, res):
        if target == 0:
            res.append(path)
            return
        for i in range(len(nums)):
            if nums[i] > target:
                continue
            self.dfs(nums[i:], target - nums[i], path + [nums[i]], res)


sl = Solution()
arr = [2, 3, 6, 7]
target = 7
print(sl.combine_sum(arr, 7))
