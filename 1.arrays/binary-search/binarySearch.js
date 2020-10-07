function binarySearch(arr, key) {
  let lower = 0;
  let upper = arr.length - 1;
  let indexMid = 0;
  let mid = arr[indexMid];
  while (lower < upper) {
    indexMid = Math.floor(lower + (upper - lower) / 2);
    mid = arr[indexMid];
    if (mid === key) {
      return indexMid;
    } else if (mid < key) {
      lower = indexMid + 1;
    } else {
      upper = indexMid - 1;
    }
  }
  return -1;
}

arr = [3, 5, 12, 56, 92, 123, 156, 190, 201, 222];
key = 12;
result = binarySearch(arr, key); //2
console.log(result);

// Complexity
// Worst case time complexity: O(log N)
// Average case time complexity: O(log N)
// Best case time complexity: O(1)
// Space complexity: O(1)
