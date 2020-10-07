def binary_search(arr, key):
  lower = 0
  upper = len(arr)-1
  indexMid = 0
  mid = arr[indexMid]
  while lower < upper:
    indexMid = round(lower + (upper - lower)/2)
    mid = arr[indexMid]
    if mid == key:
      return indexMid
    elif mid < key:
      lower = indexMid + 1  
    else:
      upper = indexMid
  return -1

arr = [3, 5, 12, 56, 92, 123, 156, 190, 201, 222]
key = 12
result = binary_search(arr, key)
print(result)


# Complexity
# Worst case time complexity: O(log N)
# Average case time complexity: O(log N)
# Best case time complexity: O(1)
# Space complexity: O(1)