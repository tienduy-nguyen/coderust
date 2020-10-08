function leftRotate(arr, d) {
  const first = arr.slice(0, d);
  const rest = arr.slice(d, arr.length - 1);
  return [].concat(rest, first);
}
const arr1 = [1, 2, 3, 4, 5, 6, 7];
console.log(leftRotate(arr1, 2));
