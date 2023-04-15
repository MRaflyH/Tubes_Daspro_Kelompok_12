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


def find_huruf_awal(data_user):
    for i in range(custom_len(data_user)):
        huruf = data_user[i][0]
    return huruf[0]

# def pengumpul_terajin(data_user):


def hitung_candi(data_candi, max_data_candi):
    jumlah_candi = 0
    for i in range(custom_len(data_candi, max_data_candi)):
        if data_candi[i][1] is not None:
            jumlah_candi += 1
    return jumlah_candi

