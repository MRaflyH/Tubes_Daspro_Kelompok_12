from custom_functions import *
from random import randint

"""
JUDUL
"""


# F01 - Login
def login(nama, role, data_user, max_data_user):
    berhasil_login = False
    input_user = ""

    if role is not None:
        print(f"Login gagal!\nAnda telah login dengan username {nama}, silahkan lakukan “logout” sebelum melakukan "
              "login kembali.")
    else:
        input_user = input("Username: ")
        input_password = input("Password: ")

        if not cek_nama_terdaftar(input_user, data_user, max_data_user):
            print("Username tidak terdaftar!\n")
        elif not cek_password_cocok(input_password, input_user, data_user, max_data_user):
            print("Password salah!\n")
        else:
            print(f"Selamat datang, {input_user}!\n")
            print('Masukkan command "help" untuk daftar command yang dapat kamu panggil.\n')
            berhasil_login = True

    if berhasil_login:
        role = nama_to_role(input_user, data_user, max_data_user)
        return input_user, role
    else:
        return nama, role


# F02 - Logout
def logout(nama):
    if nama is None:
        print("Logout gagal!\nAnda belum login, silahkan login terlebih dahulu sebelum melakukan logout")
    return None, None


# F03 - Summon Jin
def summon_jin(nama, role, data_user, max_data_user):
    if role != "bandung_bondowoso":
        print(f"{nama} tidak memiliki akses untuk summon jin")
    else:
        print("Jenis jin yang dapat dipanggil:")
        print("  (1) Pengumpul - Bertugas mengumpulkan bahan bangunan")
        print("  (2) Pembangun - Bertugas membangun candi")

        data_jin = daftar_jin(data_user, max_data_user)

        print("Mengumpulkan sesajen...\nMenyerahkan sesajen...\nMembacakan mantra...\n")
        print(f"Jin {data_jin[0]} berhasil dipanggil!\n")

        data_user = custom_append(data_user, data_jin, max_data_user)

    return data_user


# F04 - Hilangkan Jin (Akses : Bandung Bondowoso)
def hilangkan_jin(nama, role, data_user, data_candi, max_data_user, max_data_candi):
    if role != "bandung_bondowoso":
        print(f"{nama} tidak memiliki akses untuk hilangkan jin")
    else:
        confirm = ""
        jin = input("Masukkan username jin: ")
        if not cek_nama_terdaftar(jin, data_user, max_data_user):
            print("Tidak ada jin dengan username tersebut.")
        else:
            confirm = input(f"Apakah anda yakin ingin menghapus jin dengan username {jin} (Y/N)? ")

        if confirm == 'Y' or confirm == 'y':
            for i in range(custom_len(data_user, max_data_user)):
                if data_user[i][0] == jin:
                    data_user = custom_pop(data_user, i, max_data_user)
                    break
            data_candi = hapus_candi_jin(jin, data_candi, max_data_candi)
            print("Jin telah berhasil dihapus dari alam gaib.")
        else:
            print("Jin tidak dihapus dari alam gaib.")

    return data_user, data_candi


# F05 - Ubah Tipe Jin
def ubah_tipe_jin(nama, role, data_user, max_data_user):
    if role != "bandung_bondowoso":
        print(f"{nama} tidak memiliki akses untuk ubah tipe jin")
    else:
        confirm = ""
        reverse_role_jin = ""
        jin = input("Masukkan username jin: ")

        if not cek_nama_terdaftar(jin, data_user, max_data_user):
            print("Tidak ada jin dengan username tersebut.")
        else:
            for i in range(custom_len(data_user, max_data_user)):
                if data_user[i][0] == jin:
                    if data_user[i][2] == "jin_pengumpul":
                        confirm = input(
                            "Jin ini bertipe \"Pengumpul\". Yakin ingin mengubah ke tipe \"Pembangun\" (Y/N)?")
                        reverse_role_jin = "jin_pembangun"
                    else:
                        confirm = input(
                            "Jin ini bertipe \"Pembangun\". Yakin ingin mengubah ke tipe \"Pengumpul\" (Y/N)?")
                        reverse_role_jin = "jin_pembangun"
                    break

        if confirm == 'Y' or confirm == 'y':
            for i in range(custom_len(data_user, max_data_user)):
                if data_user[i][0] == jin:
                    data_user[i][2] = reverse_role_jin
                    break
            print("Jin telah berhasil diubah.")
        else:
            print("Jin tidak diubah.")

    return data_user


# F06 - Jin Pembangun (Akses : Jin Pembangun)
def jin_pembangun(nama, role, data_candi, data_bahan_bangunan, max_data_candi, max_data_bahan_bangunan):
    if role != "jin_pembangun":
        print(f"{nama} tidak memiliki akses untuk bangun candi")
    else:
        butuh_pasir = randint(1, 5)
        butuh_batu = randint(1, 5)
        butuh_air = randint(1, 5)
        jumlah_air, jumlah_batu, jumlah_pasir = jumlah_air_batu_pasir(data_bahan_bangunan, max_data_bahan_bangunan)

        if jumlah_pasir >= butuh_pasir and jumlah_batu >= butuh_batu and jumlah_air >= butuh_air:
            data_candi = append_candi(nama, butuh_air, butuh_batu, butuh_pasir, data_candi, max_data_candi)
            jumlah_candi = hitung_candi(data_candi, max_data_candi)
            sisa_candi = 100 - jumlah_candi

            data_bahan_bangunan = pakai_bahan(butuh_air, butuh_batu, butuh_pasir, data_bahan_bangunan,
                                              max_data_bahan_bangunan)

            print("Candi berhasil dibangun.")
            print(f"Sisa candi yang perlu dibangun: {sisa_candi}")
        else:
            print("Bahan bangunan tidak mencukupi.")
            print("Candi tidak bisa dibangun!")

    return data_candi, data_bahan_bangunan


