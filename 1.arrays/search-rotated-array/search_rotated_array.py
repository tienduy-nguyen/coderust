# Searches an element key in a pivoted 
# sorted array arrp[] of size n  
def pivot_binary_search(arr, key):
  high = len(arr)-1
  pivot = find_pivot(arr, 0, high)
  if pivot == -1:
    return binary_search(arr,0, high, key)
  if arr[pivot] == key:
    return pivot
  if arr[0] <= key:
    return binary_search(arr, 0, pivot-1, key)
  return binary_search(arr, pivot+1, high, key)


# Function to get pivot. For array  
# 3, 4, 5, 6, 1, 2 it returns 3  
# (index of 6)
def find_pivot(arr, low, high):
  if high < low:
    return -1
  if low == high:
    return low
  mid = int((low+high)/2)
  if mid < high and arr[mid] > arr[mid+1]:
    return mid
  if mid > low and arr[mid] < arr[mid-1]:
    return mid
  if arr[low] >= arr[mid]:
    return find_pivot(arr, low, mid-1)
  return find_pivot(arr, mid+1, high)


def binary_search(arr, low,high, key):
  if high < low:
    return -1
  midIndex = int((low+high)/2)
  midValue = arr[midIndex]
  if midValue == key:
    return midIndex
  if midValue > key:
    return binary_search(arr, low, midIndex-1, key)
  return binary_search(arr, midIndex+1, high, key)


arr1 = [5, 6, 7, 8, 9, 10, 1, 2, 3]
key1 = 3 # output 8
arr2 = [5, 6, 7, 8, 9, 10, 1, 2, 3]
key2 = 30 # not found
arr3 = [30, 40, 50, 10, 20]
key3 = 10
print(pivot_binary_search(arr1, key1))
print(pivot_binary_search(arr2, key2))
print(pivot_binary_search(arr3, key3))