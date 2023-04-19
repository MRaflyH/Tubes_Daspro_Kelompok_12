# F01 - Custom len
def custom_len(array, max_array):
    """
    mencari panjang suatu array dengan jumlah elemen maksimum tertentu
    :param array:
    :param max_array:
    :return: integer
    """
    # mencari instansi None pertama dan return index tersebut
    for i in range(max_array):
        if array[i] is None:
            return i

    return max_array

# F02 - Custom append
def custom_append(array, elemen, max_array):
    """
    menambah elemen pada akhir array (instansi None) pertama pada array tersebut
    jika array penuh, array tidak akan ganti
    :param array:
    :param elemen:
    :param max_array:
    :return: array
    """
    if custom_len(array, max_array) < max_array:
        # elemen dimasukkan pada index efektif terakhir array
        array[custom_len(array, max_array)] = elemen

    return array

# F03 - Custom insert
def custom_insert(elemen, array, max_array):
    """
    menambah elemen pada awal array pertama pada array tersebut
    jika array penuh, elemen terakhir array akan hilang
    :param elemen:
    :param array:
    :param max_array:
    :return: array
    """
    # menghapus elemen terakhir jika array penuh
    if custom_len(array, max_array) == max_array:
        array[max_array - 1] = None

    # setiap elemen array dipindah 1 ke kanan (index tambah 1)
    for i in range(custom_len(array, max_array), 0, -1):
        array[i] = array[i - 1]

    # elemen dimasukkan pada awal array
    array[0] = elemen

    return array

# F04 - Custom pop
def custom_pop(array, index, max_array):
    """
    menghapuskan suatu elemen pada array berdasarkan indexnya
    :param array:
    :param index:
    :param max_array:
    :return: array
    """
    # setiap elemen array setelah index dipindah 1 ke kiri (index kurang 1)
    for i in range(index, custom_len(array, max_array) - 1):
        array[i] = array[i + 1]

    # elemen terakhir array (duplikat) dihapuskan
    array[custom_len(array, max_array) - 1] = None

    return array

# F05 - Custom split
def custom_split(string_list, jumlah_elemen, pemisah):
    """
    memisahkan suatu string menjadi elemen-elemennya berdasarkan suatu pemisah
    :param string_list:
    :param jumlah_elemen:
    :param pemisah:
    :return: array
    """
    data_list = [None for i in range(jumlah_elemen)]
    index = 0
    elemen_sementara = ""

    while True:
        # jika char adalah pemisah atau akhir baris, append elemen baru pada data_list
        if string_list[index] == pemisah or string_list[index] == "\n":
            data_list = custom_append(data_list, elemen_sementara, jumlah_elemen)
            elemen_sementara = ""

            if string_list[index] == "\n":
                return data_list

        else:
            # menambah char pada elemen_sementara
            elemen_sementara += string_list[index]

        index += 1

# F06 - CSV to matriks
def csv_to_matriks(nama_file_csv, jumlah_elemen, max_data):
    """
    mengubah file csv menjadi suatu matriks
    :param nama_file_csv:
    :param jumlah_elemen:
    :param max_data:
    :return: array/matriks
    """
    data_matriks = [None for i in range(max_data)]
    file_user = open(nama_file_csv, 'r')
    file_user.readline()

    while True:
        # membaca baris selanjutnya
        string_baris_user = file_user.readline()

        # jika baris csv kosong, keluar dari loop
        if string_baris_user == "":
            break

        # mengubah baris csv menjadi array dan append array itu pada data_matriks
        data_baris_user = custom_split(string_baris_user, jumlah_elemen, ";")
        data_matriks = custom_append(data_matriks, data_baris_user, max_data)

    file_user.close()

    return data_matriks

# F07 - Cek nama terdaftar
def cek_nama_terdaftar(nama, data_user, max_data_user):
    """
    mengecek jika nama tertentu sudah terdaftar atau belum
    :param nama:
    :param data_user:
    :param max_data_user:
    :return: boolean
    """
    # mencari instansi munculnya nama pada data_user
    for i in range(custom_len(data_user, max_data_user)):
        if data_user[i][0] == nama:
            return True

    return False

# F08 - Cek password cocok
def cek_password_cocok(password, nama, data_user, max_data_user):
    """
    mengecek jika password suatu nama benar/cocok atau tidak
    :param password:
    :param nama:
    :param data_user:
    :param max_data_user:
    :return: boolean
    """
    # cek instansi munculnya nama
    for i in range(custom_len(data_user, max_data_user)):
        if data_user[i][0] == nama:
            # cek jika password cocok
            if password == data_user[i][1]:
                return True
            return False

    return False

