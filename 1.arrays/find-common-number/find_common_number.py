def find_common_number(*args):
  result = args[0]
  for arr in args:
    result = insect_array(result, arr)
  return result



def union_array(arr1, arr2):
  return list(set.union(arr1, arr2))

def insect_array(arr1, arr2):
  return list(set(arr1) & set(arr2))


arr1 = [1,5,10,20,40,80]
arr2 = [6,27,20,80,100]
arr3 = [3,4,15,20,30,70,80,120]
print(find_common_number(arr1, arr2, arr3))