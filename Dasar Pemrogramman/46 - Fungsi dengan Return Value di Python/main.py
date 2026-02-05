# Fungsi dengan Return Value di Python

# Implementasi Fungsi dengan Return Value

## 1. Fungsi dengan Single Return (Mengembalikan Satu Nilai)
def kuadrat(input_angka):
    """Mengembalikan kuadrat dari x."""
    output_kuadrat = input_angka ** 2
    return output_kuadrat

hasil_kuadrat = kuadrat(5)
print("Hasil kuadrat dari 5 adalah:", hasil_kuadrat)

tambahan_kuadrat = 5 + kuadrat(3)
print("5 ditambah kuadrat dari 3 adalah:", tambahan_kuadrat)

## 2. Fungsi dengan Multi Input dan Single Return
def hitung_luas_persegi_panjang(panjang, lebar):
    """Mengembalikan luas dari persegi panjang."""
    luas = panjang * lebar
    return luas

luas_persegi_panjang = hitung_luas_persegi_panjang(4, 6)
print("Luas persegi panjang dengan panjang 4 dan lebar 6 adalah:", luas_persegi_panjang)

## 3. Fungsi dengan Multi Return (Mengembalikan Banyak Nilai Sekaligus)
def hitung_luas_dan_keliling_persegi(sisi):
    """Mengembalikan luas dan keliling dari persegi."""
    luas = sisi * sisi
    keliling = 4 * sisi
    return luas, keliling

luas, keliling = hitung_luas_dan_keliling_persegi(5)
print("Luas persegi dengan sisi 5 adalah:", luas)
print("Keliling persegi dengan sisi 5 adalah:", keliling)