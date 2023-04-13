from custom_functions import custom_len, csv_to_matriks

user_login = ""
user = csv_to_matriks("user.csv")
candi = csv_to_matriks("candi.csv")
bahan_bangunan = csv_to_matriks("bahan_bangunan.csv")

for i in range(1, custom_len(candi)):
    candi[i][0] = int(candi[i][0])
    candi[i][2] = int(candi[i][2])
    candi[i][3] = int(candi[i][3])
    candi[i][4] = int(candi[i][4])

for i in range(1, custom_len(bahan_bangunan)):
    bahan_bangunan[i][2] = int(bahan_bangunan[i][2])