def find_pair(arr, sum):
  found = -1
  for i in range(0,len(arr)):
    search = sum - arr[i]
    newArr = arr[:] # Copy the original list
    newArr.remove(arr[i])
    if search in newArr:
      found = [arr[i], search]
      break
  return found

arr1 = [0, -1, 2, -3, 1]
arr2 = [1, -2, 1, 0, 5]
arr3 = [1]
sum1 = -2
sum2 = 0
sum3 = 2
print(find_pair(arr1, sum1))
print(find_pair(arr2, sum2))
print(find_pair(arr3, sum3))