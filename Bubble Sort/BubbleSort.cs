using System;
using System.Collections.Generic;

namespace ConsoleApp
{
	public static class Program
	{		
		public static void Main(string[] args)
		{
			// deklarasi variable 
			var rand = new Random(0);
			var arr = new List<int>();

			// isi array dengan random data
			for (var i = 0; i < 10; i++)
			{
				arr.Add(rand.Next() % 100);
			}

			// tampilakan isi array
			Console.WriteLine("Array sebelum sorting:");
			for (var i = 0; i < arr.Count; i++)
			{
				Console.WriteLine(arr[i]);
			}
			Console.WriteLine();

			// memanggil Method BubbleSort()
			arr.BubbleSort();

			// tampilakan isi array setelah di sorting
			Console.WriteLine("Array sesudah sorting:");
			for (var i = 0; i < arr.Count; i++)
			{
				Console.WriteLine(arr[i]);
			}
			Console.WriteLine();
			Console.ReadLine();
		}
		public static void BubbleSort(this List<int> item)
		{
			int temp;
			for (var i = 0; i < item.Count; i++)
			{
				for (var j = i; j < item.Count; j++)
				{
					if (item[i] > (item[j]))
					{
						temp = item[j];
						item[j] = item[i];
						item[i] = temp;
					}
				}
			}
		}
    }
}
