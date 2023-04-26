from matriks import user_login, role_login, end_game, user, candi, bahan_bangunan, max_user, max_candi, \
    max_bahan_bangunan, sejarah, max_sejarah
from command_input import run

while not end_game:
    # hilangkan atau tambahkan comment untuk print jika ingin melihat perubahan setiap input
    print("----- DATA -----")
    print(user_login)
    print(role_login)
    print(end_game)
    print(user)
    print(candi)
    print(bahan_bangunan)
    # print("----- SEJARAH -----")
    # for i in sejarah:
    #     if i is None:
    #         break
    #     print(i)
    print()
    masukan = input(">>> ")
    if masukan == "stop":
        break
    user_login, role_login, end_game, user, candi, bahan_bangunan, sejarah = run(masukan.lower(), user_login,
                                                                                 role_login, end_game, user, candi,
                                                                                 bahan_bangunan, max_user, max_candi,
                                                                                 max_bahan_bangunan, sejarah,
                                                                                 max_sejarah)
