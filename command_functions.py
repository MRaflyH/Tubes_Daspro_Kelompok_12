from custom_functions import *
from random import randint
from os import path, mkdir

"""
JUDUL
"""


# F01 - Login
def login(nama, role, data_user, max_data_user):
    """
    :param nama:
    :param role:
    :param data_user:
    :param max_data_user:
    :return: nama, role
    """

    berhasil_login = False
    input_user = ""

    # memastikan akses sesuai
    if role is not None:
        print(f"Login gagal!\nAnda telah login dengan username {nama}, silahkan lakukan “logout” sebelum melakukan "
              "login kembali.")

    else:
        # input nama dan passwordd
        input_user = input("Username: ")
        input_password = input("Password: ")
        print()

        # cek jika nama terdaftar
        if not cek_nama_terdaftar(input_user, data_user, max_data_user):
            print("Username tidak terdaftar!")

        # cek jika password cocok
        elif not cek_password_cocok(input_password, input_user, data_user, max_data_user):
            print("Password salah!")

        # berhasil login
        else:
            print(f"Selamat datang, {input_user}!")
            print('Masukkan command "help" untuk daftar command yang dapat kamu panggil.')
            berhasil_login = True

    # return nama dan role sesuai login
    if berhasil_login:
        role = nama_to_role(input_user, data_user, max_data_user)
        return input_user, role

    else:
        return nama, role


# F02 - Logout
def logout(nama):
    """
    :param nama:
    :return: nama, role
    """

    # cek jika sudah login
    if nama is None:
        print("Logout gagal!\nAnda belum login, silahkan login terlebih dahulu sebelum melakukan logout")

    return None, None


# F03 - Summon Jin (Akses : Bandung Bondowoso)
def summon_jin(nama, role, data_user, max_data_user):
    """
    :param nama:
    :param role:
    :param data_user:
    :param max_data_user:
    :return: data_user
    """
    # memastikan akses sesuai
    if role != "bandung_bondowoso":
        print(f"{nama} tidak memiliki akses untuk summon jin")

    else:
        # pengecualian jika jumlah jin sudah 100
        if custom_len(data_user, max_data_user) == max_data_user:
            print("Jumlah Jin telah maksimal! (100 jin). Bandung tidak dapat men-summon lebih dari itu")

        else:
            print("Jenis jin yang dapat dipanggil:")
            print("  (1) Pengumpul - Bertugas mengumpulkan bahan bangunan")
            print("  (2) Pembangun - Bertugas membangun candi")
            print()

            # meminta tipe, nama, dan password jin
            data_jin = daftar_jin(data_user, max_data_user)

            print("Mengumpulkan sesajen...\nMenyerahkan sesajen...\nMembacakan mantra...")
            print()
            print(f"Jin {data_jin[0]} berhasil dipanggil!")

            # update data_user dengan jin baru
            data_user = custom_append(data_user, data_jin, max_data_user)

    return data_user


# F04 - Hilangkan Jin (Akses : Bandung Bondowoso)
def hilangkan_jin(nama, role, data_user, data_candi, max_data_user, max_data_candi):
    """
    :param nama:
    :param role:
    :param data_user:
    :param data_candi:
    :param max_data_user:
    :param max_data_candi:
    :return: data_user, data_candi
    """

    # memastikan akses sesuai
    if role != "bandung_bondowoso":
        print(f"{nama} tidak memiliki akses untuk hilangkan jin")

    else:
        jin = input("Masukkan username jin: ")

        # cek jika ada nama jin tersebut
        if not cek_nama_terdaftar(jin, data_user, max_data_user):
            print()
            print("Tidak ada jin dengan username tersebut.")

        else:
            # konfirmasi
            confirm = ""
            while confirm.lower() != "y" and confirm.lower() != "n":
                confirm = input(f"Apakah anda yakin ingin menghapus jin dengan username {jin} (Y/N)? ")
            print()

            if confirm.lower() == 'y':
                # cari index jin dan menghapusnya dari data_user
                for i in range(custom_len(data_user, max_data_user)):
                    if data_user[i][0] == jin:
                        data_user = custom_pop(data_user, i, max_data_user)
                        break

                # menghapuskan candi yang dibuat jin tersebut
                data_candi = hapus_candi_jin(jin, data_candi, max_data_candi)

                print("Jin telah berhasil dihapus dari alam gaib.")

            else:
                print("Jin tidak dihapus dari alam gaib.")

    return data_user, data_candi


