# Konsep dan Fungsi break

## Contoh Dasar Penggunaan break
print("Contoh Dasar Penggunaan break:")
angka = 0
while angka < 10:
    print(f"Angka: {angka}")
    if angka == 5:
        print("Menghentikan loop karena angka mencapai 5")
        break
    angka += 1
    print("Lanjut ke iterasi berikutnya.")
print("Selesai dengan loop dasar.\n")

## Contoh Penggunaan break dalam Loop Bersarang
print("Contoh Penggunaan break dalam Loop Bersarang:")
for i in range(1, 6):
    for j in range(1, 6):
        print(f"i: {i}, j: {j}")
        if j == 3:
            print("Menghentikan loop dalam karena j mencapai 3")
            break
    print("Lanjut ke iterasi berikutnya dari loop luar.")
print("Selesai dengan loop bersarang.\n")

## Contoh Implementasi dengan Input Pengguna
print("Contoh 1 Implementasi dengan Input Pengguna:")
while True:
    user_input = input("Masukkan 'stop' untuk menghentikan: ")
    if user_input == "stop":
        print("Loop dihentikan oleh pengguna.")
        break
    print(f"Anda memasukkan: {user_input}")
print("Selesai dengan loop input pengguna.\n")

print("Contoh 2 Implementasi dengan Input Pengguna:")
input_str = int(input("Masukkan angka positif (masukkan angka negatif untuk berhenti): "))
angka = 0
while angka < 10:
    print(f"Angka: {angka}")
    if angka == input_str:
        print("Menghentikan loop karena angka mencapai input_str")
        break
    angka += 1
    print("Lanjut ke iterasi berikutnya.")
print("Selesai dengan loop input angka.\n")
