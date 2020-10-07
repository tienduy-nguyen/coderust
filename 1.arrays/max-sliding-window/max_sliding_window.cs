using System;
using System.Collections.Generic;
using System.Linq;
namespace MaxSlidingWindow
{
  class Propgram
  {
    public static void Main()
    {
      List<int> arr = new List<int>() { 1, 2, 3 };
      int k = 3;
      var result = maxSlidingWindow(arr, k);
      foreach (var item in result)
      {
        Console.WriteLine(item);
        Console.WriteLine("Something");
      }

    }
    static List<int> maxSlidingWindow(List<int> arr, int k)
    {
      List<int> result = new List<int>();
      if (arr.Count <= (k - 1))
      {

        result.Add(arr.Max());
        return result;
      }

      List<int> first = arr.Take(k - 1).ToList();
      int max = first.Max();
      for (int i = k; i < arr.Count; ++i)
      {
        if (arr[i] > max)
        {
          max = arr[i];
        }
        result.Add(max);
      }
      return result;

    }
  }
}