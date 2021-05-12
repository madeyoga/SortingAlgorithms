import numpy as np
from random import shuffle
import time


def merge_sort(arr):
    if len(arr) > 1:

        middle = len(arr) // 2

        sorted_left = arr[:middle]
        sorted_right = arr[middle:]
        
        merge_sort(sorted_left)
        merge_sort(sorted_right)

        left_pointer = 0
        right_pointer = 0
        main_pointer = 0
        
        left_len = len(sorted_left)
        right_len = len(sorted_right)
        
        # Merge
        while left_pointer < left_len and right_pointer < right_len:
            left = sorted_left[left_pointer]
            right = sorted_right[right_pointer]
            
            if left < right:
                arr[main_pointer] = left
                left_pointer += 1
            else:
                arr[main_pointer] = right
                right_pointer += 1

            main_pointer += 1

        while left_pointer < left_len:
            arr[main_pointer] = sorted_left[left_pointer]
            left_pointer += 1
            main_pointer += 1

        while right_pointer < right_len:
            arr[main_pointer] = sorted_right[right_pointer]
            right_pointer += 1
            main_pointer += 1


# Buat array berisi 0 sampai n_data
n_data = 1000000
print("Generating {} data...".format(n_data))
random_array = np.arange(n_data).tolist()

# Acak isi array
shuffle(random_array)

print(random_array)

start = time.time()
merge_sort(random_array)
print("Elapsed time:", time.time() - start)

##print(random_array)
