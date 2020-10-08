function findCommonNumber(...args) {
  let result = args[0];
  args.forEach((x) => {
    result = insectArr(result, x);
  });
  return result;
}

function findCommonNumber2(...args) {
  let result = args[0];
  for (let arr of args) {
    result = insectArr2(result, arr);
  }
  return result;
}
function insectArr(arr1, arr2) {
  return arr1.filter((x) => arr2.includes(x));
}
function insectArr2(arr1, arr2) {
  let result = [];
  arr2.forEach((x) => {
    if (arr1.includes(x)) {
      result.push(x);
    }
  });
  return result;
}
function unionArr(arr1, arr2) {
  return [...new Set([...arr1, ...arr2])];
}

const arr1 = [1, 5, 10, 20, 40, 80];
const arr2 = [6, 27, 20, 80, 100];
const arr3 = [3, 4, 15, 20, 30, 70, 80, 120];
console.log(findCommonNumber2(arr1, arr2, arr3));
console.log(findCommonNumber(arr1, arr2, arr3));
