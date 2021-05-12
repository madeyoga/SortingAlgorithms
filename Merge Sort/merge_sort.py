from random import shuffle
import time


def merge_sort(arr):
    length = len(arr)
    
    if length == 1:
        return arr

    middle = length // 2
    
    sorted_left = merge_sort(arr[:middle])
    sorted_right = merge_sort(arr[middle:])

    left_pointer = 0
    right_pointer = 0

    left_len = len(sorted_left)
    right_len = len(sorted_right)
    
    # Merge
    temp_list = []
    while left_pointer < left_len and right_pointer < right_len:
        left = sorted_left[left_pointer]
        right = sorted_right[right_pointer]
        
        if left > right:
            temp_list.append(right)
            right_pointer += 1
        else:
            temp_list.append(left)
            left_pointer += 1

    while left_pointer < left_len:
        temp_list.append(sorted_left[left_pointer])
        left_pointer += 1

    while right_pointer < right_len:
        temp_list.append(sorted_right[right_pointer])
        right_pointer += 1
        
##    if left_pointer < left_len:
##        temp_list.extend(sorted_left[left_pointer:])
##
##    if right_pointer < right_len:
##        temp_list.extend(sorted_right[right_pointer:])

    return temp_list


# Buat array berisi 0 sampai n_data
n_data = 10000000
print("Generating {} data...".format(n_data))
random_array = []
for i in range(n_data):
    random_array.append(i)

# Acak isi array
shuffle(random_array)

print("Sorting...")
start = time.time()
sorted_array = merge_sort(random_array)
print("Elapsed time:", time.time() - start)

input("Press enter to exit...")
