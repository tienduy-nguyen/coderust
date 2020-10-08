def find_first_last(arr, key)
  indices = arr.each_index.select{|i| arr[i] == key}
  return [indices[0], indices[-1]]
end

arr1 = [1, 3, 5, 5, 5, 5, 67, 123, 125]
key1 = 5
arr2 = [1, 3, 5, 5, 5, 5, 7, 123, 125]
key2 = 7
p(find_first_last(arr1, key1))
p(find_first_last(arr2, key2))