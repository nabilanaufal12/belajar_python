# Summary Operasi Logika Pytho

> Generated: January 16th, 2026 4:59 PM
> Sources: Belajar Python [Dasar] - 11 - Operasi Logika atau.youtube, pasted-text-1.md

---

# Catatan Studi: Operasi Logika (Boolean) di Python

Operasi logika atau boolean adalah dasar dalam pemrograman yang memungkinkan kita untuk membuat keputusan berdasarkan kondisi `True` (benar) atau `False` (salah). Dalam Python, terdapat empat operasi logika utama: **NOT**, **OR**, **AND**, dan **XOR**.

## 1. Operasi NOT (Negasi)

Operasi **NOT** berfungsi untuk membalikkan nilai boolean. Ini adalah operasi yang paling sederhana karena hanya membutuhkan satu input.

*   **Konsep**: Membalikkan nilai kebenaran dari sebuah ekspresi.
*   **Perilaku**:
    *   Jika inputnya `True`, hasilnya akan menjadi `False`.
    *   Jika inputnya `False`, hasilnya akan menjadi `True`.
*   **Sintaks**: `not a`

**Tabel Kebenaran NOT:**
| Input (a) | Output (not a) |
| :--- | :--- |
| `True` | `False` |
| `False` | `True` |

**Contoh Kode:**
```python
a = True
c = not a
print("data a =", a)
print("data c =", c) # Hasil: False
```

## 2. Operasi OR (Disjungsi)

Operasi **OR** memerlukan dua buah nilai boolean sebagai input. Operasi ini akan menghasilkan `True` jika setidaknya salah satu input bernilai `True`.

*   **Konsep**: Menggabungkan dua kondisi, di mana kebenaran salah satu kondisi sudah cukup untuk membuat hasil keseluruhan menjadi `True`.
*   **Perilaku**:
    *   Akan menghasilkan `True` jika salah satu atau kedua input bernilai `True`.
    *   Hanya akan menghasilkan `False` jika **kedua** input bernilai `False`.
*   **Analogi**: Mirip seperti operasi pertambahan, di mana `0+1=1`, `1+0=1`, dan `1+1` dianggap `True` (lebih dari nol).
*   **Sintaks**: `a or b`

**Tabel Kebenaran OR:**
| a | b | a OR b |
| :--- | :--- | :--- |
| `False` | `False` | `False` |
| `False` | `True` | `True` |
| `True` | `False` | `True` |
| `True` | `True` | `True` |

**Contoh Kode:**
```python
a = False
b = True
c = a or b
print(a, 'OR', b, '=', c) # Hasil: True
```

## 3. Operasi AND (Konjungsi)

Operasi **AND** juga memerlukan dua buah nilai boolean sebagai input. Operasi ini akan menghasilkan `True` hanya jika **kedua** input bernilai `True`.

*   **Konsep**: Menggabungkan dua kondisi, di mana kedua kondisi harus benar agar hasil keseluruhan menjadi `True`.
*   **Perilaku**:
    *   Akan menghasilkan `True` hanya jika **kedua** input bernilai `True`.
    *   Jika ada satu saja input yang bernilai `False`, maka hasilnya akan `False`.
*   **Analogi**: Mirip seperti operasi perkalian, di mana `1x1=1`, sedangkan `1x0=0` atau `0x0=0`.
*   **Sintaks**: `a and b`

**Tabel Kebenaran AND:**
| a | b | a AND b |
| :--- | :--- | :--- |
| `False` | `False` | `False` |
| `False` | `True` | `False` |
| `True` | `False` | `False` |
| `True` | `True` | `True` |

**Contoh Kode:**
```python
a = True
b = True
c = a and b
print(a, 'AND', b, '=', c) # Hasil: True
```

## 4. Operasi XOR (Exclusive OR)

Operasi **XOR** (Exclusive OR) adalah operasi logika yang unik dan memerlukan dua input boolean. Operasi ini akan menghasilkan `True` jika input-inputnya memiliki nilai yang **berbeda**.

*   **Konsep**: Menghasilkan `True` jika hanya satu dari dua kondisi yang benar, tetapi `False` jika kedua kondisi sama (keduanya `True` atau keduanya `False`).
*   **Perilaku**:
    *   Akan menghasilkan `True` jika **salah satu saja** input bernilai `True`.
    *   Akan menghasilkan `False` jika **kedua** input bernilai sama (keduanya `True` atau keduanya `False`).
*   **Sintaks**: `a ^ b` (menggunakan operator `^` atau "topi")

**Tabel Kebenaran XOR:**
| a | b | a XOR b (^) |
| :--- | :--- | :--- |
| `False` | `False` | `False` |
| `False` | `True` | `True` |
| `True` | `False` | `True` |
| `True` | `True` | `False` |

**Contoh Kode:**
```python
a = True
b = True
c = a ^ b
print(a, 'XOR', b, '=', c) # Hasil: False (karena sama-sama True)
```

## Tabel Kebenaran

Tabel-tabel yang menunjukkan semua kemungkinan input dan output dari operasi logika disebut sebagai **Tabel Kebenaran**. Tabel ini sangat membantu untuk memahami perilaku setiap operasi logika secara sistematis.