def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    size = len(arr)
    mid = int((0 + size - 1) / 2)
    left = arr[0 : mid + 1]
    right = arr[mid + 1 :]
    print("left: ", left)
    print("left: ", right)
    return merge(mergeSort(left), mergeSort(right))


def merge(left, right):
    result = []
    while left and right:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    return result + left + right


arr = [1, 5, 3, 9, 6, 32, 2, 6, 56, 26, 697]
print(mergeSort(arr))
