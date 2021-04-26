import numpy as np
from random import shuffle


def selection_sort(array):
    for i in range(len(array)):
        
        smallest_value_index = i
        
        # Search for the smallest value index
        for j in  range(i, len(array)):
            if array[j] < array[smallest_value_index]:
                smallest_value_index = j

        array[i], array[smallest_value_index] = array[smallest_value_index], array[i]

    return array


# Buat array berisi 0 sampai 999
random_array = np.arange(1000)

# Acak isi array
shuffle(random_array)

print(random_array)

print(selection_sort(random_array))
