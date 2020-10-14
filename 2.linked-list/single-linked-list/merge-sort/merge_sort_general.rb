def merge_sort(arr)
  if arr.length <= 1
    return arr
  end
  len = arr.length
  mid = ((0 + len - 1) / 2).round()
  left = arr[0..mid]
  right = arr[mid + 1..-1]
  return merge(merge_sort(left), merge_sort(right))
end

def merge(left, right)
  result = []
  while (left.length >= 1 and right.length >= 1)
    if (left[0] < right[0])
      result.push(left.shift)
    else
      result.push(right.shift)
    end
  end
  return result + left + right
end

arr = [1, 5, 6, 9, 4, 3, 11, 26, 85, 1, 0, 574, 799]
p merge_sort(arr)