# F07 - Jin Pengumpul (Akses : Jin Pengumpul)
def jin_pengumpul(nama, role, data_bahan_bangunan, max_data_bahan_bangunan):
    if role != "jin_pengumpul":
        print(f"{nama} tidak memiliki akses untuk kumpul bahan")
    else:
        jumlah_air, jumlah_batu, jumlah_pasir = jumlah_air_batu_pasir(data_bahan_bangunan, max_data_bahan_bangunan)

        nemu_pasir = randint(1, 5)
        nemu_batu = randint(1, 5)
        nemu_air = randint(1, 5)

        jumlah_air += nemu_pasir
        jumlah_batu += nemu_batu
        jumlah_air += nemu_air

        data_bahan_bangunan = tambah_bahan(nemu_air, nemu_batu, nemu_pasir, data_bahan_bangunan,max_data_bahan_bangunan)

        print(f"Jin menemukan {nemu_pasir} pasir, {nemu_batu} batu, dan {nemu_air} air")

        return data_bahan_bangunan


# F08 - Batch Kumpul/Bangun

# F09 - Ambil Laporan Jin

def laporan_jin(nama, role, data_user, data_candi, data_bahan_bangunan, max_data_user, max_data_candi,
                max_data_bahan_bangunan):
    jumlah_candi_tiap_jin = [0 for i in range(custom_len(data_user, max_data_user))]

    if role != "bandung_bondowoso":
        print("Laporan jin hanya dapat diakses oleh akun Bandung Bondowoso.")
    else:
        max_data_jin = 100
        data_jin = [None for i in range(max_data_jin)]

        for i in range(custom_len(data_user, max_data_user) - 2):
            data_jin[i] = data_user[i + 2][0]

        data_jin = urutkan_leksikografis(data_jin, max_data_jin)

        total_jin, total_jin_pengumpul, total_jin_pembangun = count_jin_total_pengumpul_pembangun(data_user,
                                                                                                  max_data_user)
        jin_terajin, jin_termalas = jin_terajin_termalas(data_jin, data_candi, max_data_jin, max_data_candi)
        jumlah_air, jumlah_batu, jumlah_pasir = jumlah_air_batu_pasir(data_bahan_bangunan, max_data_bahan_bangunan)

        print(f"> Total Jin: {total_jin}")
        print(f"> Total Jin Pengumpul: {total_jin_pengumpul}")
        print(f"> Total Jin Pembangun: {total_jin_pembangun}")
        print(f"> Jin Terajin: {jin_terajin}")
        print(f"> Jin Termalas: {jin_termalas}")
        print(f"> Jumlah Pasir: {jumlah_pasir} unit")
        print(f"> Jumlah Air: {jumlah_air} unit")
        print(f"> Jumlah Batu: {jumlah_batu} unit")


# F10 - Ambil Laporan Candi (Akses : Bandung Bondowoso)

# F11 - Hancurkan Candi (Akses : Roro Jonggrang)

# F12 - Ayam Berkokok (Akses : Roro Jonggrang)
def ayam_berkokok(nama, role, data_candi, max_data_candi):
    jumlah_candi = hitung_candi(data_candi, max_data_candi)

    if role == "roro_jonggrang":
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
        return True

    else:
        print(f"{nama} tidak memiliki akses ini.")
        return False


# F13 - Load

# F14 - Save

# F15 - Help
def help_role(role):
    print("=========== HELP ===========")
    if role is None:
        print("1. login")
        print("   Untuk masuk menggunakan akun")
        print("2. exit")
        print("   Untuk keluar dari program dan kembali ke terminal")
    elif role == "bandung_bondowoso":
        print("1. logout")
        print("   Untuk keluar dari akun yang digunakan sekarang")
        print("2. summonjin")
        print("   Untuk memanggil jin")
        # print("3. ")
        # Jika ada, lanjutkan
    elif role == "roro_jonggrang":
        print("3. hapusjin")
        print("   Untuk menghapus jin")
        print("4. ubahjin")
        print("   Untuk mengubah tipe jin")
        print("5. batchkumpul")
        print("   Untuk mengerahkan seluruh pasukan jin")
        print("6. laporanjin")
        print("   Untuk mengambil laporan jin dan mengetahui kinerja dari para jin")
        print("7. laporancandi")
        print("   Untuk mengambil laporan candi dan mengetahui progress pembangunan candi")
        print("8. laporancandi")
        print("   Untuk mengambil laporan candi dan mengetahui progress pembangunan candi")
        print("9. exit")
        print("   Untuk keluar dari program dan kembali ke terminal")


# F16 - Exit

def exit_game():
    while True:
        confirm = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")
        if confirm == 'y':
            print("jalanin save()")
            # save() belum ada
            break
        elif confirm == 'n':
            print("tidak jalanin save()")
            break
    return True
