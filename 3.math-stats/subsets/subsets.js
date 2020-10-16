const subsets = function (nums) {
  res = [];
  dfs(nums, [], res);
  return res;
};

const dfs = function (nums, path, res) {
  res.push(path);
  for (let i = 0; i < nums.length; ++i) {
    const newNums = [...nums];
    newNums.splice(0, i + 1);
    dfs(newNums, [...path, ...[nums[i]]], res);
  }
  return res;
};
const nums = [1, 2, 3];
console.log(subsets(nums));
