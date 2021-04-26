#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void insertion_sort(int n, int* arr)
{
	int temp;
	for (int i = 0; i < n; i++)
	{
		int current_key = arr[i];

		for (int j = i - 1; j >= 0; j--)
		{
			if (current_key < arr[j])
			{
				// swap
				temp = arr[j + 1];
				arr[j + 1] = arr[j];
				arr[j] = temp;
			}
			else
			{
				break;
			}
		}
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

	insertion_sort(arr_length, arr);

	printf("\n\nSorted Array: \n");

	// print array
	for (int i = 0; i < arr_length; i++)
	{
		printf("%d ", arr[i]);
	}

	return 0;
}
