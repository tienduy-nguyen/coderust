function findPair(arr, sum) {
  let found = -1;
  for (let i = 0; i < arr.length; ++i) {
    const search = sum - arr[i];
    let newArr = [...arr];
    newArr.splice(i, 1);
    if (newArr.includes(search)) {
      found = [arr[i], search];
      break;
    }
  }
  return found;
}

arr1 = [0, -1, 2, -3, 1];
arr2 = [1, -2, 1, 0, 5];
arr3 = [1];
sum1 = -2;
sum2 = 0;
sum3 = 1;
console.log(findPair(arr1, sum1));
console.log(findPair(arr2, sum2));
console.log(findPair(arr3, sum3));
