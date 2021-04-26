#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void selection_sort(int n, int* arr)
{
	int temp;
	for (int i = 0; i < n; i++)
	{
		int smallest_value_index = i;

		for (int j = i; j < n; j++)
		{
			if (arr[j] < arr[smallest_value_index])
			{
				smallest_value_index = j;
			}
		}
		// swap
		temp = arr[i];
		arr[i] = arr[smallest_value_index];
		arr[smallest_value_index] = temp;
	}
}

int main()
{
	int arr_length = 100;
	int arr[100];

	srand(time(0));

	// Add random numbers to array
	for (int i = 0; i < arr_length; i++)
	{
		// Get number in range 0 - 100;
		int num = (rand() % (100 - 0 + 1)) + 0;
		arr[i] = num;
		printf("%d ", arr[i]);
	}

	selection_sort(arr_length, arr);

	printf("\n\nSorted Array: \n");

	// print array
	for (int i = 0; i < arr_length; i++)
	{
		printf("%d ", arr[i]);
	}

	return 0;
}
