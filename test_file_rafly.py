from custom_functions import *
from matriks import user, max_user, candi, max_candi, bahan_bangunan, max_bahan_bangunan
from random import randint

nama = "jin1"
air = randint(1, 5)
batu = randint(1, 5)
pasir = randint(1, 5)

print(candi)
print(bahan_bangunan)
candi = append_candi(nama, air, batu, pasir, candi, max_candi)
bahan_bangunan = pakai_bahan(air, batu, pasir, bahan_bangunan, max_bahan_bangunan)
print(candi)
print(bahan_bangunan)