# F05 - Ubah Tipe Jin (Akses : Bandung Bondowoso)
def ubah_tipe_jin(nama, role, data_user, max_data_user):
    """
    :param nama:
    :param role:
    :param data_user:
    :param max_data_user:
    :return: data_user
    """

    # memastikan akses sesuai
    if role != "bandung_bondowoso":
        print(f"{nama} tidak memiliki akses untuk ubah tipe jin")

    else:
        confirm = ""
        reverse_role_jin = ""
        jin = input("Masukkan username jin: ")

        # cek jika nama jin terdaftar
        if not cek_nama_terdaftar(jin, data_user, max_data_user):
            print()
            print("Tidak ada jin dengan username tersebut.")

        else:
            # mencari index jin pada data_user
            for i in range(custom_len(data_user, max_data_user)):
                if data_user[i][0] == jin:

                    # cek role jin dan konfirmasi
                    if data_user[i][2] == "jin_pengumpul":
                        while confirm.lower() != "y" and confirm.lower() != "n":
                            confirm = input(
                                "Jin ini bertipe \"Pengumpul\". Yakin ingin mengubah ke tipe \"Pembangun\" (Y/N)? ")
                        reverse_role_jin = "jin_pembangun"

                    else:
                        while confirm.lower() != "y" and confirm.lower() != "n":
                            confirm = input(
                                "Jin ini bertipe \"Pembangun\". Yakin ingin mengubah ke tipe \"Pengumpul\" (Y/N)? ")
                        reverse_role_jin = "jin_pengumpul"

                    break

            print()

            if confirm.lower() == 'y':
                # cek index jin dan mengganti rolenya
                for i in range(custom_len(data_user, max_data_user)):
                    if data_user[i][0] == jin:
                        data_user[i][2] = reverse_role_jin
                        break
                print("Jin telah berhasil diubah.")
            else:
                print("Jin tidak berhasil diubah.")

    return data_user


# F06 - Jin Pembangun (Akses : Jin Pembangun)
def bangun(nama, role, data_candi, data_bahan_bangunan, max_data_candi, max_data_bahan_bangunan):
    """
    :param nama:
    :param role:
    :param data_candi:
    :param data_bahan_bangunan:
    :param max_data_candi:
    :param max_data_bahan_bangunan:
    :return: data_candi, data_bahan_bangunan
    """

    # memastikan akses sesuai
    if role != "jin_pembangun":
        print(f"{nama} tidak memiliki akses untuk bangun candi")

    else:
        # generate pasir batu dan air random
        butuh_pasir = randint(1, 5)
        butuh_batu = randint(1, 5)
        butuh_air = randint(1, 5)

        # menambah 1 candi dan memakai bahan bangunannya
        data_candi, data_bahan_bangunan, berhasil_dibangun = bangun_tunggal(nama, butuh_pasir, butuh_batu, butuh_air, data_candi, data_bahan_bangunan, max_data_candi, max_data_bahan_bangunan)

        if berhasil_dibangun:
            jumlah_candi = hitung_candi(data_candi, max_data_candi)
            sisa_candi = 100 - jumlah_candi
            print("Candi berhasil dibangun.")
            print(f"Sisa candi yang perlu dibangun: {sisa_candi}")

        else:
            print("Bahan bangunan tidak mencukupi.")
            print("Candi tidak bisa dibangun!")

    return data_candi, data_bahan_bangunan


