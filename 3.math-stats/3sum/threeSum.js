const threeSum = function (nums) {
  const res = [];
  nums.sort((a, b) => a - b);
  for (let i = 0; i < nums.length - 1; ++i) {
    let l = i + 1;
    let r = nums.length - 1;
    let sum;
    while (l < r) {
      sum = nums[i] + nums[l] + nums[r];
      if (sum < 0) {
        l++;
      } else if (sum > 0) {
        r--;
      } else {
        res.push([nums[i], nums[l], nums[r]]);
        while (l < r && nums[l] === nums[l + 1]) {
          l++;
        }
        while (l < r && nums[r] === nums[r - 1]) {
          r--;
        }
        l++;
        r--;
      }
    }
  }
  return res;
};

arr = [1, -4, 2, -1, 0, 0, -1, 0, 1, 1, 1, 1, 2, 4, 5, 6];
console.log(threeSum(arr));
