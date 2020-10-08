def quick_sort(arr)
  if arr.empty? || arr.length <= 1
    return arr
  end
  mid = ((0+arr.length-1)/1).round()
  pivot = arr[mid]
  left = []
  right = []
  for i in 0..(arr.length-1)
    if i == mid
      next
    end
    if(arr[i] <= pivot)
      left.push(arr[i])
    else
      right.push(arr[i])
    end
  end
  return quick_sort(left) + [pivot] + quick_sort(right)
end


arr = [10, 80, 30, 90, 40, 50, 70]
p(quick_sort(arr))
