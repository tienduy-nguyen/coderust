using System;
namespace BinarySearch
{
  class Propgram
  {
    static void Main(string[] args)
    {
      int[] arr = new int[] { 3, 5, 12, 56, 92, 123, 156, 190, 201, 222 };
      int key = 12;
      Console.WriteLine(binarySearch(arr, key));
    }
    static int binarySearch(int[] arr, int key)
    {
      int lower = 0;
      int upper = arr.Length;
      int indexMid = 0;
      int mid = 0;
      while (lower < upper)
      {
        indexMid = lower + (upper - lower) / 2;
        mid = arr[indexMid];
        if (mid == key)
        {
          return indexMid;
        }
        else if (mid < key)
        {
          lower = indexMid + 1;
        }
        else
        {
          upper = indexMid - 1;
        }
      }
      return -1;
    }
  }
}