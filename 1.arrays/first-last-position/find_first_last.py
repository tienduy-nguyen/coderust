def find_fist_last(arr, key):
  indices = [i for i, x in enumerate(arr) if x == key]
  return [indices[0], indices[-1]]


arr1 = [1, 3, 5, 5, 5, 5, 67, 123, 125]
key1 = 5
arr2 = [1, 3, 5, 5, 5, 5, 7, 123, 125]
key2 = 7
print(find_fist_last(arr1, key1))
print(find_fist_last(arr2, key2))