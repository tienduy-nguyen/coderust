def max_sliding_window(arr, k):
  result = []
  if len(arr) <= (k-1):
    result.append(max(arr))
    return result
  maxValue = max(arr[0:k])
  for i in range(k,len(arr)-1):
    current = arr[i]
    print(current)
    if current >= maxValue:
      maxValue = current
    result.append(maxValue)
  return result

arr = [1, 2,5,7,6,8,32,1,2]
k = 3
print(max_sliding_window(arr, k))
