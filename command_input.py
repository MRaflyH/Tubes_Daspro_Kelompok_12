from command_functions import *


def run(command, nama, role, end, data_user, data_candi, data_bahan_bangunan, max_data_user, max_data_candi, max_data_bahan_bangunan):
    if command == "login":
        nama, role = login(nama, role, data_user, max_data_user)
    elif command == "logout":
        nama, role = logout(nama)
    elif command == "summonjin":
        data_user = summon_jin(nama, role, data_user, max_data_user)
    elif command == "hapusjin":
        data_user, data_candi = hilangkan_jin(nama, role, data_user, data_candi, max_data_user, max_data_candi)
    elif command == "ubahjin":
        data_user = ubah_tipe_jin(nama, role, data_user, max_data_user)
    elif command == "bangun":
        data_candi, data_bahan_bangunan = bangun(nama, role, data_candi, data_bahan_bangunan, max_data_candi, max_data_bahan_bangunan)
    elif command == "kumpul":
        data_bahan_bangunan = kumpul(nama, role, data_bahan_bangunan, max_data_bahan_bangunan)
    elif command == "batchkumpul":
        data_bahan_bangunan = batch_kumpul(nama, role, data_user, max_data_user, data_bahan_bangunan, max_data_bahan_bangunan)
    elif command == "batchbangun":
        data_candi, data_bahan_bangunan = batch_bangun(nama, role, data_user, data_candi, data_bahan_bangunan, max_data_user, max_data_candi, max_data_bahan_bangunan)
    elif command == "laporanjin":
        laporan_jin(role, data_user, data_candi, data_bahan_bangunan, max_data_user, max_data_candi, max_data_bahan_bangunan)
    elif command == "laporancandi":
        laporan_candi(role, data_candi, max_data_candi)
    elif command == "hancurkancandi":
        data_candi = hancurkan_candi(role, data_candi, max_data_candi)
    elif command == "ayamberkokok":
        end = ayam_berkokok(nama, role, data_candi, max_data_candi)
    elif command == "help":
        help_role(role)
    elif command == "save":
        save(data_user, data_candi, data_bahan_bangunan, max_data_user, max_data_candi, max_data_bahan_bangunan)
    elif command == "exit":
        end = exit_game(data_user, data_candi, data_bahan_bangunan, max_data_user, max_data_candi, max_data_bahan_bangunan)
    elif command == "status":
        print(nama)
        print(role)
        print(end)
        print()
        print(data_user)
        print()
        print(data_candi)
        print()
        print(data_bahan_bangunan)

    print()
    return nama, role, end, data_user, data_candi, data_bahan_bangunan
