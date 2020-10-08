function quickSort(arr) {
  if (!arr || arr.length <= 1) {
    return arr;
  }
  const mid = Math.floor((0 + arr.length - 1) / 2);
  const pivot = arr[mid];
  const left = [];
  const right = [];
  for (let i = 0; i < arr.length; ++i) {
    if (i === mid) continue;
    if (arr[i] <= pivot) {
      left.push(arr[i]);
    } else {
      right.push(arr[i]);
    }
  }
  return [...quickSort(left), pivot, ...quickSort(right)];
}

const arr = [10, 80, 30, 90, 40, 50, 70];
console.log(quickSort(arr));
