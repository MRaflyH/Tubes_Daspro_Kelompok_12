from command_functions import *


def run(command, nama, data_user, data_candi, data_bahan_bangunan):
    if command == "login":
        return Login(nama, data_user), data_user, data_candi, data_bahan_bangunan
    elif command == "logout":
        return Logout(nama), data_user, data_candi, data_bahan_bangunan
    elif command == "summonjin":
        return nama, SummonJin(nama, data_user), data_candi, data_bahan_bangunan
