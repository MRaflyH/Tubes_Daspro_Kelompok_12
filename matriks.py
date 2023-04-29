from custom_functions import custom_len, csv_to_matriks
from argparse import *
import os
import time

max_user = 102
max_candi = 100
max_bahan_bangunan = 3

user = [None for i in range(max_user)]
candi = [None for i in range(max_candi)]
bahan_bangunan = [None for i in range(max_bahan_bangunan)]

user_login = None
role_login = None
end_game = False

parser = ArgumentParser()
parser.add_argument("nama_folder", nargs='?', type=str, default='')
arg = parser.parse_args()
folder = arg.nama_folder


# F13 - Load
if os.path.isdir(folder):
    print("\nLoading...")
    time.sleep(1)

    user = csv_to_matriks(folder + "/user.csv", 3, max_user)
    candi = csv_to_matriks(folder + "/candi.csv", 5, max_candi)
    bahan_bangunan = csv_to_matriks(folder + "/bahan_bangunan.csv", 3, max_bahan_bangunan)

    print("\nSelamat datang di program \"Manajerial Candi\"")
    print("Masukkan command \"help\" untuk daftar command yang dapat kamu panggil.")

elif folder == '':
    print("\nTidak ada nama folder yang diberikan!\n")
    print("Usage: " + "python main.py" + " <nama_folder>")
    end_game = True
else:
    print(f"\nfolder \"{folder}\" tidak ditemukan")
    end_game = True
print()


for i in range(0, custom_len(candi, max_candi)):
    candi[i][0] = int(candi[i][0])
    if candi[i][1] != "None":
        candi[i][2] = int(candi[i][2])
        candi[i][3] = int(candi[i][3])
        candi[i][4] = int(candi[i][4])
    else:
        candi[i][1] = None
        candi[i][2] = None
        candi[i][3] = None
        candi[i][4] = None

for i in range(0, custom_len(bahan_bangunan, max_bahan_bangunan)):
    bahan_bangunan[i][2] = int(bahan_bangunan[i][2])

# test