# F07 - Jin Pengumpul (Akses : Jin Pengumpul)
def kumpul(nama, role, data_bahan_bangunan, max_data_bahan_bangunan):
    """
    :param nama:
    :param role:
    :param data_bahan_bangunan:
    :param max_data_bahan_bangunan:
    :return: data_bahan_bangunan
    """

    if role != "jin_pengumpul":
        print(f"{nama} tidak memiliki akses untuk kumpul bahan")

    else:
        # generate pasir batu dan air random
        nemu_pasir = randint(1, 5)
        nemu_batu = randint(1, 5)
        nemu_air = randint(1, 5)

        # menambah bahan bangunan yang dikumpul
        data_bahan_bangunan = tambah_bahan(nemu_air, nemu_batu, nemu_pasir, data_bahan_bangunan, max_data_bahan_bangunan)

        print(f"Jin menemukan {nemu_pasir} pasir, {nemu_batu} batu, dan {nemu_air} air")

    return data_bahan_bangunan


# F08 - Batch Kumpul/Bangun (Akses : Bandung Bondowoso)
def batch_kumpul(nama, role, data_user, max_data_user, data_bahan_bangunan, max_data_bahan_bangunan):
    """
    :param nama:
    :param role:
    :param data_user:
    :param max_data_user:
    :param data_bahan_bangunan:
    :param max_data_bahan_bangunan:
    :return: data_bahan_bangunan
    """

    if role != "bandung_bondowoso":
        print(f"{nama} tidak memiliki akses untuk batch kumpul")

    else:
        jumlah_pembangun_jin = 0
        total_air = 0
        total_batu = 0
        total_pasir = 0

        for i in range(custom_len(data_user, max_data_user)):
            # untuk setip jin pengumpul
            if data_user[i][2] == "jin_pengumpul":
                jumlah_pembangun_jin += 1

                # generate pasir batu dan air random
                nemu_pasir = randint(1, 5)
                nemu_batu = randint(1, 5)
                nemu_air = randint(1, 5)

                # menambah bahan bangunannya
                data_bahan_bangunan = tambah_bahan(nemu_air, nemu_batu, nemu_pasir, data_bahan_bangunan, max_data_bahan_bangunan)

                total_air += nemu_air
                total_batu += nemu_batu
                total_pasir += nemu_pasir

        print(f'Mengerahkan {jumlah_pembangun_jin} jin untuk mengumpulkan bahan.')
        print(f'Jin menemukan total {total_pasir} pasir, {total_batu} batu, dan {total_air} air.')

    return data_bahan_bangunan


def batch_bangun(nama, role, data_user, data_candi, data_bahan_bangunan, max_data_user, max_data_candi,
                 max_data_bahan_bangunan):
    """
    :param nama:
    :param role:
    :param data_user:
    :param data_candi:
    :param data_bahan_bangunan:
    :param max_data_user:
    :param max_data_candi:
    :param max_data_bahan_bangunan:
    :return: data_candi, data_bahan_bangunan
    """

    batch_bangun_berhasil = True

    if role != "bandung_bondowoso":
        print(f"{nama} tidak memiliki akses untuk batch bangun")

    else:
        jumlah_pembangun_jin = 0
        total_air = 0
        total_batu = 0
        total_pasir = 0

        # membuat data sementara
        data_candi_sementara = copy_matriks(data_candi, max_data_candi)
        data_bahan_bangunan_sementara = copy_matriks(data_bahan_bangunan, max_data_bahan_bangunan)

        for i in range(custom_len(data_user, max_data_user)):
            # untuk setiap jin pembangun
            if data_user[i][2] == "jin_pembangun":

                # generate pasir batu air random
                jumlah_pembangun_jin += 1
                butuh_pasir = randint(1, 5)
                butuh_batu = randint(1, 5)
                butuh_air = randint(1, 5)

                # bangun 1 candi dan memakai bahannya
                data_candi_sementara, data_bahan_bangunan_sementara, berhasil_dibangun = bangun_tunggal(data_user[i][0], butuh_pasir, butuh_batu, butuh_air, data_candi_sementara, data_bahan_bangunan_sementara, max_data_candi, max_data_bahan_bangunan)

                # print(data_bahan_bangunan)
                # print(data_bahan_bangunan_sementara)
                # print(data_candi)
                # print(data_candi_sementara)

                total_air += butuh_air
                total_batu += butuh_batu
                total_pasir += butuh_pasir

                if not berhasil_dibangun:
                    batch_bangun_berhasil = False

                # print(21, data_candi)
                # print(22, data_candi_sementara)

        print(f"Mengerahkan {jumlah_pembangun_jin} jin untuk membangun candi dengan total bahan {total_pasir} pasir, {total_batu} batu, dan {total_air} air.")

        if batch_bangun_berhasil:
            # membangun semua candi dan pakai semua bahan
            data_candi = copy_matriks(data_candi_sementara, max_data_candi)
            data_bahan_bangunan = copy_matriks(data_bahan_bangunan_sementara, max_data_bahan_bangunan)

            print(f"Jin berhasil membangun total {jumlah_pembangun_jin} candi")

        else:
            # tidak jadi bangun candi dan pakai bahan serta menghitung kekurangan bahan
            jumlah_air, jumlah_batu, jumlah_pasir = jumlah_air_batu_pasir(data_bahan_bangunan, max_data_bahan_bangunan)
            kurang_air = total_air - jumlah_air
            kurang_batu = total_batu - jumlah_batu
            kurang_pasir = total_pasir - jumlah_pasir

            print(f"Bangun gagal. Kurang {kurang_pasir} pasir, {kurang_batu} batu, dan {kurang_air} air.")

    return data_candi, data_bahan_bangunan


