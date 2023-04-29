from custom_functions import *
from random import randint
from os import path, mkdir
from custom_functions import bcolors
import time

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
        print(f"{bcolors.fail}Login gagal!\nAnda telah login dengan username {nama}, silahkan lakukan “logout” sebelum melakukan login kembali.{bcolors.endc}")

    else:
        # input nama dan passwordd
        input_user = input(f"{bcolors.input}Username: {bcolors.endc}")
        input_password = input(f"{bcolors.input}Password: {bcolors.endc}")
        time.sleep(0.5)
        print()

        # cek jika nama terdaftar
        if not cek_nama_terdaftar(input_user, data_user, max_data_user):
            print(f"{bcolors.fail}Username tidak terdaftar!{bcolors.endc}")

        # cek jika password cocok
        elif not cek_password_cocok(input_password, input_user, data_user, max_data_user):
            print(f"{bcolors.fail}Password salah!{bcolors.endc}")

        # berhasil login
        else:
            print(f"Selamat datang, {input_user}!")
            print("Masukkan command \"help\" untuk daftar command yang dapat kamu panggil.")
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
        time.sleep(0.5)
        print(f"{bcolors.fail}Logout gagal!\nAnda belum login, silahkan login terlebih dahulu sebelum melakukan logout{bcolors.endc}")

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
    if role is None:
        print(f"{bcolors.warning}Anda belum login, silahkan login terlebih dahulu sebelum melakukan summonjin{bcolors.endc}")

    elif role != "bandung_bondowoso":
        print(f"{bcolors.warning}{nama} tidak memiliki akses untuk summon jin{bcolors.endc}")

    else:
        # pengecualian jika jumlah jin sudah 100
        if custom_len(data_user, max_data_user) == max_data_user:
            print(f"{bcolors.fail}Jumlah Jin telah maksimal! (100 jin). Bandung tidak dapat men-summon lebih dari itu{bcolors.endc}")

        else:
            print("Jenis jin yang dapat dipanggil:")
            time.sleep(0.5)
            print("  (1) Pengumpul - Bertugas mengumpulkan bahan bangunan")
            time.sleep(0.5)
            print("  (2) Pembangun - Bertugas membangun candi")
            time.sleep(0.5)
            print()

            # meminta tipe, nama, dan password jin
            data_jin = daftar_jin(data_user, max_data_user)

            print("Mengumpulkan sesajen...")
            time.sleep(1)
            print("Menyerahkan sesajen...")
            time.sleep(1)
            print("Membacakan mantra...")
            time.sleep(1)
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
    if role is None:
        print(f"{bcolors.warning}Anda belum login, silahkan login terlebih dahulu sebelum melakukan hilangkan jin{bcolors.endc}")

    elif role != "bandung_bondowoso":
        print(f"{bcolors.warning}{nama} tidak memiliki akses untuk hilangkan jin{bcolors.endc}")

    else:
        jin = input(f"{bcolors.input}Masukkan username jin: {bcolors.endc}")

        # cek jika ada nama jin tersebut
        if not cek_nama_terdaftar(jin, data_user, max_data_user):
            print()
            time.sleep(0.5)
            print(f"{bcolors.fail}Tidak ada jin dengan username tersebut.{bcolors.endc}")

        else:
            # konfirmasi
            confirm = ""
            while confirm.lower() != "y" and confirm.lower() != "n":
                confirm = input(f"{bcolors.input}Apakah anda yakin ingin menghapus jin dengan username {jin} (Y/N)? {bcolors.endc}")
            print()

            if confirm.lower() == 'y':
                # cari index jin dan menghapusnya dari data_user
                for i in range(custom_len(data_user, max_data_user)):
                    if data_user[i][0] == jin:
                        data_user = custom_pop(data_user, i, max_data_user)
                        break

                # menghapuskan candi yang dibuat jin tersebut
                data_candi = hapus_candi_jin(jin, data_candi, max_data_candi)

                time.sleep(0.5)
                print("Jin telah berhasil dihapus dari alam gaib.")

            else:
                time.sleep(0.5)
                print(f"{bcolors.fail}Jin tidak dihapus dari alam gaib.{bcolors.endc}")

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
    if role is None:
        print(f"{bcolors.warning}Anda belum login, silahkan login terlebih dahulu sebelum melakukan ubah tipe jin{bcolors.endc}")

    elif role != "bandung_bondowoso":
        print(f"{bcolors.warning}{nama} tidak memiliki akses untuk ubah tipe jin{bcolors.endc}")

    else:
        confirm = ""
        reverse_role_jin = ""
        jin = input(f"{bcolors.input}Masukkan username jin: {bcolors.endc}")

        # cek jika nama jin terdaftar
        if not cek_nama_terdaftar(jin, data_user, max_data_user):
            print()
            time.sleep(0.5)
            print(f"{bcolors.fail}Tidak ada jin dengan username tersebut.{bcolors.endc}")

        else:
            # mencari index jin pada data_user
            for i in range(custom_len(data_user, max_data_user)):
                if data_user[i][0] == jin:

                    # cek role jin dan konfirmasi
                    if data_user[i][2] == "jin_pengumpul":
                        while confirm.lower() != "y" and confirm.lower() != "n":
                            confirm = input(f"{bcolors.input}Jin ini bertipe \"Pengumpul\". Yakin ingin mengubah ke tipe \"Pembangun\" (Y/N)? {bcolors.endc}")
                        reverse_role_jin = "jin_pembangun"

                    else:
                        while confirm.lower() != "y" and confirm.lower() != "n":
                            confirm = input(f"{bcolors.input}Jin ini bertipe \"Pembangun\". Yakin ingin mengubah ke tipe \"Pengumpul\" (Y/N)? {bcolors.endc}")
                        reverse_role_jin = "jin_pengumpul"

                    break

            print()

            if confirm.lower() == 'y':
                # cek index jin dan mengganti rolenya
                for i in range(custom_len(data_user, max_data_user)):
                    if data_user[i][0] == jin:
                        data_user[i][2] = reverse_role_jin
                        break

                time.sleep(0.5)
                print("Jin telah berhasil diubah.")
            else:
                time.sleep(0.5)
                print(f"{bcolors.fail}Jin tidak berhasil diubah.{bcolors.endc}")

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
    if role is None:
        print(f"{bcolors.warning}Anda belum login, silahkan login terlebih dahulu sebelum melakukan bangun candi{bcolors.endc}")

    elif role != "jin_pembangun":
        print(f"{bcolors.warning}{nama} tidak memiliki akses untuk bangun candi{bcolors.endc}")

    else:
        # generate pasir batu dan air random
        butuh_pasir = randint(1, 5)
        butuh_batu = randint(1, 5)
        butuh_air = randint(1, 5)

        # menghitung jumlah air, batu, dan pasir
        jumlah_air, jumlah_batu, jumlah_pasir = jumlah_air_batu_pasir(data_bahan_bangunan, max_data_bahan_bangunan)

        # jika bahan cukup, membuat candi dan memakai bahan
        if jumlah_pasir >= butuh_pasir and jumlah_batu >= butuh_batu and jumlah_air >= butuh_air:
            data_candi = append_candi(nama, butuh_air, butuh_batu, butuh_pasir, data_candi, max_data_candi)
            data_bahan_bangunan = pakai_bahan(butuh_air, butuh_batu, butuh_pasir, data_bahan_bangunan,
                                              max_data_bahan_bangunan)

            # menghitung jumlah candi dan sisa candi
            jumlah_candi = hitung_candi(data_candi, max_data_candi)
            sisa_candi = 100 - jumlah_candi
            print("Candi berhasil dibangun.")
            time.sleep(0.5)
            print(f"Sisa candi yang perlu dibangun: {sisa_candi}")
            time.sleep(0.5)

        else:
            print(f"{bcolors.fail}Bahan bangunan tidak mencukupi.{bcolors.endc}")
            time.sleep(0.5)
            print(f"{bcolors.fail}Candi tidak bisa dibangun!{bcolors.endc}")
            time.sleep(0.5)

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

    if role is None:
        print(f"{bcolors.warning}Anda belum login, silahkan login terlebih dahulu sebelum melakukan kumpul bahan{bcolors.endc}")

    elif role != "jin_pengumpul":
        print(f"{bcolors.warning}{nama} tidak memiliki akses untuk kumpul bahan{bcolors.endc}")

    else:
        # generate pasir batu dan air random
        nemu_pasir = randint(1, 5)
        nemu_batu = randint(1, 5)
        nemu_air = randint(1, 5)

        # menambah bahan bangunan yang dikumpul
        data_bahan_bangunan = tambah_bahan(nemu_air, nemu_batu, nemu_pasir, data_bahan_bangunan,
                                           max_data_bahan_bangunan)

        print(f"Jin menemukan {nemu_pasir} pasir, {nemu_batu} batu, dan {nemu_air} air")
        time.sleep(0.5)

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
    count_total_jin, count_total_jin_pengumpul, jumlah_pengumpul_jin = count_jin_total_pengumpul_pembangun(data_user,
                                                                                                           max_data_user)

    if role is None:
        print(f"{bcolors.warning}Anda belum login, silahkan login terlebih dahulu sebelum melakukan batch kumpul{bcolors.endc}")

    elif role != "bandung_bondowoso":
        print(f"{bcolors.warning}{nama} tidak memiliki akses untuk batch kumpul{bcolors.endc}")

    elif jumlah_pengumpul_jin == 0:
        print(f"{bcolors.fail}Kumpul gagal. Anda tidak punya jin pengumpul. Silahkan summon terlebih dahulu.{bcolors.endc}")

    else:
        total_air = 0
        total_batu = 0
        total_pasir = 0

        for i in range(custom_len(data_user, max_data_user)):
            # untuk setip jin pengumpul
            if data_user[i][2] == "jin_pengumpul":
                # generate pasir batu dan air random
                nemu_pasir = randint(1, 5)
                nemu_batu = randint(1, 5)
                nemu_air = randint(1, 5)

                # menambah bahan bangunannya
                data_bahan_bangunan = tambah_bahan(nemu_air, nemu_batu, nemu_pasir, data_bahan_bangunan,
                                                   max_data_bahan_bangunan)

                total_air += nemu_air
                total_batu += nemu_batu
                total_pasir += nemu_pasir

        print(f"Mengerahkan {jumlah_pengumpul_jin} jin untuk mengumpulkan bahan.")
        time.sleep(0.5)
        print(f"Jin menemukan total {total_pasir} pasir, {total_batu} batu, dan {total_air} air.")
        time.sleep(0.5)

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
    count_total_jin, jumlah_pembangun_jin, count_total_jin_pembangun = count_jin_total_pengumpul_pembangun(data_user,
                                                                                                           max_data_user)

    if role is None:
        print(f"{bcolors.warning}Anda belum login, silahkan login terlebih dahulu sebelum melakukan batch bangun{bcolors.endc}")

    elif role != "bandung_bondowoso":
        print(f"{bcolors.warning}{nama} tidak memiliki akses untuk batch bangun{bcolors.endc}")

    elif jumlah_pembangun_jin == 0:
        print(f"{bcolors.fail}Bangun gagal. Anda tidak punya jin pembangun. Silahkan summon terlebih dahulu.{bcolors.endc}")

    else:
        total_air = 0
        total_batu = 0
        total_pasir = 0

        # membuat data sementara
        data_candi_sementara = [None for i in range(max_data_candi)]

        for i in range(custom_len(data_user, max_data_user)):
            # untuk setiap jin pembangun
            if data_user[i][2] == "jin_pembangun":
                # generate pasir batu air random
                butuh_pasir = randint(1, 5)
                butuh_batu = randint(1, 5)
                butuh_air = randint(1, 5)

                # bangun 1 candi dan memakai bahannya
                data_candi_sementara = append_candi(data_user[i][0], butuh_air, butuh_batu, butuh_pasir,
                                                    data_candi_sementara, max_data_candi)

                # menghitung keperluan total
                total_air += butuh_air
                total_batu += butuh_batu
                total_pasir += butuh_pasir

        print(f"Mengerahkan {jumlah_pembangun_jin} jin untuk membangun candi dengan total bahan {total_pasir} pasir, {total_batu} batu, dan {total_air} air.")
        time.sleep(0.5)

        jumlah_air, jumlah_batu, jumlah_pasir = jumlah_air_batu_pasir(data_bahan_bangunan, max_data_bahan_bangunan)

        if jumlah_pasir >= total_pasir and jumlah_batu >= total_batu and jumlah_air >= total_air:
            # membangun semua candi
            for i in range(jumlah_pembangun_jin):
                nama_jin = data_candi_sementara[i][1]
                butuh_pasir = data_candi_sementara[i][2]
                butuh_batu = data_candi_sementara[i][3]
                butuh_air = data_candi_sementara[i][4]

                data_candi = append_candi(nama_jin, butuh_air, butuh_batu, butuh_pasir, data_candi, max_data_candi)

            # pakai semua bahan
            data_bahan_bangunan = pakai_bahan(total_air, total_batu, total_pasir, data_bahan_bangunan,
                                              max_data_bahan_bangunan)

            print(f"Jin berhasil membangun total {jumlah_pembangun_jin} candi")

        else:
            # tidak jadi bangun candi dan pakai bahan serta menghitung kekurangan bahan
            kurang_air = total_air - jumlah_air
            kurang_batu = total_batu - jumlah_batu
            kurang_pasir = total_pasir - jumlah_pasir

            if kurang_air < 0:
                kurang_air = 0
            if kurang_batu < 0:
                kurang_batu = 0
            if kurang_pasir < 0:
                kurang_pasir = 0

            print(f"{bcolors.fail}Bangun gagal. Kurang {kurang_pasir} pasir, {kurang_batu} batu, dan {kurang_air} air.{bcolors.endc}")

        time.sleep(0.5)

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

    if role is None:
        print(f"{bcolors.warning}Anda belum login, silahkan login terlebih dahulu sebelum melakukan laporan jin{bcolors.endc}")

    elif role != "bandung_bondowoso":
        print(f"{bcolors.warning}Laporan jin hanya dapat diakses oleh akun Bandung Bondowoso.{bcolors.endc}")

    else:
        # membuat matriks nama semua jin
        max_data_jin = 100
        data_jin = [None for i in range(max_data_jin)]

        for i in range(custom_len(data_user, max_data_user) - 2):
            data_jin[i] = data_user[i + 2][0]

        # mengurut data jin sesuai leksikografis
        data_jin = urutkan_leksikografis(data_jin, max_data_jin)

        # menghitung semua jin
        total_jin, total_jin_pengumpul, total_jin_pembangun = count_jin_total_pengumpul_pembangun(data_user,
                                                                                                  max_data_user)

        # jika tidak ada candi dan tidak ada jin pembangun
        if hitung_candi(data_candi, max_data_candi) == 0 and total_jin_pembangun == 0:
            jin_terajin, jin_termalas = "-", "-"

        else:
            # mencari jin terajin dan termalas
            jin_terajin, jin_termalas = jin_terajin_termalas(data_jin, data_user, data_candi, max_data_jin,
                                                             max_data_user, max_data_candi)

        # menghitung stock air, batu, dan pasir
        jumlah_air, jumlah_batu, jumlah_pasir = jumlah_air_batu_pasir(data_bahan_bangunan, max_data_bahan_bangunan)

        print()
        print(f"{bcolors.header}============ LAPORAN JIN ============{bcolors.endc}")
        time.sleep(0.3)
        print(f"> Total Jin           : {total_jin}")
        time.sleep(0.3)
        print(f"> Total Jin Pengumpul : {total_jin_pengumpul}")
        time.sleep(0.3)
        print(f"> Total Jin Pembangun : {total_jin_pembangun}")
        time.sleep(0.3)
        print(f"> Jin Terajin         : {jin_terajin}")
        time.sleep(0.3)
        print(f"> Jin Termalas        : {jin_termalas}")
        time.sleep(0.3)
        print(f"> Jumlah Pasir        : {jumlah_pasir} unit")
        time.sleep(0.3)
        print(f"> Jumlah Air          : {jumlah_air} unit")
        time.sleep(0.3)
        print(f"> Jumlah Batu         : {jumlah_batu} unit")
        time.sleep(0.3)
        print(f"{bcolors.header}====================================={bcolors.endc}")
        time.sleep(0.3)


