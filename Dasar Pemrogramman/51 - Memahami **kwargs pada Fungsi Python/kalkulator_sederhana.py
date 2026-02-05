# Studi Kasus: Kalkulator Dinamis

def math(*args, **kwargs):
    '''
    Docstring for math
    
    :param args: Description
    :param kwargs: Description
    '''
    hasil = 0

    if kwargs["option"] == "tambah":
        print("Operasi Penjumlahan")
        for angka in args:
            hasil += angka

    elif kwargs["option"] == "kurang":
        print("Operasi Penjumlahan")
        for angka in args:
            hasil -= angka

    else:
        print("Tidak ada operasi")
    
    return hasil

hasil_tambah = math(1, 2, 3, 4, option="tambah")
print(hasil_tambah)

hasil_kurang = math(1, 2, 3, 4, option="kurang")
print(hasil_kurang)