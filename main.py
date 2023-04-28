from matriks import user_login, role_login, end_game, user, candi, bahan_bangunan, max_user, max_candi, \
    max_bahan_bangunan
from custom_functions import bcolors
from command_input import run

while not end_game:
    masukan = input(f"{bcolors.input}>>> {bcolors.endc}")
    if masukan == "stop":
        break
    user_login, role_login, end_game, user, candi, bahan_bangunan = run(masukan.lower(), user_login,
                                                                        role_login, end_game, user, candi,
                                                                        bahan_bangunan, max_user, max_candi,
                                                                        max_bahan_bangunan)