# F09 - Ambil Laporan Jin (Akses : Bandung Bondowoso)
def laporan_jin(role, data_user, data_candi, data_bahan_bangunan, max_data_user, max_data_candi,
                max_data_bahan_bangunan):
    """
    :param role:
    :param data_user:
    :param data_candi:
    :param data_bahan_bangunan:
    :param max_data_user:
    :param max_data_candi:
    :param max_data_bahan_bangunan:
    :return:
    """

    if role != "bandung_bondowoso":
        print("Laporan jin hanya dapat diakses oleh akun Bandung Bondowoso.")

    else:
        # membuat matriks nama semua jin
        max_data_jin = 100
        data_jin = [None for i in range(max_data_jin)]

        for i in range(custom_len(data_user, max_data_user) - 2):
            data_jin[i] = data_user[i + 2][0]

        # mengurut data jin sesuai leksikografis
        data_jin = urutkan_leksikografis(data_jin, max_data_jin)
        print(data_jin)

        # menghitung semua jin
        total_jin, total_jin_pengumpul, total_jin_pembangun = count_jin_total_pengumpul_pembangun(data_user,
                                                                                                  max_data_user)

        # jika tidak ada candi dan tidak ada jin pembangun
        if hitung_candi(data_candi, max_data_candi) == 0 and total_jin_pembangun == 0:
            jin_terajin, jin_termalas = "-", "-"

        else:
            # mencari jin terajin dan termalas
            jin_terajin, jin_termalas = jin_terajin_termalas(data_jin, data_user, data_candi, max_data_jin, max_data_user, max_data_candi)

        # menghitung stock air, batu, dan pasir
        jumlah_air, jumlah_batu, jumlah_pasir = jumlah_air_batu_pasir(data_bahan_bangunan, max_data_bahan_bangunan)

        print()
        print(f"> Total Jin: {total_jin}")
        print(f"> Total Jin Pengumpul: {total_jin_pengumpul}")
        print(f"> Total Jin Pembangun: {total_jin_pembangun}")
        print(f"> Jin Terajin: {jin_terajin}")
        print(f"> Jin Termalas: {jin_termalas}")
        print(f"> Jumlah Pasir: {jumlah_pasir} unit")
        print(f"> Jumlah Air: {jumlah_air} unit")
        print(f"> Jumlah Batu: {jumlah_batu} unit")


