def pivot_binary_search(arr, key)
  high = arr.length()
  pivot = find_pivot(arr, 0, high)
  if pivot == -1
    return binary_search(arr, 0, high, key)
  end
  if arr[pivot] == key
    return pivot
  end
  if arr[0] <= key
    return binary_search(arr, 0, pivot-1, key)
  end
  return binary_search(arr, pivot+1, high, key)
end

def find_pivot(arr, low, high)
  if high < low
    return -1
  end
  if high == low
    return low
  end
  mid = ((low + high)/2).round()
  if mid < high && arr[mid] > arr[mid+1]
    return mid
  end
  if mid > low && arr[mid] < arr[mid-1]
    return mid
  end
  if arr[low] >= arr[mid]
    return find_pivot(arr, low, mid-1)
  end
  return find_pivot(arr, mid+1, high)
end

def binary_search(arr, low, high, key)
  if high < low
    return -1
  end
  mid = ((low+high)/2).round()
  if arr[mid]== key
    return mid
  end
  if arr[mid]>key
    return binary_search(arr, low, mid-1, key)
  end
  return binary_search(arr, mid+1, high, key)
end


arr1 = [5, 6, 7, 8, 9, 10, 1, 2, 3]
key1 = 3 # output 8
arr2 = [5, 6, 7, 8, 9, 10, 1, 2, 3]
key2 = 30 # not found
arr3 = [30, 40, 50, 10, 20]
key3 = 10
puts(pivot_binary_search(arr1, key1))
puts(pivot_binary_search(arr2, key2))
puts(pivot_binary_search(arr3, key3))