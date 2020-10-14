const mergeSort = function (arr) {
  if (arr.length <= 1) return arr;
  let mid = Math.floor(arr.length / 2);
  let right = [...arr];
  let left = right.splice(0, mid);

  return merge(mergeSort(left), mergeSort(right));
};

const merge = function (left, right) {
  const result = [];
  while (left.length && right.length) {
    if (left[0] < right[0]) {
      result.push(left.shift());
    } else {
      result.push(right.shift());
    }
  }
  return result.concat(left).concat(right);
};

let arr = [12, 35, 21, 1, 23, 3, 2, 4, 5, 13, 8, 9, 21];
console.log(mergeSort(arr));