# F10 - Ambil Laporan Candi (Akses : Bandung Bondowoso)
def laporan_candi(role, data_candi, max_data_candi):
    """
    :param role:
    :param data_candi:
    :param max_data_candi:
    :return:
    """

    if role != "bandung_bondowoso":
        print("Laporan candi hanya dapat diakses oleh akun Bandung Bondowoso.")

    else:
        total_candi = 0
        total_pasir = 0
        total_batu = 0
        total_air = 0
        id_candi_termahal = 0
        harga_candi_termahal = 0
        id_candi_termurah = 0
        harga_candi_termurah = 0

        # cek semua candi
        for i in range(custom_len(data_candi, max_data_candi)):
            # jika id candi tidak kosong
            if data_candi[i][1] is not None:
                pasir = data_candi[i][2]
                batu = data_candi[i][3]
                air = data_candi[i][4]

                total_pasir += pasir
                total_batu += batu
                total_air += air
                total_candi += 1

                harga_candi = 10000 * pasir + 15000 * batu + 7500 * air

                # cek jika harga candi lebih murah atau lebih mahal serta mencari termurah dan termahal
                if harga_candi > harga_candi_termahal:
                    id_candi_termahal = data_candi[i][0]
                    harga_candi_termahal = harga_candi
                if harga_candi < harga_candi_termurah:
                    id_candi_termurah = data_candi[i][0]
                    harga_candi_termurah = harga_candi

        print()
        print(f"Total Candi: {total_candi}")
        print(f"Total Pasir yang digunakan: {total_pasir}")
        print(f"Total Batu yang digunakan: {total_batu}")
        print(f"Total Air yang digunakan: {total_air}")

        if total_candi == 0:
            print("ID Candi Termahal: -")
            print("ID Candi Termurah: -")
        else:
            print(f"ID Candi Termahal: {id_candi_termahal} (Rp {harga_candi_termahal})")
            print(f"ID Candi Termurah: {id_candi_termurah} (Rp {harga_candi_termurah})")


# F11 - Hancurkan Candi (Akses : Roro Jonggrang)
def hancurkan_candi(role, data_candi, max_data_candi):
    """
    data_candi
    :param role:
    :param data_candi:
    :param max_data_candi:
    :return:
    """

    if role != "roro_jonggrang":
        print("Hancurkan candi hanya dapat diakses oleh akun Roro Jonggrang.")

    else:
        id_candi = int(input("Masukkan ID candi: "))
        candi_ditemukan = False

        # cari id candi
        for i in range(custom_len(data_candi, max_data_candi)):
            if data_candi[i][0] == id_candi:
                if data_candi[i][1] is not None:
                    candi_ditemukan = True
                    confirm = ""

                    # konfirmasi
                    while confirm.lower() != "y" and confirm.lower() != "n":
                        confirm = input("Apakah anda yakin ingin menghancurkan candi ID: 5 (Y/N)? ")

                    print()

                    if confirm.lower() == "y":
                        # hapus candi
                        data_candi = hapus_candi(i, data_candi)
                        print("Candi telah berhasil dihancurkan.")

                    else:
                        print("Candi tidak berhasil dihancurkan.")

                break

        if not candi_ditemukan:
            print()
            print("Tidak ada candi dengan ID tersebut.")

    return data_candi


# F12 - Ayam Berkokok (Akses : Roro Jonggrang)
def ayam_berkokok(nama, role, data_candi, max_data_candi):
    """
    :param nama:
    :param role:
    :param data_candi:
    :param max_data_candi:
    :return: end
    """

    jumlah_candi = hitung_candi(data_candi, max_data_candi)

    if role == "roro_jonggrang":
        print("Kukuruyuk.. Kukuruyuk..")
        print()
        print(f"Jumlah Candi: {jumlah_candi}")
        print()

        if jumlah_candi < 100:
            print("Selamat, Roro Jonggrang memenangkan permainan!")
            print()
            print("*Bandung Bondowoso angry noise*")
            print("Roro Jonggrang dikutuk menjadi candi.")

        else:
            print("Selamat, Bandung Bondowoso memenangkan permainan!")
            print()
            print("*Roro Jonggrang angry noise*")
            print("Bandung Bondowoso menikahi Roro Jonggrang.")

        return True

    else:
        print(f"{nama} tidak memiliki akses ini.")
        return False


# F13 - Load

