#include <iostream>
#include <stdlib.h>
#include <time.h>
#include <vector>


std::vector<int> merge_sort(std::vector<int> arr)
{
	int length = arr.size();

	if (length == 1)
	{
		return arr;
	}

	int middle = length / 2;

	std::vector<int> sorted_left = merge_sort(std::vector<int>(arr.begin(), arr.begin() + middle));
	std::vector<int> sorted_right = merge_sort(std::vector<int>(arr.begin() + middle, arr.end()));

	int left_length = sorted_left.size();
	int right_length = sorted_right.size();

	int left_pointer = 0, right_pointer = 0;

	std::vector<int> temp_vector;

	while (left_pointer < left_length && right_pointer < right_length)
	{
		int left_value = sorted_left[left_pointer];
		int right_value = sorted_right[right_pointer];

		if (left_value < right_value)
		{
			temp_vector.push_back(left_value);
			left_pointer += 1;
		}
		else
		{
			temp_vector.push_back(right_value);
			right_pointer += 1;
		}
	}

	while (left_pointer < left_length)
	{
		temp_vector.push_back(sorted_left.at(left_pointer));
		left_pointer += 1;
	}

	while (right_pointer < right_length)
	{
		temp_vector.push_back(sorted_right.at(right_pointer));
		right_pointer += 1;
	}

	return temp_vector;
}


int main() 
{
	int arr_length = 1000000;

	std::vector<int> arr(arr_length);

	srand(time(0));
	
	// Add random numbers to array
	for (int i = 0; i < arr_length; i++)
	{
		// Get number in range 0 - 100;
		int num = (rand() % (arr_length - 0 + 1)) + 0;
		arr.at(i) = num;
		//std::cout << arr.at(i) << " ";
	}
	
	clock_t t;
	t = clock();

	std::cout << "Sorting " << arr_length << " data...\n\n";

	std::vector<int> sorted_array = merge_sort(arr);
	
	t = clock() - t;
	double time_taken = ((double)t) / CLOCKS_PER_SEC; // calculate the elapsed time
	printf("Sorting took %f seconds to complete ", time_taken);

	std::cout << sorted_array.size() << " data\n\n";

	return 0;
}
