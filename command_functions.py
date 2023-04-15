from custom_functions import cek_nama_terdaftar, cek_password_cocok, daftar_jin, custom_append, custom_len, custom_pop, \
    hapus_candi_jin

"""
JUDUL
"""

# F01 - Login
def login(nama, data_user):
    berhasil_login = False
    input_user = ""

    if nama is not None:
        print(f"Login gagal!\nAnda telah login dengan username {nama}, silahkan lakukan “logout” sebelum melakukan "
              "login kembali.")
    else:
        input_user = input("Username: ")
        input_password = input("Password: ")

        if not cek_nama_terdaftar(input_user, data_user):
            print("Username tidak terdaftar!\n")
        elif not cek_password_cocok(input_password, input_user, data_user):
            print("Password salah!\n")
        else:
            print(f"Selamat datang, {input_user}!\n")
            print('Masukkan command "help" untuk daftar command yang dapat kamu panggil.\n')
            berhasil_login = True

    if berhasil_login:
        return input_user
    else:
        return nama

# F02 - Logout
def logout(nama):
    if nama is None:
        print("Logout gagal!\nAnda belum login, silahkan login terlebih dahulu sebelum melakukan logout")
    return None

# F03 - Summon Jin
def summon_jin(nama, data_user):
    if nama != "Bondowoso":
        print(f"{nama} tidak memiliki akses untuk summonjin")
    else:
        print("Jenis jin yang dapat dipanggil:")
        print("  (1) Pengumpul - Bertugas mengumpulkan bahan bangunan")
        print("  (2) Pembangun - Bertugas membangun candi")

        data_jin = daftar_jin(data_user)

        print("Mengumpulkan sesajen...\nMenyerahkan sesajen...\nMembacakan mantra...\n")
        print(f"Jin {data_jin[0]} berhasil dipanggil!\n")

        data_user = custom_append(data_user, data_jin)

    return data_user

# F04 - Hilangkan Jin (Akses : Bandung Bondowoso)
# fungsi hilangkan_jin() bisa menghapus bondowoso dan roro (harusnya gaboleh)
def hilangkan_jin(nama, data_user, data_candi):
    if nama != "Bondowoso":
        print(f"{nama} tidak memiliki akses untuk summonjin")
    else:
        confirm = ""
        jin = input("Masukkan username jin: ")
        if not cek_nama_terdaftar(jin, data_user):
            print("Tidak ada jin dengan username tersebut.")
        else:
            confirm = input(f"Apakah anda yakin ingin menghapus jin dengan username {jin} (Y/N)? ")

        if confirm == 'Y':
            for i in range(custom_len(data_user)):
                if data_user[i][0] == jin:
                    data_user = custom_pop(data_user, i)
                    break
            data_candi = hapus_candi_jin(jin, data_candi)
            print("Jin telah berhasil dihapus dari alam gaib.")
        else:
            print("Jin tidak dihapus dari alam gaib.")

    return data_user, data_candi

# F05 - Ubah Tipe Jin
def ubah_tipe_jin(nama, data_user):
    if nama != "Bondowoso":
        print(f"{nama} tidak memiliki akses untuk summonjin")
    else:
        confirm = ""
        role_jin = ""
        reverse_role_jin = ""
        jin = input("Masukkan username jin: ")

        if not cek_nama_terdaftar(jin, data_user):
            print("Tidak ada jin dengan username tersebut.")
        else:
            for i in range(custom_len(data_user)):
                if data_user[i][0] == jin:
                    if data_user[i][2] == "jin_pengumpul":
                        confirm = input(
                            "Jin ini bertipe \"Pengumpul\". Yakin ingin mengubah ke tipe \"Pembangun\" (Y/N)?")
                        role_jin = data_user[i][2]
                        reverse_role_jin = "jin_pembangun"
                    else:
                        confirm = input(
                            "Jin ini bertipe \"Pembangun\". Yakin ingin mengubah ke tipe \"Pengumpul\" (Y/N)?")
                        role_jin = data_user[i][2]
                        reverse_role_jin = "jin_pembangun"
                    break

        if confirm == 'Y':
            for i in range(custom_len(data_user)):
                if data_user[i][0] == jin:
                    data_user[i][2] = reverse_role_jin
                    break
            print("Jin telah berhasil diubah.")
        else:
            print("Jin tidak diubah.")

    return data_user

# F08 - Batch Kumpul/Bangun

# F09 - Ambil Laporan Jin

# F10 - Ambil Laporan Candi (Akses : Bandung Bondowoso)

# F11 - Hancurkan Candi (Akses : Roro Jonggrang)

# F12 - Ayam Berkokok (Akses : Roro Jonggrang)
'''
def ayam_berkokok(jumlah_candi,nama):
    if nama == "Roro":
        print("Kukuruyuk.. Kukuruyuk..")
        print(f"Jumlah Candi: {jumlah_candi}")

        if jumlah_candi < 100:
            print("Selamat, Roro Jonggrang memenangkan permainan!")
            print("*Bandung Bondowoso angry noise*")
            print("Roro Jonggrang dikutuk menjadi candi.")
        else:
            print("Selamat, Bandung Bondowoso memenangkan permainan!")
            print("*Roro Jonggrang angry noise*")
            print("Bandung Bondowoso menikahi Roro Jonggrang.")
        exit()
    else:
        print("Anda tidak memiliki akses ini.")
    return None
'''

# F13 - Load

# F14 - Save

# F15 - Help
'''
def help(nama):
    print("=========== HELP ===========")
    if nama == '':
        print("1. login")
        print("   Untuk masuk menggunakan akun")
        print("2. exit")
        print("   Untuk keluar dari program dan kembali ke terminal")
    elif nama =="Bondowoso":
        print("1. logout")
        print("   Untuk keluar dari akun yang digunakan sekarang")
        print("2. summonjin")
        print("   Untuk memanggil jin")
        # print("3. ")
        # Jika ada, lanjutkan
    elif nama == "Roro":
        print("1. logout")
        print("   Untuk keluar dari akun yang digunakan sekarang")
        print("2. hancurkancandi")
        print("   Untuk menghancurkan candi yang tersedia")
        # print("3. ")
        # Jika ada, lanjutkan
    return None
'''

# F16 - Exit
'''
def exit():
    ask_simpan = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n)", end='')

    if ask_simpan != 'y' or ask_simpan != 'n':
        while True:
            ask_simpan = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n)", end='')
            if ask_simpan == 'y':
                save()
            exit()
    else:
        if ask_simpan == 'y':
            save()
        exit()
'''


