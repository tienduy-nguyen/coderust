def find_common_number(*args)
  result = args[0]
  for x in args
    result = result & x
  end
  return result
end

arr1 = [1,5,10,20,40,80]
arr2 = [6,27,20,80,100]
arr3 = [3,4,15,20,30,70,80,120]
p find_common_number(arr1, arr2, arr3)

def find_common_number2(*args)
  result = args[0]
  check = []
  for arr in args
    arr.each do |item|
      if result.include?(item)
        check.push(item)
      end
    end
    result = check.clone
    check = []
  end
  return result
end
p find_common_number2(arr1, arr2, arr3)