# F10 - Ambil Laporan Candi (Akses : Bandung Bondowoso)
def laporan_candi(role, data_candi, max_data_candi):
    """
    :param role:
    :param data_candi:
    :param max_data_candi:
    :return:
    """

    if role is None:
        print(f"{bcolors.warning}Anda belum login, silahkan login terlebih dahulu sebelum melakukan laporan candi{bcolors.endc}")

    elif role != "bandung_bondowoso":
        print(f"{bcolors.warning}Laporan candi hanya dapat diakses oleh akun Bandung Bondowoso.{bcolors.endc}")

    else:
        total_candi = 0
        total_pasir = 0
        total_batu = 0
        total_air = 0
        id_candi_termahal = 0
        harga_candi_termahal = 0
        id_candi_termurah = 0
        harga_candi_termurah = 10000 * 5 + 15000 * 5 + 7500 * 5

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
        print(f"{bcolors.header}=========== LAPORAN CANDI ==========={bcolors.endc}")
        time.sleep(0.3)
        print(f"Total Candi               : {total_candi}")
        time.sleep(0.3)
        print(f"Total Pasir yang digunakan: {total_pasir}")
        time.sleep(0.3)
        print(f"Total Batu yang digunakan : {total_batu}")
        time.sleep(0.3)
        print(f"Total Air yang digunakan  : {total_air}")
        time.sleep(0.3)

        if total_candi == 0:
            print("ID Candi Termahal         : -")
            time.sleep(0.3)
            print("ID Candi Termurah         : -")
            time.sleep(0.3)

        else:
            print(f"ID Candi Termahal         : {id_candi_termahal} (Rp {harga_candi_termahal})")
            time.sleep(0.3)
            print(f"ID Candi Termurah         : {id_candi_termurah} (Rp {harga_candi_termurah})")
            time.sleep(0.3)

        print(f"{bcolors.header}====================================={bcolors.endc}")
        time.sleep(0.3)


