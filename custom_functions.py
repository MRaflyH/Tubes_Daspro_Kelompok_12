"""
Fungsi-Fungsi Mengsimulasikan Fungsi yang Diban dan Fungsi Selain Fungsi Utama
"""

"""
Persis kayak len()
>>> custom_len_list([1, 2, 3, 4])
4
Digunakan untuk list dan array saja, tuple dan string tidak bisa
"""


def custom_len(array):
    count = 0
 
    for i in array:
        count += 1
    return count


"""
Mengembalikan persis kayak append() atau konso di Haskell tapi parameter elemen ga boleh kosong, atau ga hasilnya
[e1, e2, e3, ]
>>> array = custom_append_list([1, 2, 3]], 4)
>>> print(array)
[1, 2, 3, 4]
"""

def custom_append(array, elemen):
    array_baru = [None for i in range(custom_len(array) + 1)]
    for i in range(custom_len(array)):
        array_baru[i] = array[i]
    array_baru[custom_len(array)] = elemen
    return array_baru


"""
Mengembalikan persis kayak insert() atau konsdot di Haskell tapi parameter elemen ga boleh kosong, atau ga hasilnya
[ , e1, e2, e3]
>>> array = custom_append_list(1, [2, 3, 4])
>>> print(array)
[1, 2, 3, 4]
"""


def custom_insert(elemen, array):
    array_baru = [None for i in range(custom_len(array) + 1)]
    array_baru[0] = elemen
    for i in range(custom_len(array)):
        array_baru[i + 1] = array[i]
    return array_baru


"""
Mengsimulasi pop() tapi cara penggunaannya beda sedikit
Untuk replikasi:
>>> elemen = array.pop(index)
Lakukan:
>>> elemen = array[index]
>>> array = custom_pop_remove(array, index)
"""


def custom_pop(array, index):
    if index == 0:
        return custom_pop(array[1:], index - 1)
    elif custom_len(array) == 0:
        return []
    elif custom_len(array) == 1:
        return array
    else:
        return custom_insert(array[0], custom_pop(array[1:], index - 1))


"""
Mirip dengan split() tapi cara penggunaannya beda sedikit
Untuk replikasi:
>>> data = text.split(pemisah)
Lakukan:
>>> data = custom.split(text, pemisah)
Hanya bisa digunakkan jika string selalu berakhir dengan \n
"""


def custom_split(string_list, pemisah=" "):
    data_list = []
    elemen_sementara = ""
    index = 0
    index_awal = 0
    index_akhir = -1
    while True:
        if string_list[index] == pemisah or string_list[index] == "\n":
            index_awal = index_akhir + 1
            index_akhir = index
            elemen_sementara = string_list[index_awal: index_akhir]
            data_list = custom_append(data_list, elemen_sementara)
            if string_list[index] == "\n":
                return data_list
        index += 1


"""
Function yang mengembalikan matriks data suatu file csv (tanpa baris pertamanya)
"""


def csv_to_matriks(nama_file_csv):
    data_matriks = []
    file_user = open(nama_file_csv, 'r')
    file_user.readline()
    while True:
        string_baris_user = file_user.readline()
        if string_baris_user == "":
            break
        data_baris_user = custom_split(string_baris_user, ";")
        data_matriks = custom_append(data_matriks, data_baris_user)
    file_user.close()
    return data_matriks


def cek_user_terdaftar(user, data):
    for i in range(custom_len(data)):
        if data[i][0] == user:
            return True
    return False


def cek_password_cocok(password, user, data):
    for i in range(custom_len(data)):
        if data[i][0] == user:
            if password == data[i][1]:
                return True
            return False
        return False


def daftar_jin(data):
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
        if cek_user_terdaftar(user_jin, data):
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
