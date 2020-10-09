function mergeIntervals(intervals) {
  intervals = intervals.sort((a, b) => a[0] - b[0]);
  const result = [];
  intervals.forEach((cur) => {
    if (result.length === 0) {
      result.push(cur);
    } else {
      let prev = result[result.length - 1];
      if (prev[prev.length - 1] >= cur[0]) {
        prev[prev.length - 1] = Math.max(
          prev[prev.length - 1],
          cur[cur.length - 1]
        );
      } else {
        result.push(cur);
      }
    }
  });

  return result;
}

const intervals = [
  [1, 3],
  [8, 10],
  [2, 6],
  [15, 18],
];
const intervals2 = [
  [1, 4],
  [4, 5],
];
console.log(mergeIntervals(intervals));
console.log(mergeIntervals(intervals2));
