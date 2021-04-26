import numpy as np
from random import shuffle


def insertion_sort(array):
    for i in range(len(array)):
        current_key = array[i]
        for j in range(i - 1, -1, -1):
            if current_key < array[j]:
                array[j + 1], array[j] = array[j], array[j + 1]
            else:
                break
    return array


# Buat array berisi 0 sampai 999
random_array = np.arange(1000)

# Acak isi array
shuffle(random_array)

print(random_array)

print(insertion_sort(random_array))
