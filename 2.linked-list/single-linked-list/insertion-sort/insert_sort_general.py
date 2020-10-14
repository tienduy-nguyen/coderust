def insertion_sort_general(arr):
    if not arr:
        return arr
    size = len(arr)
    for i in range(size):
        for j in range(i + 1, size):
            while i < j:
                if arr[j] < arr[j - 1]:
                    arr[j], arr[j - 1] = arr[j - 1], arr[j]
                j -= 1
    return arr


arr = [1, 5, 3, 8, 2, 6, 7]
print(insertion_sort_general(arr))
# // Name	            Best	Average	Worst	Memory	Stable	Comments
# // Insertion sort	  n	    n2	    n2	  1	      Yes