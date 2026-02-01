# Python Dictionary: Pengenalan dan Perbandingan dengan List

data_list = ['apel', 'pisang', 'jeruk']
print("Data List:", data_list)

data_dict = {
    'buah1': 'apel',
    'buah2': 'pisang',
    'buah3': 'jeruk'}
print("Data Dictionary:", data_dict)

# Mengakses elemen dalam list
print("Elemen pertama dalam list:", data_list[0])

# Mengakses elemen dalam dictionary
print("Elemen dengan kunci 'buah1' dalam dictionary:", data_dict['buah1'])

data_dictionary_kompleks = {
    'nama_depan': 'Budi',
    'umur': 30,
    'is_mahasiswa': False,
    'hobi': ['membaca', 'berenang'],
    'nilai_ujian': {
        'matematika': 90,
        'fisika': 85
    },
    1: 'Ini adalah value dengan key angka' # Key juga bisa berupa angka
}

print("Data Dictionary Kompleks:", data_dictionary_kompleks)
print("Nama Depan:", data_dictionary_kompleks['nama_depan'])
print("Hobi kedua:", data_dictionary_kompleks['hobi'][1])
print("Kota:", data_dictionary_kompleks['alamat']['kota'])