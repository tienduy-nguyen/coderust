def max_profit(prices) -> int:
  if not prices:
    return 0
  minPrice = prices[0]
  maxPrice = 0
  for i in range(1, len(prices)):
    minPrice = min(prices[i], minPrice)
    maxPrice = max(prices[i],maxPrice)
  return maxPrice


arr = [100, 180, 260, 310, 40, 535, 695]
print(max_profit(arr))