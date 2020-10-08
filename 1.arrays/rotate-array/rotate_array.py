# Write a function rotate(ar[], d, n) that rotates arr[] of size n by d elements
def left_rotate(arr, d):
  first, rest = arr[:d], arr[d:-1]
  return rest+first


arr1 = [1,2,3,4,5,6,7]
print(left_rotate(arr1,2))