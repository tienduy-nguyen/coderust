const permuteAll = function (nums) {
  let res = [];
  permute(nums, [], res);
  return res;
};
const permute = function (nums, path, res) {
  if (nums.length < 1) {
    res.push(path);
    return res;
  }
  for (let i = 0; i < nums.length; ++i) {
    const newNums = [...nums];
    const item = newNums.splice(i, 1);
    const newPath = [...path, ...item];
    permute(newNums, newPath, res);
  }
};

nums = [1, 2, 3];
console.log(permuteAll(nums));