# F09 - Name to role
def nama_to_role(nama, data_user, max_data_user):
    """
    mencari role suatu nama
    :param nama:
    :param data_user:
    :param max_data_user:
    :return: string
    """
    # cek instansi munculnya nama dan return rolenya
    for i in range(custom_len(data_user, max_data_user)):
        if data_user[i][0] == nama:
            return data_user[i][2]

    return None

# F10 - Daftar jin
def daftar_jin(data_user, max_data_user):
    """
    meminta input tipe, nama, dan password jin yang valid
    :param data_user:
    :param max_data_user:
    :return: array
    """
    # meminta tipe jin, diulangi sampai mendapat pengumpul atau pembangun
    while True:
        nomor_jin = int(input("Masukkan nomor jenis jin yang ingin dipanggil: "))
        print()

        if nomor_jin != 1 and nomor_jin != 2:
            print(f"Tidak ada jenis jin bernomor \"{nomor_jin}\"")
            print()

        else:
            if nomor_jin == 1:  # Jin pengumpul
                print("Memilih jin \"Pengumpul\".")
                jenis_jin = "jin_pengumpul"

            else:  # nomor_jin == 2; Jin pembangun
                print("Memilih jin \"Pembangun\".")
                jenis_jin = "jin_pembangun"

            print()

            break

    # meminta nama jin, diulangi sampai namanya belum terdaftar
    while True:
        user_jin = input("Masukkan username jin: ")

        if cek_nama_terdaftar(user_jin, data_user, max_data_user):
            print()
            print(f"Username \"{user_jin}\"sudah diambil!")
            print()

        else:
            break

    # meminta password jin, diulangi sampai panjangnya diantara 5-25 karakter
    while True:
        pass_jin = input("Masukkan password jin: ")
        print()

        if (len(pass_jin) < 5) or (len(pass_jin) > 25):
            print("Password panjangnya harus 5-25 karakter!")
            print()

        else:
            break

    return [user_jin, pass_jin, jenis_jin]

# F11 - Hapus candi
def hapus_candi(index, data_candi):
    """
    menghapus candi dengan index tertentu
    :param index:
    :param data_candi:
    :return: array
    """
    # mengganti semua elemennya menjadi None kecuali "id"
    data_candi[index][1] = None
    data_candi[index][2] = None
    data_candi[index][3] = None
    data_candi[index][4] = None

    return data_candi

# F12 - Hapus candi jin
def hapus_candi_jin(jin, data_candi, max_data_candi):
    """
    menghapus candi hasil buat jin tertentu
    :param jin:
    :param data_candi:
    :param max_data_candi:
    :return: array
    """
    # cek semua instansi candi dengan pembuat jin tertentu
    for i in range(custom_len(data_candi, max_data_candi) - 1, -1, -1):
        if data_candi[i][1] == jin:
            # candi dihapus berdasarkan indexnya
            hapus_candi(i, data_candi)

    return data_candi

# F13 - Hitung candi
def hitung_candi(data_candi, max_data_candi):
    """
    menghitung jumlah candi
    :param data_candi:
    :param max_data_candi:
    :return: integer
    """
    jumlah_candi = 0

    # cek setiap instansi candi yang tidak kosong (None)
    for i in range(custom_len(data_candi, max_data_candi)):
        if data_candi[i][1] is not None:
            jumlah_candi += 1

    return jumlah_candi

# F14 - Leksikografis lebih rendah
def leksikografis_lebih_rendah(nama_pertama, nama_kedua):
    """
    mengecek jika kata pertama terurut secara leksikografis lebih duluan daripada kata kedua
    :param nama_pertama:
    :param nama_kedua:
    :return: boolean
    """
    kata_pertama_lebih_pendek = True
    length = len(nama_pertama)

    # cek panjang kata terpendek untuk mencegahi eror dan mengendali kejadian dua kata yang mirip tetapi salah satu kata
    # memiliki huruf lebih banyak seperti "ayam" dan "ayamgoreng", "ayam" terurut duluan secara leksikografis
    if len(nama_kedua) < len(nama_pertama):
        length = len(nama_kedua)
        kata_pertama_lebih_pendek = False

    # membandingkan setiap huruf
    for i in range(length):
        if ord(nama_pertama[i]) < ord(nama_kedua[i]):
            return True
        elif ord(nama_kedua[i]) < ord(nama_pertama[i]):
            return False

    return kata_pertama_lebih_pendek

