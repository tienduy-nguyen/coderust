function maxProfit(prices) {
  if (!prices) {
    return 0;
  }
  let maxPrice = 0;
  let minPrice = prices[0];
  for (let i = 1; i < prices.length; ++i) {
    minPrice = Math.min(minPrice, prices[i]);
    maxPrice = Math.max(maxPrice, prices[i]);
  }
  return maxPrice;
}

const arr = [100, 180, 260, 310, 40, 535, 695];
console.log(maxProfit(arr));
