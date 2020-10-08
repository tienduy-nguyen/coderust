'''
Two intervals i1, i2overlap if the following requirements are satisfied:

requirement 1: i1.end >= i2.start
requirement 2: i1.start <= i2.end
We preprocess the list by sorting intervals by starts increasingly.
In this way, requirement 2 i1.start <= i2.start < i2.end is promised.
We only have to compare i1.end with i2.start to see if requirement 1 is satisfied.
'''

def merge(intervals):
  # Sort by first element in list children
  intervals = sorted(intervals, key=lambda x: x[0])
  result = []
  for cur in intervals:
    if len(result) < 1:
      result.append(cur)
    else:
      prev = result[-1]
      if prev[-1] >= cur[0]:
        prev[-1] = max(prev[-1], cur[-1])
      else:
        result.append(cur)
  return result


def merge_intervals2(intervals):
  if not intervals or len(intervals) <=1:
    return intervals
  result = []
  i = len(intervals)-1
  while i >= 0:
    arr = list(range(intervals[i][0], intervals[i][-1]+1))
    k = 0
    for j in range(1, len(intervals)):
      if intervals[i-j][-1] in arr:
        k +=1
    if k > 0:
      result.append([intervals[i-k][0],arr[-1]])
    else:
      result.append([arr[0], arr[-1]])
    i = i-k-1
  return list(reversed(result))

intervals = [[1,3],[2,6],[8,10],[15,18]]
intervals2 = [[1,4],[4,5]]
print(merge(intervals))
print(merge(intervals2))
print(merge2(intervals))
print(merge2(intervals2))