# F15 - Urutkan leksikografis
def urutkan_leksikografis(data_jin, max_data_jin):
    """
    mengurutkan suatu array string secara leksikografis
    :param data_jin:
    :param max_data_jin:
    :return: array
    """
    # membandingakan elemen 1 - 2, 1 - 3, 1 - 4, ..., 1 - n, 2 - 3, 2 - 4, ... n-1 - n
    for i in range(custom_len(data_jin, max_data_jin) - 1):
        for j in range(i + 1, custom_len(data_jin, max_data_jin)):
            # jika dua elemen tidak terurut, ditukar posisinya
            if not leksikografis_lebih_rendah(data_jin[i], data_jin[j]):
                data_jin[i], data_jin[j] = data_jin[j], data_jin[i]

    return data_jin

# F16 - Count jin total pengumpul pembangun
def count_jin_total_pengumpul_pembangun(data_user, max_data_user):
    """
    menghitung jumlah jin, jin pengumpul, dan jin pembangun
    :param data_user:
    :param max_data_user:
    :return: integer total jin, integer total jin pengumpul, integer total jin pembangun
    """
    count_total_jin = 0
    count_total_jin_pengumpul = 0
    count_total_jin_pembangun = 0

    # cek semua instansi jin, jin pengumpul, dan jin pembangun
    for i in range(custom_len(data_user, max_data_user)):
        if data_user[i][2] == "jin_pengumpul" or data_user[i][2] == "jin_pembangun":
            if data_user[i][2] == "jin_pengumpul":
                count_total_jin_pengumpul += 1
            elif data_user[i][2] == "jin_pembangun":
                count_total_jin_pembangun += 1
            count_total_jin += 1

    return count_total_jin, count_total_jin_pengumpul, count_total_jin_pembangun

# F17 - Jin terajin termalas
def jin_terajin_termalas(data_jin, data_user, data_candi, max_data_jin, max_data_user, max_data_candi):
    """
    mencari jin terajin dan jin termalas
    :param data_jin:
    :param data_user:
    :param data_candi:
    :param max_data_jin:
    :param max_data_user:
    :param max_data_candi:
    :return: string jin terajin, string jin termalas
    """
    # membuat array jumlah candi yang dibangun setiap jin
    jumlah_candi_dibangun = [None for j in range(max_data_jin)]

    for i in range(custom_len(data_jin, max_data_jin)):
        jumlah_candi_dibangun[i] = 0

    # cek setiap instansi candi dan jin yang membangunnya untuk ditambahkan pada jumlah_candi_jin
    for i in range(custom_len(data_candi, max_data_candi)):
        for j in range(custom_len(data_jin, max_data_jin)):
            if data_candi[i][1] == data_jin[j]:
                jumlah_candi_dibangun[j] += 1

    index_awal = 0
    index_jin_terajin = 0
    index_jin_termalas = 0

    # cek jin pertama yang adalah jin pembangun atau telah membangun minimal 1 cani
    for i in range(custom_len(data_jin, max_data_jin)):
        if nama_to_role(data_jin[i], data_user, max_data_user) == "jin_pembangun" or jumlah_candi_dibangun[i] != 0:
            index_awal = i
            index_jin_terajin = i
            index_jin_termalas = i
            break

    # menjadi jin terajin dan termalas dengan membandingkan jumlah candi yang dibangunnya
    for i in range(index_awal, custom_len(jumlah_candi_dibangun, max_data_jin) - 1):
        if nama_to_role(data_jin[i], data_user, max_data_user) == "jin_pembangun" or jumlah_candi_dibangun[i] != 0:
            if jumlah_candi_dibangun[i] > jumlah_candi_dibangun[index_jin_terajin]:
                index_jin_terajin = i
            elif jumlah_candi_dibangun[i] < jumlah_candi_dibangun[index_jin_termalas]:
                index_jin_termalas = i

    jin_terajin = data_jin[index_jin_terajin]
    jin_termalas = data_jin[index_jin_termalas]

    return jin_terajin, jin_termalas

