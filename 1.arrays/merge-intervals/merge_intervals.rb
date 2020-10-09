def merge_intervals(intervals)
  if intervals.empty? || intervals.length <= 1
    return intervals
  end
  intervals = intervals.sort_by{|x| x.first}
  result = []
  intervals.each do |cur|
    if result.length == 0
      result.push(cur)
    else 
      prev = result.last
      if prev.last >= cur.first
        prev[-1] = [prev.last, cur.last].max
      else
        result.push(cur)
      end
    end
  end
  return result
end



intervals = [[1,3],[8,10],[2,6],[15,18]]
intervals2 = [[1,4],[4,5]]
p(merge_intervals(intervals))
p(merge_intervals(intervals2))