from command_functions import *


def run(command, nama, data_user, data_candi, data_bahan_bangunan):
    if command == "login":
        return login(nama, data_user), data_user, data_candi, data_bahan_bangunan
    elif command == "logout":
        return logout(nama), data_user, data_candi, data_bahan_bangunan
    elif command == "summonjin":
        return nama, summon_jin(nama, data_user), data_candi, data_bahan_bangunan
    elif command == "hapusjin":
        data_user, data_candi = hilangkan_jin(nama, data_user, data_candi)
        return nama, data_user, data_candi, data_bahan_bangunan
    elif command == "ubahjin":
        return nama, ubah_tipe_jin(nama, data_user), data_candi, data_bahan_bangunan