# F11 - Hancurkan Candi (Akses : Roro Jonggrang)
def hancurkan_candi(role, data_candi, max_data_candi):
    """
    data_candi
    :param role:
    :param data_candi:
    :param max_data_candi:
    :return:
    """

    if role is None:
        print(f"{bcolors.warning}Anda belum login, silahkan login terlebih dahulu sebelum melakukan hancurkan candi{bcolors.endc}")

    elif role != "roro_jonggrang":
        print(f"{bcolors.warning}Hancurkan candi hanya dapat diakses oleh akun Roro Jonggrang.{bcolors.endc}")

    else:
        id_candi = int(input(f"{bcolors.input}Masukkan ID candi: {bcolors.endc}"))
        candi_ditemukan = False

        # cari id candi
        for i in range(custom_len(data_candi, max_data_candi)):
            if data_candi[i][0] == id_candi:
                if data_candi[i][1] is not None:
                    candi_ditemukan = True
                    confirm = ""

                    # konfirmasi
                    while confirm.lower() != "y" and confirm.lower() != "n":
                        confirm = input(f"{bcolors.input}Apakah anda yakin ingin menghancurkan candi ID: {id_candi} (Y/N)? {bcolors.endc}")

                    print()
                    time.sleep(0.5)

                    if confirm.lower() == "y":
                        # hapus candi
                        data_candi = hapus_candi(i, data_candi)
                        print("Candi telah berhasil dihancurkan.")

                    else:
                        print(f"{bcolors.fail}Candi tidak berhasil dihancurkan.{bcolors.endc}")

                break

        if not candi_ditemukan:
            print()
            print(f"{bcolors.fail}Tidak ada candi dengan ID tersebut.{bcolors.endc}")

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

    if role is None:
        print(f"{bcolors.warning}Anda belum login, silahkan login terlebih dahulu sebelum melakukan ayam berkokok{bcolors.endc}")
        return False

    elif role == "roro_jonggrang":
        print("Kukuruyuk..", end=" ")
        time.sleep(1)
        print("Kukuruyuk..\n")
        time.sleep(1)
        print(f"Jumlah Candi: {jumlah_candi}\n")
        time.sleep(1)

        if jumlah_candi < 100:
            print("Selamat, Roro Jonggrang memenangkan permainan!\n")
            time.sleep(1)
            print(f"{bcolors.fail}*Bandung Bondowoso angry noise*{bcolors.endc}")
            time.sleep(1)
            print("Roro Jonggrang dikutuk menjadi candi.")
            time.sleep(1)

        else:
            print("Selamat, Bandung Bondowoso memenangkan permainan!\n")
            time.sleep(1)
            print(f"{bcolors.fail}*Roro Jonggrang angry noise*{bcolors.endc}")
            time.sleep(0.5)
            print("Bandung Bondowoso menikahi Roro Jonggrang.")
            time.sleep(0.5)

        return True

    else:
        print(f"{bcolors.warning}{nama} tidak memiliki akses ini.{bcolors.endc}")
        return False


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

    folder_name = input(f"{bcolors.input}Masukkan nama folder: {bcolors.endc}")
    print()
    print("Saving...\n")
    time.sleep(1)

    # membuat folder save jika belum ada folder save
    if not path.exists("save"):
        mkdir("save")
        print("Membuat folder save...")
        time.sleep(1)

    folder_path = "save/" + folder_name

    # membuat path folder jika belum ada path tersebut
    if not path.exists(folder_path):
        mkdir(folder_path)
        print(f"Membuat folder {folder_path}...")
        time.sleep(1)

    print()

    # write data user, candi, dan bahan bangunan dalam file masing-masing
    matriks_to_csv(folder_path, "user.csv", 3, data_user, max_data_user)
    matriks_to_csv(folder_path, "candi.csv", 5, data_candi, max_data_candi)
    matriks_to_csv(folder_path, "bahan_bangunan.csv", 3, data_bahan_bangunan, max_data_bahan_bangunan)

    print(f"Berhasil menyimpan data di folder {folder_path}!")
    time.sleep(1)


