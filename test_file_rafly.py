from custom_functions import *
from matriks import user, max_user

length_jin = 100
data_jin = [None for i in range(length_jin)]

for i in range(custom_len(user, max_user)-2):
    data_jin[i] = user[i+2][0]

print(data_jin)
print(urutkan_leksikografis(data_jin, length_jin))

print(count_jin_total_pengumpul_pembangun(user, max_user))