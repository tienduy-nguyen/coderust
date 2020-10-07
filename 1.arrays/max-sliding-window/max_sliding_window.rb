def max_sliding_window(arr, k)
  result = []
  if arr.length <= (k-1)
    result.push(arr.max)
    return result
  end
  maxValue = arr[0..(k-1)].max
  for i in k..(arr.length-1)
    if arr[i] > maxValue
      maxValue = arr[i]
    end
    result.push(maxValue)
  end
  return result
end

arr = [1, 2, 3, 1, 4, 5, 2, 3, 6];
k = 3;
p (max_sliding_window(arr, k));