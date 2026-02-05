# Type Hints pada Fungsi Python

# Implementasi Type Hints

## 1. Untuk Argumen Fungsi
def sepuluh_pangkat(argumen: int):
    hasil = 10 ** argumen
    return hasil

print(sepuluh_pangkat(2))

## 2. Untuk Nilai Kembalian (Return Value)
def fungsi_matematika(argumen: int) -> int:
    hasil = 10 ** argumen
    return hasil

print(sepuluh_pangkat(2))

def tampilkan(argumen: str) -> None:
    print(argumen)

tampilkan("Mizu")