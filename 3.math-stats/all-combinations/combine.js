const combine = function (n, k) {
  const nums = Array.from({ length: n }, (_, i) => i + 1);
  console.log(nums);
  const res = [];
  dfs(nums, k, [], res);
  return res;
};

const dfs = function (nums, k, path, res) {
  if (path.length === k) {
    res.push(path);
    return res;
  }
  for (let i = 0; i < nums.length; ++i) {
    const newNums = [...nums];
    newNums.splice(0, i + 1);
    dfs(newNums, k, [...path, ...[nums[i]]], res);
  }
};

console.log(combine(4, 2));
