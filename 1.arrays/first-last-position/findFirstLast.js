function findFirstLast(arr, key) {
  const indices = arr.map((e, i) => (e === key ? i : ''));
  return [indices.first, indices.last];
}

const arr1 = [1, 3, 5, 5, 5, 5, 67, 123, 125];
const key1 = 5;
const arr2 = [1, 3, 5, 5, 5, 5, 7, 123, 125];
const key2 = 7;
console.log(find_first_last(arr1, key1));
console.log(find_first_last(arr2, key2));
