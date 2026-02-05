# Konsep While Loop

## Sintaks Dasar
# while kondisi:
#     blok kode yang akan diulang
#     (opsional) pernyataan untuk mengubah kondisi agar loop dapat berhenti

## Bahaya: Infinite Loop
# angka = 1
# while angka <= 5:
    # print(f"Angka saat ini: {angka}")
    # Tidak ada pernyataan untuk mengubah kondisi
    # Ini akan menyebabkan infinite loop karena angka tidak berubah
    # angka += 1  # Jika baris ini diaktifkan, loop akan berhenti setelah angka mencapai 6

## Mengontrol While Loop
angka = 0
print(f"Angka awal: {angka}")

while angka < 5:
    angka += 1  # Mengubah kondisi agar loop dapat berhenti
    print(f"Angka saat ini: {angka}")

print("Loop selesai.")