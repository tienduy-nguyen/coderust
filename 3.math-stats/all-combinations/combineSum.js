const combineSum = function (candidates, target) {
  const res = [];
  dfs(candidates, target, [], res);
  return res;
};
const dfs = function (nums, target, path, res) {
  if (target === 0) {
    res.push(path);
    return res;
  }
  for (let i = 0; i < nums.length; ++i) {
    const newNums = [...nums];
    if (i > 0) {
      newNums.splice(0, i);
    }
    if (nums[i] > target) {
      continue;
    }
    dfs(newNums, target - nums[i], [...path, ...[nums[i]]], res);
  }
};

const arr = [2, 3, 6, 7];
const target = 7;
console.log(combineSum(arr, 7));
