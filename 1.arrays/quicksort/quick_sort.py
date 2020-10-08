def quick_sort(arr):
  if not arr or len(arr) <=1:
    return arr
  mid = int((0 + len(arr)-1)/2)
  pivot = arr[mid]
  left = []
  right = []
  for i in range(0,len(arr)):
    if i == mid:
      continue
    if arr[i] <= pivot:
      left.append(arr[i])
    else:
      right.append(arr[i])
  return quick_sort(left) + [pivot] + quick_sort(right)


arr = [10, 80, 30, 90, 40, 50, 70]
print(quick_sort(arr))
