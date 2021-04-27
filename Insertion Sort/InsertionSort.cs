using System;
using System.Collections.Generic;
using System.Text;

namespace Test
{
    static class Program
    {
        static void Main(string[] args)
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

            // memanggil Method InsertionSort()
            arr.InsertionSort();

            // tampilakan isi array setelah di sorting
            Console.WriteLine("Array sesudah sorting:");
            for (var i = 0; i < arr.Count; i++)
            {
                Console.WriteLine(arr[i]);
            }
            Console.WriteLine();
            Console.ReadLine();
        }

        public static void InsertionSort(this List<int> arr)
        {
            int temp; 
            int	key;

            for (var i = 0; i < arr.Count; i++)
            {
                key = arr[i];
                for (var j = i - 1; j >= 0; j--)
                {
                    if (key < arr[j])
                    {
                        // swap
                        temp = arr[j + 1];
                        arr[j + 1] = arr[j];
                        arr[j] = temp;
                    }
                }
            }
        }
    }
}
