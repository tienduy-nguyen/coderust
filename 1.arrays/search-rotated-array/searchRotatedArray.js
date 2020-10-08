function pivotBinarySearch(arr, key) {
  let high = arr.length;
  let pivot = findPivot(arr, 0, high);
  if (pivot === -1) {
    return binarySearch(arr, 0, high, key);
  }
  if (arr[pivot] === key) {
    return pivot;
  }
  if (arr[0] <= key) {
    return binarySearch(arr, 0, pivot - 1, key);
  }
  return binarySearch(arr, pivot + 1, high, key);
}

function findPivot(arr, low, high) {
  if (high < low) {
    return -1;
  }
  if (low === high) {
    return low;
  }
  mid = Math.floor((low + high) / 2);
  if (mid < high && arr[mid] > arr[mid + 1]) {
    return mid;
  }
  if (mid > low && arr[mid] < arr[mid - 1]) {
    return mid;
  }
  if (arr[low] >= arr[mid]) {
    return findPivot(arr, low, mid - 1);
  }
  return findPivot(arr, mid + 1, high);
}

function binarySearch(arr, low, high, key) {
  if (high < low) {
    return -1;
  }
  mid = Math.floor((low + high) / 2);
  if (arr[mid] === key) {
    return mid;
  }
  if (arr[mid] > key) {
    return binarySearch(arr, low, mid - 1, key);
  }
  return binarySearch(arr, mid + 1, high, key);
}

const arr1 = [5, 6, 7, 8, 9, 10, 1, 2, 3];
const key1 = 3;
const arr2 = [5, 6, 7, 8, 9, 10, 1, 2, 3];
const key2 = 30;
const arr3 = [30, 40, 50, 10, 20];
const key3 = 10;
console.log(pivotBinarySearch(arr1, key1));
console.log(pivotBinarySearch(arr2, key2));
console.log(pivotBinarySearch(arr3, key3));
