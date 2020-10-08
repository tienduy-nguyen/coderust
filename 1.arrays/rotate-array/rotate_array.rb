def left_rotate(arr,d)
  first, rest = arr[0..d-1], arr[d..-1]
  return rest + first
end

arr1 = [1,2,3,4,5,6,7]
p(left_rotate(arr1,2))