from matriks import user_login, user, candi, bahan_bangunan
from command_input import run

while True:
    # hilangkan comment untuk print jika ingin melihat perubahan setiap input
    print(user_login)
    print(user)
    # print(candi)
    # print(bahan_bangunan)
    masukan = input(">>> ")
    if masukan == "stop":
        break
    user_login, user, candi, bahan_bangunan = run(masukan, user_login, user, candi, bahan_bangunan)
