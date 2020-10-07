def binary_search(arr, key)
  lower = 0
  upper = arr.length
  while lower<upper do
    indexMid = (lower + (upper -  lower)/2).round(0)
    mid = arr[indexMid]
    if key == mid
      return indexMid
    elsif mid > key
      upper = indexMid -1
    else
      lower = indexMid + 1
    end
  end
  return -1
end

arr = [3, 5, 12, 56, 92, 123, 156, 190, 201, 222]
key = 12
result = binary_search(arr, key)
puts result


# Complexity
# Worst case time complexity: O(log N)
# Average case time complexity: O(log N)
# Best case time complexity: O(1)
# Space complexity: O(1)