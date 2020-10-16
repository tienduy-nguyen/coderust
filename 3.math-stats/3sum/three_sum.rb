def three_sum(nums)
  res = []
  nums.sort!
  for i in (0..nums.length - 3)
    if (i > 0 and nums[i] == nums[i - 1])
      next
    end
    l = i + 1
    r = nums.length - 1
    while l < r
      s = nums[i] + nums[l] + nums[r]
      if s < 0
        l += 1
      elsif s > 0
        r -= 1
      else
        res.push([nums[i], nums[l], nums[r]])
        while l < r and nums[l] == nums[l + 1]
          l += 1
        end
        while l < r and nums[r] == nums[r - 1]
          r -= 1
        end
        l += 1
        r -= 1
      end
    end
  end
  return res
end

arr = [1, -4, 2, -1, 0, 0, -1, 0, 1, 1, 1, 1, 2, 4, 5, 6]
p(three_sum(arr))
