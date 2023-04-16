from custom_functions import *
from matriks import user, max_user, candi, max_candi, bahan_bangunan, max_bahan_bangunan
from random import randint


def copy_matriks(array, max_array):
    array_baru = [None for i in range(max_array)]

    for i in range(custom_len(array, max_array)):
        array_baru[i] = array[i]
    return array_baru


data = [0, 1, 2, 3]
databaru = copy_matriks(data, 4)
data[2] = 4

print(data)
print(databaru)
