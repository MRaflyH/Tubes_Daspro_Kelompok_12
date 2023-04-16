def custom_len(array, max_array):
    for i in range(max_array):
        if array[i] is None:
            return i
    return max_array


def custom_append(array, elemen, max_array):
    array[custom_len(array, max_array)] = elemen
    return array


def custom_insert(elemen, array, max_array):
    for i in range(custom_len(array, max_array)-1, 0, -1):
        array[i] = array[i-1]
    array[0] = elemen
    return array


def custom_pop(array, index, max_array):
    for i in range(index, custom_len(array, max_array)-1):
        array[i] = array[i+1]
    array[custom_len(array, max_array)-1] = None
    return array


def custom_split(string_list, jumlah_elemen, pemisah=" "):
    data_list = [None for i in range(jumlah_elemen)]
    elemen_sementara = ""
    index = 0
    index_awal = 0
    index_akhir = -1
    while True:
        if string_list[index] == pemisah or string_list[index] == "\n":
            index_awal = index_akhir + 1
            index_akhir = index
            elemen_sementara = string_list[index_awal: index_akhir]
            data_list = custom_append(data_list, elemen_sementara, jumlah_elemen)
            if string_list[index] == "\n":
                return data_list
        index += 1


def csv_to_matriks(nama_file_csv, jumlah_elemen, max_data):
    data_matriks = [None for i in range(max_data)]
    file_user = open(nama_file_csv, 'r')
    file_user.readline()
    while True:
        string_baris_user = file_user.readline()
        if string_baris_user == "":
            break
        data_baris_user = custom_split(string_baris_user, jumlah_elemen, ";")
        data_matriks = custom_append(data_matriks, data_baris_user, max_data)
    file_user.close()
    return data_matriks


def cek_nama_terdaftar(nama, data_user, max_data_user):
    for i in range(custom_len(data_user, max_data_user)):
        if data_user[i][0] == nama:
            return True
    return False


def cek_password_cocok(password, nama, data_user, max_data_user):
    for i in range(custom_len(data_user, max_data_user)):
        if data_user[i][0] == nama:
            if password == data_user[i][1]:
                return True
            return False
    return False


def nama_to_role(nama, data_user, max_data_user):
    for i in range(custom_len(data_user, max_data_user)):
        if data_user[i][0] == nama:
            return data_user[i][2]
    return None


def daftar_jin(data_user, max_data_user):
    while True:
        nomor_jin = int(input("Masukkan nomor jenis jin yang ingin dipanggil: "))
        if nomor_jin != 1 and nomor_jin != 2:
            print(f'Tidak ada jenis jin bernomor "{nomor_jin}"')
        else:
            if nomor_jin == 1:  # Jin pengumpul
                print('Memilih jin “Pengumpul”.\n')
                jenis_jin = "jin_pengumpul"
            else:  # nomor_jin == 2; Jin pembangun
                print('Memilih jin "Pembangun”.\n')
                jenis_jin = "jin_pembangun"
            break

    while True:
        user_jin = input("Masukkan username jin: ")
        if cek_nama_terdaftar(user_jin, data_user, max_data_user):
            print(f"Username “{user_jin}” sudah diambil!")
        else:
            break

    while True:
        pass_jin = input("Masukkan password jin: ")
        if (len(pass_jin) < 5) or (len(pass_jin) > 25):
            print("Password panjangnya harus 5-25 karakter!\n")
        else:
            break

    return [user_jin, pass_jin, jenis_jin]


def hapus_candi_jin(jin, data_candi, max_data_candi):
    for i in range(custom_len(data_candi, max_data_candi) - 1, -1, -1):
        if data_candi[i][1] == jin:
            data_candi = custom_pop(data_candi, i, max_data_candi)
    return data_candi


def string_role_jin(jin, data_user, max_data_user):
    for i in range(custom_len(data_user, max_data_user)):
        if data_user[i][0] == jin:
            if data_user[i][2] == "jin_pengumpul":
                return "Pengumpul"
            else:
                return "Pembangun"


"""
def find_huruf_awal(data_user):
    for i in range(custom_len(data_user)):
        huruf = data_user[i][0]
    return huruf[0]
"""
# def pengumpul_terajin(data_user):


def hitung_candi(data_candi, max_data_candi):
    jumlah_candi = 0
    for i in range(custom_len(data_candi, max_data_candi)):
        if data_candi[i][1] is not None:
            jumlah_candi += 1
    return jumlah_candi


def leksikografis_lebih_rendah(nama_pertama, nama_kedua):
    kata_pertama_lebih_pendek = True
    length = len(nama_pertama)

    if len(nama_kedua) < len(nama_pertama):
        length = len(nama_kedua)
        kata_pertama_lebih_pendek = False

    for i in range(length):
        if ord(nama_pertama[i]) < ord(nama_kedua[i]):
            return True
        elif ord(nama_kedua[i]) < ord(nama_pertama[i]):
            return False

    return kata_pertama_lebih_pendek


def urutkan_leksikografis(data_jin, max_data_jin):
    for i in range(custom_len(data_jin, max_data_jin)-1):
        for j in range(i+1, custom_len(data_jin, max_data_jin)):
            if not leksikografis_lebih_rendah(data_jin[i], data_jin[j]):
                data_jin[i], data_jin[j] = data_jin[j], data_jin[i]
    return data_jin


