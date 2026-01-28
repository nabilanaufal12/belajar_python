# Catatan Studi: Program Menghitung Luas dan Keliling Persegi Panjang dengan Python

import os

def menu():
    '''
    Docstring for menu
    '''
    os.system("clear")
    print(f"{'Program Menghitung Luas Dan':^40}")
    print(f"{'Keliling Persegi Panjang':^40}")
    print(f"{'-'*40}")

def input_user():
    '''
    Docstring for input_user
    
    :param panjang: Description
    :param lebar: Description
    '''
    panjang = int(input("Masukkan nilai panjang: "))
    lebar = int(input("Masukkan nilai lebar: "))
    return panjang, lebar

def hitung_luas(panjang, lebar):
    '''
    Docstring for hitung_luas
    
    :param panjang: Description
    :param lebar: Description
    '''
    return panjang * lebar

def hitung_keliling(panjang, lebar):
    '''
    Docstring for hitung_kelliling
    
    :param panjang: Description
    :param lebar: Description
    '''
    return 2 * (panjang + lebar)

def tampilan_hasil(pesan, hasil):
    '''
    Docstring for tampilan_hasil
    
    :param pesan: Description
    :param hasil: Description
    '''
    print(f"hasil perhitungan {pesan}: {hasil}")

while True:
    menu()

    print("""Pilih menu:
1. Hitung Luas
2. Hitung Keliling
3. Keluar Program
          """)
    

    pilih_menu = int(input("Pilih menu: "))
    if pilih_menu == 1:
        PANJANG, LEBAR = input_user()
        LUAS = hitung_luas(PANJANG, LEBAR)
        tampilan_hasil("luas", LUAS)
    elif pilih_menu == 2:
        PANJANG, LEBAR = input_user()
        KELILING = hitung_keliling(PANJANG, LEBAR)
        tampilan_hasil("keliling", KELILING)
    else: break
    

    lanjut = input("Apakah mau lanjut? (y/n) : ")
    if lanjut.lower() == 'n':
        break

print("Terimakasih telah menggunakan program ini.")