from matriks import user_login, user, candi, bahan_bangunan, max_user, max_candi, max_bahan_bangunan
from command_input import run

while True:
    # hilangkan atau tambahkan comment untuk print jika ingin melihat perubahan setiap input
    # print(user_login)
    # print(user)
    # print(candi)
    # print(bahan_bangunan)
    masukan = input(">>> ")
    if masukan == "stop":
        break
    user_login, user, candi, bahan_bangunan = run(masukan, user_login, user, candi, bahan_bangunan, max_user, max_candi, max_bahan_bangunan)
