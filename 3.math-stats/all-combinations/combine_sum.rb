def combine_sum(candidates, target)
  res = []
  dfs(candidates, target, [], res)
  return res
end

def dfs(nums, target, path, res)
  if target == 0
    res.push(path)
    return res
  end
  for i in 0..(nums.length - 1)
    if nums[i] > target
      next
    end
    dfs(nums[i..-1], target - nums[i], path + [nums[i]], res)
  end
end

arr = [2, 3, 6, 7]
target = 7
p(combine_sum(arr, 7))
