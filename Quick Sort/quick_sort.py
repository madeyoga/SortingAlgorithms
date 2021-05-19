import numpy as np
from random import shuffle


def partition(arr, left_index):
    left_part = arr[:left_index]
    right_part = arr[left_index:]

    if len(left_part) > 1:
        quick_sort(left_part)
    
    if len(right_part) > 1:
        quick_sort(right_part)


def quick_sort(arr):
    last_index = len(arr) - 1
    
    pivot = arr[last_index]

    left_index = -1
    right_index = 0

    while left_index < right_index:
        # Get item from left that is greater than pivot
        left_index = last_index
        for index in range(last_index):
            if arr[index] > pivot:
                left_index = index
                break

        # Get item from right that is smaller than pivot
        right_index = -1
        for index in range(last_index - 1, -1, -1):
            if arr[index] < pivot:
                right_index = index
                break

        if left_index > right_index:
            arr[left_index], arr[last_index] = arr[last_index], arr[left_index]
        else:
            arr[left_index], arr[right_index] = arr[right_index], arr[left_index]

    partition(arr, left_index)
    

# Buat array berisi 0 sampai 999
random_array = np.arange(100000)

# Acak isi array
shuffle(random_array)

print(random_array)

quick_sort(random_array)

##print(random_array)
