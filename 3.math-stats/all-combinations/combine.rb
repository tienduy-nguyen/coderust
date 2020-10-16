def combine(n, k)
  res = []
  nums = [*1..n]
  dfs(nums, k, [], res)
  return res
end

def dfs(nums, k, path, res)
  if path.length == k
    res.push(path)
    return res
  end
  for i in 0..(nums.length - 1)
    dfs(nums[i + 1..-1], k, path + [nums[i]], res)
  end
end

p(combine(4, 2))
