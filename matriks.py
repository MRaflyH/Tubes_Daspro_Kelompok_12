from custom_functions import custom_len, csv_to_matriks

max_sejarah = 9999
max_user = 102
max_candi = 100
max_bahan_bangunan = 3

user_login = None
role_login = None
end_game = False
user = csv_to_matriks("user.csv", 3, max_user)
candi = csv_to_matriks("candi.csv", 5, max_candi)
bahan_bangunan = csv_to_matriks("bahan_bangunan.csv", 3, max_bahan_bangunan)
sejarah = [None for i in range(max_sejarah)]

sejarah[0] = [user_login, role_login, user, candi, bahan_bangunan]

# for i in range(0, custom_len(candi, max_candi)):
#     candi[i][0] = int(candi[i][0])
#     if candi[i][1] != "None":
#         candi[i][2] = int(candi[i][2])
#         candi[i][3] = int(candi[i][3])
#         candi[i][4] = int(candi[i][4])
#     else:
#         candi[i][1] = None
#         candi[i][2] = None
#         candi[i][3] = None
#         candi[i][4] = None

for i in range(0, custom_len(bahan_bangunan, max_bahan_bangunan)):
    bahan_bangunan[i][0] = str(bahan_bangunan[i][0])
    bahan_bangunan[i][1] = str(bahan_bangunan[i][1])
    bahan_bangunan[i][2] = int(bahan_bangunan[i][2])

# test
