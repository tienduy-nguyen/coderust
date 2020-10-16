def subsets(nums)
  res = []
  dfs(nums, [], res)
  return res
end

def dfs(nums, path, res)
  res.push(path)
  for i in 0..(nums.length - 1)
    dfs(nums[i + 1..-1], path + [nums[i]], res)
  end
  return res
end

nums = [1, 2, 3]
p(subsets(nums))
