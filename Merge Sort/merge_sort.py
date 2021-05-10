import numpy as np
from random import shuffle


def merge_sort(arr):
    if len(arr) == 1:
        return arr

    middle = len(arr) // 2

    sorted_left = merge_sort(arr[:middle])
    sorted_right = merge_sort(arr[middle:])

    left_pointer = 0
    right_pointer = 0

    # Merge
    temp_list = []
    while left_pointer < len(sorted_left) and right_pointer < len(sorted_right):
        left = sorted_left[left_pointer]
        right = sorted_right[right_pointer]
        
        if left > right:
            temp_list.append(right)
            right_pointer += 1
        else:
            temp_list.append(left)
            left_pointer += 1

    if left_pointer < len(sorted_left):
        temp_list.extend(sorted_left[left_pointer:])

    if right_pointer < len(sorted_right):
        temp_list.extend(sorted_right[right_pointer:])

    return temp_list


# Buat array berisi 0 sampai 999
random_array = np.arange(100000)

# Acak isi array
shuffle(random_array)

print(random_array)

print(merge_sort(random_array))