# F15 - Help
def help_role(role):
    """
    :param role:
    :return:
    """

    print(f"{bcolors.header}=============== HELP ================{bcolors.endc}")
    time.sleep(0.3)
    index_save = 0

    if role is None:
        print("1. login")
        print("   Untuk masuk menggunakan akun")
        time.sleep(0.3)
        index_save = 2

    else:
        print("1. logout")
        print("   Untuk keluar dari akun yang digunakan sekarang")
        time.sleep(0.3)

        if role == "bandung_bondowoso":
            print("2. summonjin")
            print("   Untuk memanggil jin")
            time.sleep(0.3)
            print("3. hapusjin")
            print("   Untuk menghapus jin")
            time.sleep(0.3)
            print("4. ubahjin")
            print("   Untuk mengubah tipe jin")
            time.sleep(0.3)
            print("5. batchkumpul")
            print("   Untuk mengerahkan seluruh pasukan jin pengumpul")
            time.sleep(0.3)
            print("6. batchkumpul")
            print("   Untuk mengerahkan seluruh pasukan jin pembangun")
            time.sleep(0.3)
            print("7. laporanjin")
            print("   Untuk mengambil laporan jin dan mengetahui kinerja dari para jin")
            time.sleep(0.3)
            print("8. laporancandi")
            print("   Untuk mengambil laporan candi dan mengetahui progress pembangunan candi")
            time.sleep(0.3)
            index_save = 9

        elif role == "roro_jonggrang":
            print("2. hancurkancandi")
            print("   Untuk menghancurkan candi yang tersedia")
            time.sleep(0.3)
            print("3. ayamberkokok")
            print("   Untuk menyelesaikan permainan dengan memalsukan pagi hari")
            time.sleep(0.3)
            index_save = 4

        elif role == "jin_pembangun":
            print("2. bangun")
            print("   Untuk membangun candi")
            time.sleep(0.3)
            index_save = 3

        elif role == "jin_pengumpul":
            print("2. kumpul")
            print("   Untuk mengumpul bahan bangunan")
            time.sleep(0.3)
            index_save = 3

    print(f"{index_save}. save")
    print("   Untuk simpan progres program")
    time.sleep(0.3)
    print(f"{index_save + 1}. exit")
    print("   Untuk keluar dari program dan kembali ke terminal")
    time.sleep(0.3)
    print(f"{bcolors.header}====================================={bcolors.endc}")
    time.sleep(0.3)


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
        confirm = input(f"{bcolors.input}Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) {bcolors.endc}")

    if confirm.lower() == 'y':
        save(data_user, data_candi, data_bahan_bangunan, max_data_user, max_data_candi, max_data_bahan_bangunan)

    return True
