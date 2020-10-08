def max_profit(arr)
  if !arr.any?
    return 0
  end
  maxPrice = 0
  minPrice = arr[0]
  for i in 1..(arr.length-1)
    minPrice = [minPrice, arr[i]].min
    maxPrice = [maxPrice, arr[i]].max
  end
  return maxPrice
end



arr = [100, 180, 260, 310, 40, 535, 695]
p(max_profit(arr))