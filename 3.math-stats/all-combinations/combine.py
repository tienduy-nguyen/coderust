# leetcode: https://leetcode.com/problems/combinations/
def combine(n, k):
    res = []
    dfs(list(range(1, n + 1)), k, [], res)
    return res


def dfs(nums, k, path, res):
    if len(path) == k:
        res.append(path)
        return res
    for i in range(len(nums)):
        dfs(nums[i + 1 :], k, path + [nums[i]], res)


n = 4
k = 2
print(combine(n, k))
