from custom_functions import cek_user_terdaftar, cek_password_cocok, daftar_jin, custom_append_array
"""

"""


def Login(nama, data_user):
    berhasil_login = False
    input_user = input("Username: ")
    input_password = input("Password: ")
    if nama != "":
        print(f"Login gagal!\nAnda telah login dengan username {nama}, silahkan lakukan “logout” sebelum melakukan "
              "login kembali.")
    else:
        if not cek_user_terdaftar(input_user, data_user):
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


def Logout(nama):
    if nama == "":
        print("Logout gagal!\nAnda belum login, silahkan login terlebih dahulu sebelum melakukan logout")
    return ""


def SummonJin(nama, data_user):
    if nama != "Bondowoso":
        print(f"Anda tidak memiliki akses untuk summonjin")
    else:
        print("Jenis jin yang dapat dipanggil:")
        print("  (1) Pengumpul - Bertugas mengumpulkan bahan bangunan")
        print("  (2) Pembangun - Bertugas membangun candi")

        data_jin = daftar_jin(data_user)

        print("Mengumpulkan sesajen...\nMenyerahkan sesajen...\nMembacakan mantra...\n")
        print(f"Jin {data_jin[0]} berhasil dipanggil!\n")

        data_user = custom_append_array(data_user, data_jin)

    return data_user

