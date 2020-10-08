function moveZeroToEnd(arr) {
  noZero = arr.filter((x) => x !== 0);
  countZero = arr.length - noZero.length;
  zero = Array(countZero).fill(0);
  return [...noZero, ...zero];
}

const arr = [1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0, 9];
console.log(moveZeroToEnd(arr));
