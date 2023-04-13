from matriks import user_login, user, candi, bahan_bangunan
from command_input import run

while True:
    masukan = input(">>> ")
    if masukan == "stop":
        break
    user_login, user, candi, bahan_bangunan = run(masukan, user_login, user, candi, bahan_bangunan)
