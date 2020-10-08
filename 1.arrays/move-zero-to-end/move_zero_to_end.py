def move_zero_to_end(arr):
  no_zero = list(filter(lambda x: x!= 0, arr))
  count_zero = len(arr)-len(no_zero)
  zero = []
  for i in range(count_zero):
    zero.append(0)
  return no_zero + zero


arr = [1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0, 9] 
print(move_zero_to_end(arr))