# F18 - Jumlah air batu pasir
def jumlah_air_batu_pasir(data_bahan_bangunan, max_data_bahan_bangunan):
    """
    mencari jumlah air, batu, dan pasir yang tersedia
    :param data_bahan_bangunan:
    :param max_data_bahan_bangunan:
    :return: integer jumlah air, integer jumlah batu, integer jumlah pasir
    """
    jumlah_pasir = 0
    jumlah_air = 0
    jumlah_batu = 0

    # cek munculnya air, batu, dan pasir serta menyimpan jumlahnya
    for i in range(custom_len(data_bahan_bangunan, max_data_bahan_bangunan)):
        if data_bahan_bangunan[i][0] == "air":
            jumlah_air = data_bahan_bangunan[i][2]
        elif data_bahan_bangunan[i][0] == "batu":
            jumlah_batu = data_bahan_bangunan[i][2]
        elif data_bahan_bangunan[i][0] == "pasir":
            jumlah_pasir = data_bahan_bangunan[i][2]

    return jumlah_air, jumlah_batu, jumlah_pasir

# F19 - Append candi
def append_candi(nama, air, batu, pasir, data_candi, max_data_candi):
    """
    append candi baru
    :param nama:
    :param air:
    :param batu:
    :param pasir:
    :param data_candi:
    :param max_data_candi:
    :return: array data candi
    """
    data_kosong_ditemukan = False

    # cek jika ada id candi yang kosong dan mengisinya
    # contoh : [4, None, None, None, None]
    for i in range(custom_len(data_candi, max_data_candi)):
        if data_candi[i][1] is None:
            data_candi[i][1] = nama
            data_candi[i][2] = pasir
            data_candi[i][3] = batu
            data_candi[i][4] = air
            data_kosong_ditemukan = True
            break

    # jika semua id terpenuhi, membuat id baru dan mengisinya dengan candi
    if not data_kosong_ditemukan:
        candi_baru = [custom_len(data_candi, max_data_candi) + 1, nama, pasir, batu, air]
        data_candi = custom_append(data_candi, candi_baru, max_data_candi)

    return data_candi

# F20 - Update bahan
def update_bahan(jumlah_air, jumlah_batu, jumlah_pasir, data_bahan_bangunan, max_data_bahan_bangunan):
    """
    mengupdate data bahan bangunan dengan jumlah bahan bangunan baru
    :param jumlah_air:
    :param jumlah_batu:
    :param jumlah_pasir:
    :param data_bahan_bangunan:
    :param max_data_bahan_bangunan:
    :return: array data bahan bangunan
    """
    air_ditemukan = False
    batu_ditemukan = False
    pasir_ditemukan = False

    # mengecek jika air, batu, dan pasir sudah ada pada data array dan mengisinya
    for i in range(custom_len(data_bahan_bangunan, max_data_bahan_bangunan)):
        if data_bahan_bangunan[i][0] == "air":
            data_bahan_bangunan[i][2] = jumlah_air
            air_ditemukan = True
        elif data_bahan_bangunan[i][0] == "batu":
            data_bahan_bangunan[i][2] = jumlah_batu
            batu_ditemukan = True
        elif data_bahan_bangunan[i][0] == "pasir":
            data_bahan_bangunan[i][2] = jumlah_pasir
            pasir_ditemukan = True

    # jika tidak ada, membuat elemen tersebut kemudian mengisinya
    if not air_ditemukan:
        data_bahan_bangunan = custom_append(data_bahan_bangunan, ["air", "air", jumlah_air], max_data_bahan_bangunan)
    if not batu_ditemukan:
        data_bahan_bangunan = custom_append(data_bahan_bangunan, ["batu", "batu", jumlah_batu], max_data_bahan_bangunan)
    if not pasir_ditemukan:
        data_bahan_bangunan = custom_append(data_bahan_bangunan, ["pasir", "pasir", jumlah_pasir],
                                            max_data_bahan_bangunan)

    return data_bahan_bangunan

# F21 - Pakai bahan
def pakai_bahan(butuh_air, butuh_batu, butuh_pasir, data_bahan_bangunan, max_data_bahan_bangunan):
    """
    memakai bahan bangunan dan mengupdate data bahan bangunan
    :param butuh_air:
    :param butuh_batu:
    :param butuh_pasir:
    :param data_bahan_bangunan:
    :param max_data_bahan_bangunan:
    :return: array data bahan bangunan
    """
    # mengurangi semua bahan
    jumlah_air, jumlah_batu, jumlah_pasir = jumlah_air_batu_pasir(data_bahan_bangunan, max_data_bahan_bangunan)
    jumlah_air -= butuh_air
    jumlah_batu -= butuh_batu
    jumlah_pasir -= butuh_pasir

    # mengupdate bahan bangunan
    data_bahan_bangunan = update_bahan(jumlah_air, jumlah_batu, jumlah_pasir, data_bahan_bangunan,
                                       max_data_bahan_bangunan)

    return data_bahan_bangunan