def count_jin_total_pengumpul_pembangun(data_user, max_data_user):
    count_total_jin = 0
    count_total_jin_pengumpul = 0
    count_total_jin_pembangun = 0

    for i in range(custom_len(data_user, max_data_user)):
        if data_user[i][2] == "jin_pengumpul" or data_user[i][2] == "jin_pembangun":
            if data_user[i][2] == "jin_pengumpul":
                count_total_jin_pengumpul += 1
            elif data_user[i][2] == "jin_pembangun":
                count_total_jin_pembangun += 1
            count_total_jin += 1

    return count_total_jin, count_total_jin_pengumpul, count_total_jin_pembangun


def jin_terajin_termalas(data_jin, data_candi, max_data_jin, max_data_candi):
    jumlah_candi_dibangun = [None for i in range(max_data_jin)]

    for i in range(custom_len(data_jin, max_data_jin)):
        jumlah_candi_dibangun[i] = 0

    for i in range(custom_len(data_candi, max_data_candi)):
        for j in range(custom_len(data_jin, max_data_jin)):
            if data_candi[i][1] == data_jin[j]:
                jumlah_candi_dibangun[j] += 1

    index_jin_terajin = 0
    index_jin_termalas = 0
    for i in range(custom_len(jumlah_candi_dibangun, max_data_jin)):
        if jumlah_candi_dibangun[i] > jumlah_candi_dibangun[index_jin_terajin]:
            index_jin_terajin = i
        elif jumlah_candi_dibangun[i] < jumlah_candi_dibangun[index_jin_termalas]:
            index_jin_termalas = i

    jin_terajin = data_jin[index_jin_terajin]
    jin_termalas = data_jin[index_jin_termalas]

    return jin_terajin, jin_termalas


def jumlah_air_batu_pasir(data_bahan_bangunan, max_data_bahan_bangunan):
    jumlah_pasir = 0
    jumlah_air = 0
    jumlah_batu = 0

    for i in range(custom_len(data_bahan_bangunan, max_data_bahan_bangunan)):
        if data_bahan_bangunan[i][0] == "air":
            jumlah_air = data_bahan_bangunan[i][2]
        elif data_bahan_bangunan[i][0] == "batu":
            jumlah_batu = data_bahan_bangunan[i][2]
        elif data_bahan_bangunan[i][0] == "pasir":
            jumlah_pasir = data_bahan_bangunan[i][2]

    return jumlah_air, jumlah_batu, jumlah_pasir


def append_candi(nama, air, batu, pasir, data_candi, max_data_candi):
    data_kosong_ditemukan = False

    for i in range(custom_len(data_candi, max_data_candi)):
        if data_candi[i][1] is None:
            data_candi[i][1] = nama
            data_candi[i][2] = pasir
            data_candi[i][3] = batu
            data_candi[i][4] = air
            data_kosong_ditemukan = True
            break

    if not data_kosong_ditemukan:
        candi_baru = [custom_len(data_candi, max_data_candi)+1, nama, pasir, batu, air]
        data_candi = custom_append(data_candi, candi_baru, max_data_candi)

    return data_candi


def update_bahan(jumlah_air, jumlah_batu, jumlah_pasir, data_bahan_bangunan, max_data_bahan_bangunan):
    for i in range(custom_len(data_bahan_bangunan, max_data_bahan_bangunan)):
        if data_bahan_bangunan[i][0] == "air":
            data_bahan_bangunan[i][2] = jumlah_air
        elif data_bahan_bangunan[i][0] == "batu":
            data_bahan_bangunan[i][2] = jumlah_batu
        elif data_bahan_bangunan[i][0] == "pasir":
            data_bahan_bangunan[i][2] = jumlah_pasir
    return data_bahan_bangunan


def pakai_bahan(butuh_air, butuh_batu, butuh_pasir, data_bahan_bangunan, max_data_bahan_bangunan):
    jumlah_air, jumlah_batu, jumlah_pasir = jumlah_air_batu_pasir(data_bahan_bangunan, max_data_bahan_bangunan)
    jumlah_air -= butuh_air
    jumlah_batu -= butuh_batu
    jumlah_pasir -= butuh_pasir

    data_bahan_bangunan = update_bahan(jumlah_air, jumlah_batu, jumlah_pasir, data_bahan_bangunan, max_data_bahan_bangunan)

    return data_bahan_bangunan


def tambah_bahan(nemu_air, nemu_batu, nemu_pasir, data_bahan_bangunan, max_data_bahan_bangunan):
    jumlah_air, jumlah_batu, jumlah_pasir = jumlah_air_batu_pasir(data_bahan_bangunan, max_data_bahan_bangunan)
    jumlah_air += nemu_air
    jumlah_batu += nemu_batu
    jumlah_pasir += nemu_pasir

    data_bahan_bangunan = update_bahan(jumlah_air, jumlah_batu, jumlah_pasir, data_bahan_bangunan, max_data_bahan_bangunan)

    return data_bahan_bangunan
# test
