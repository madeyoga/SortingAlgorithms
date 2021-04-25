#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void bubble_sort(int n, int *arr)
{
	int temp;
	for (int i = 0; i < n; i++)
	{
		for (int j = i; j < n; j++)
		{
			if (arr[i] > arr[j])
			{
				// swap
				temp = arr[i];
				arr[i] = arr[j];
				arr[j] = temp;
			}
		}
	}
}

int main() 
{
	int arr_length = 25;
	int arr[25];

	srand(time(0));

	// Add random numbers to array
	for (int i = 0; i < arr_length; i++) 
	{
		// Get number in range 0 - 100;
		int num = (rand() % (100 - 0 + 1)) + 0;
		arr[i] = num;
		printf("%d ", arr[i]);
	}

	bubble_sort(arr_length, arr);

	printf("\n\nSorted Array: ");

	// print array
	for (int i = 0; i < arr_length; i++)
	{
		printf("%d ", arr[i]);
	}

	return 0;
}