# F22 - Tambah bahan
def tambah_bahan(nemu_air, nemu_batu, nemu_pasir, data_bahan_bangunan, max_data_bahan_bangunan):
    """
    menambah bahan bangunan dan mengupdate data bahan bangunan
    :param nemu_air:
    :param nemu_batu:
    :param nemu_pasir:
    :param data_bahan_bangunan:
    :param max_data_bahan_bangunan:
    :return: array data bahan bangunan
    """
    # menambah semua bahan
    jumlah_air, jumlah_batu, jumlah_pasir = jumlah_air_batu_pasir(data_bahan_bangunan, max_data_bahan_bangunan)
    jumlah_air += nemu_air
    jumlah_batu += nemu_batu
    jumlah_pasir += nemu_pasir

    # mengupdate bahan bangunan
    data_bahan_bangunan = update_bahan(jumlah_air, jumlah_batu, jumlah_pasir, data_bahan_bangunan,
                                       max_data_bahan_bangunan)

    return data_bahan_bangunan

# F23 - Copy matriks
def copy_matriks(array, max_array):
    """
    melakukan deep copy pada suatu array (memiliki reference object yang beda)
    :param array:
    :param max_array:
    :return: array
    """
    array_baru = [None for i in range(max_array)]

    # memasukkan setiap elemen suatu array pada array_baru
    for i in range(max_array):
        array_baru[i] = array[i]

    return array_baru

# F24 - Bangun tunggal
def bangun_tunggal(nama, butuh_pasir, butuh_batu, butuh_air, data_candi, data_bahan_bangunan, max_data_candi,
                   max_data_bahan_bangunan):
    """
    membangun suatu candi dan memakai bahan bangunan
    :param nama:
    :param butuh_pasir:
    :param butuh_batu:
    :param butuh_air:
    :param data_candi:
    :param data_bahan_bangunan:
    :param max_data_candi:
    :param max_data_bahan_bangunan:
    :return: array data candi, array data bahan bangunan, boolean keberhasilan dibangun candi
    """
    berhasil_dibangun = False
    jumlah_air, jumlah_batu, jumlah_pasir = jumlah_air_batu_pasir(data_bahan_bangunan, max_data_bahan_bangunan)

    if jumlah_pasir >= butuh_pasir and jumlah_batu >= butuh_batu and jumlah_air >= butuh_air:
        data_candi = append_candi(nama, butuh_air, butuh_batu, butuh_pasir, data_candi, max_data_candi)
        data_bahan_bangunan = pakai_bahan(butuh_air, butuh_batu, butuh_pasir, data_bahan_bangunan,
                                          max_data_bahan_bangunan)

        berhasil_dibangun = True

    return data_candi, data_bahan_bangunan, berhasil_dibangun

# F25 - Custom reverse split
def custom_reverse_split(data_list, jumlah_elemen, pemisah):
    """
    mengubah array menjadi string dengan suatu pemisah
    :param data_list:
    :param jumlah_elemen:
    :param pemisah:
    :return: string
    """
    string_list = ""

    # untuk setiap elemen ditambahkan kepada string dan ditambahkan pemisahnya sampai elemen terakhir
    for i in range(jumlah_elemen):
        string_list += str(data_list[i])
        if i < jumlah_elemen - 1:
            string_list += pemisah
        else:
            string_list += "\n"

    return string_list

# F26 - Matriks to CSV
def matriks_to_csv(folder_path, file_name, jumlah_elemen, data_matriks, max_data_matriks):
    """
    mengubah suatu matriks menjadi file csv
    :param folder_path:
    :param file_name:
    :param jumlah_elemen:
    :param data_matriks:
    :param max_data_matriks:
    """

    file_path = folder_path + '/' + file_name

    # open file
    with open(file_path, 'w') as f:
        if file_name == "user.csv":
            f.write("username;password;role\n")
        elif file_name == "candi.csv":
            f.write("id;pembuat;pasir;batu;air\n")
        elif file_name == "bahan_bangunan.csv":
            f.write("nama;deskripsi;jumlah\n")

        for i in range(custom_len(data_matriks, max_data_matriks)):
            string_list = custom_reverse_split(data_matriks[i], jumlah_elemen, ";")
            f.write(string_list)

# test
