import numpy as np
from random import shuffle


def bubble_sort(array):
    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

    return array


# Buat array berisi 0 sampai 999
random_array = np.arange(1000)

# Acak isi array
shuffle(random_array)

print(random_array)

print(bubble_sort(random_array))

