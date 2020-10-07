function maxSlidingWindow(arr, k) {
  let result = [];
  if (arr.length <= k - 1) {
    return result.push(Math.max(...arr));
  }
  let first = arr.slice(0, k);
  let max = Math.max(...first);
  result.push(max);

  for (let i = k; i < arr.length; i++) {
    if (arr[i] > max) {
      max = arr[i];
      result.push(arr[i]);
    } else {
      result.push(max);
    }
  }
  return result;
}

const arr = [1, 2, 3, 1, 4, 5, 2, 3, 6];
const k = 3;
console.log(maxSlidingWindow(arr, k));
