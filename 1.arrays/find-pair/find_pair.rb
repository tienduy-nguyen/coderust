def find_pair(arr, sum)
  found = -1
  for i in 0..(arr.length-1)
    search = sum - arr[i]
    newArr = arr.clone
    newArr.delete(arr[i])
    if newArr.include?(search)
      found = [arr[i], search]
      break
    end
  end
  return found
end

arr1 = [0, -1, 2, -3, 1]
arr2 = [1, -2, 1, 0, 5]
arr3 = [1]
sum1 = -2
sum2 = 0
sum3 = 1
p(find_pair(arr1, sum1))
p(find_pair(arr2, sum2))
p(find_pair(arr3, sum3))