# F14 - Save
def save(data_user, data_candi, data_bahan_bangunan, max_data_user, max_data_candi, max_data_bahan_bangunan):
    """
    :param data_user:
    :param data_candi:
    :param data_bahan_bangunan:
    :param max_data_user:
    :param max_data_candi:
    :param max_data_bahan_bangunan:
    :return:
    """

    folder_name = input("Masukkan nama folder: ")
    print()
    print("Saving...")
    print()

    # membuat folder save jika belum ada folder save
    if not path.exists("save"):
        mkdir("save")
        print("Membuat folder save...")

    folder_path = "save/" + folder_name

    # membuat path folder jika belum ada path tersebut
    if not path.exists(folder_path):
        mkdir(folder_path)
        print(f"Membuat folder {folder_path}...")

    print()

    # write data user, candi, dan bahan bangunan dalam file masing-masing
    matriks_to_csv(folder_path, "user.csv", 3, data_user, max_data_user)
    matriks_to_csv(folder_path, "candi.csv", 5, data_candi, max_data_candi)
    matriks_to_csv(folder_path, "bahan_bangunan.csv", 3, data_bahan_bangunan, max_data_bahan_bangunan)

    print(f"Berhasil menyimpan data di folder {folder_path}!")


# F15 - Help
def help_role(role):
    """
    :param role:
    :return:
    """

    print("=========== HELP ===========")
    index_save = 0

    if role is None:
        print("1. login")
        print("   Untuk masuk menggunakan akun")
        index_save = 2

    else:
        print("1. logout")
        print("   Untuk keluar dari akun yang digunakan sekarang")

        if role == "bandung_bondowoso":
            print("2. summonjin")
            print("   Untuk memanggil jin")
            print("3. hapusjin")
            print("   Untuk menghapus jin")
            print("4. ubahjin")
            print("   Untuk mengubah tipe jin")
            print("5. batchkumpul")
            print("   Untuk mengerahkan seluruh pasukan jin pengumpul")
            print("6. batchkumpul")
            print("   Untuk mengerahkan seluruh pasukan jin pembangun")
            print("7. laporanjin")
            print("   Untuk mengambil laporan jin dan mengetahui kinerja dari para jin")
            print("8. laporancandi")
            print("   Untuk mengambil laporan candi dan mengetahui progress pembangunan candi")
            index_save = 9

        elif role == "roro_jonggrang":
            print("2. hancurkancandi")
            print("   Untuk menghancurkan candi yang tersedia")
            print("3. ayamberkokok")
            print("   Untuk menyelesaikan permainan dengan memalsukan pagi hari")
            index_save = 4

        elif role == "jin_pembangun":
            print("2. bangun")
            print("   Untuk membangun candi")
            index_save = 3

        elif role == "jin_pengumpul":
            print("2. kumpul")
            print("   Untuk mengumpul bahan bangunan")
            index_save = 3

    print(f"{index_save}. save")
    print("   Untuk simpan progres program")
    print(f"{index_save+1}. exit")
    print("   Untuk keluar dari program dan kembali ke terminal")


# F16 - Exit
def exit_game(data_user, data_candi, data_bahan_bangunan, max_data_user, max_data_candi, max_data_bahan_bangunan):
    """
    :param data_user:
    :param data_candi:
    :param data_bahan_bangunan:
    :param max_data_user:
    :param max_data_candi:
    :param max_data_bahan_bangunan:
    :return: end
    """

    confirm = ""

    # konfirmasi save
    while confirm.lower() != "y" and confirm.lower() != "n":
        confirm = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")

    if confirm.lower() == 'y':
        save(data_user, data_candi, data_bahan_bangunan, max_data_user, max_data_candi, max_data_bahan_bangunan)

    return True

# B04 - Undo
def undo(data_sejarah, max_sejarah):
    """
    :param data_sejarah:
    :param max_sejarah:
    :return: nama, role, end, data_user, data_candi, data_bahan_bangunan, sejarah
    """

    if custom_len(data_sejarah, max_sejarah) == 1:
        print("Undo gagal karena tidak ada sejarah")

    else:
        data_sejarah = custom_pop(data_sejarah, 0, max_sejarah)
        print("Undo berhasil")

    nama = data_sejarah[0][0]
    role = data_sejarah[0][1]
    data_user = data_sejarah[0][2]
    data_candi = data_sejarah[0][3]
    data_bahan_bangunan = data_sejarah[0][4]

    return nama, role, data_user, data_candi, data_bahan_bangunan, data_sejarah