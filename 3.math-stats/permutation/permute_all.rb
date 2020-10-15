def permute_all(nums)
  res = []
  permute(nums, [], res)
  return res
end

def permute(nums, path, res)
  if nums.nil? || nums.empty?
    res.push(path)
    return res
  end
  for i in 0..(nums.length - 1)
    newNums = nums.dup
    newNums.delete_at(i)
    permute(newNums, path + [nums[i]], res)
  end
end

nums = [1, 2, 3]
p(permute_all(nums))
