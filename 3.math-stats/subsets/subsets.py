def subsets(nums):
    res = []
    dfs(nums, [], res)
    return res


def dfs(nums, path, res):
    res.append(path)
    for i in range(len(nums)):
        dfs(nums[i + 1 :], path + [nums[i]], res)
    return res


def subsets2(nums):
    res = [[]]
    for num in sorted(nums):
        print(res)
        res += [item + [num] for item in res]
    return res


nums = [1, 2, 3]
print(subsets(nums))
print(subsets2(nums))