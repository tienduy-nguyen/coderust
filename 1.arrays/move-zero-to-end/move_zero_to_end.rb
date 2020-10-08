def move_zero_to_end(arr)
  no_zero = arr.select{|x| x != 0}
  count_zero = arr.length - no_zero.length
  zero  = Array.new(count_zero,0)
  return no_zero + zero
end

arr = [1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0, 9] 
p(move_zero_to_end(arr))