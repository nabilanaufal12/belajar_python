# Summary Operator Assignment

> Generated: January 17th, 2026 9:21 PM
> Sources: Belajar Python [Dasar] - 14 - Operator Assignment.youtube, pasted-text-1.md

---

# Operator Assignment dalam Python

Operator assignment adalah operator yang digunakan untuk menetapkan nilai ke sebuah variabel. Dalam Python, selain assignment dasar (`=`), terdapat juga **operator assignment gabungan** yang memungkinkan kita untuk melakukan operasi aritmatika, bitwise, atau shifting dan assignment secara bersamaan, sehingga mempersingkat penulisan kode.

## Assignment Dasar (`=`)

Assignment dasar adalah operator yang paling umum digunakan untuk memberikan nilai awal pada sebuah variabel.
Contohnya, `a = 5` berarti nilai `5` ditetapkan ke variabel `a`.

```python
a = 5
print("Nilai a =", a) # Output: Nilai a = 5
```

## Operator Assignment Aritmatika

Operator-operator ini menggabungkan operasi aritmatika standar dengan assignment.

### Penjumlahan (`+=`)
Operator `+=` digunakan untuk menambahkan nilai ke variabel yang sudah ada. Ekspresi `a += b` adalah singkatan dari `a = a + b`.

```python
a = 5
a += 1 # Artinya: a = a + 1
print("Nilai a setelah += 1:", a) # Output: Nilai a setelah += 1: 6
```

### Pengurangan (`-=`)
Operator `-=` digunakan untuk mengurangi nilai dari variabel yang sudah ada. Ekspresi `a -= b` adalah singkatan dari `a = a - b`.

```python
a = 6 # Melanjutkan dari contoh sebelumnya
a -= 2 # Artinya: a = a - 2
print("Nilai a setelah -= 2:", a) # Output: Nilai a setelah -= 2: 4
```

### Perkalian (`*=`)
Operator `*=` digunakan untuk mengalikan variabel dengan suatu nilai. Ekspresi `a *= b` adalah singkatan dari `a = a * b`.

```python
a = 4 # Melanjutkan dari contoh sebelumnya
a *= 5 # Artinya: a = a * 5
print("Nilai a setelah *= 5:", a) # Output: Nilai a setelah *= 5: 20
```

### Pembagian (`/=`)
Operator `/=` digunakan untuk membagi variabel dengan suatu nilai. Ekspresi `a /= b` adalah singkatan dari `a = a / b`. Hasil pembagian ini akan selalu berupa bilangan *float*.

```python
a = 20 # Melanjutkan dari contoh sebelumnya
a /= 2 # Artinya: a = a / 2
print("Nilai a setelah /= 2:", a) # Output: Nilai a setelah /= 2: 10.0
```

### Modulus (`%=`)
Operator `%=` digunakan untuk menghitung sisa hasil bagi (*modulus*) dan menetapkannya kembali ke variabel. Ekspresi `a %= b` adalah singkatan dari `a = a % b`.

```python
b = 10
b %= 3 # Artinya: b = b % 3 (10 dibagi 3, sisanya 1)
print("Nilai b setelah %= 3:", b) # Output: Nilai b setelah %= 3: 1
```

### Floor Division (`//=`)
Operator `//=` digunakan untuk melakukan pembagian bulat (*floor division*) dan menetapkannya kembali ke variabel. Ekspresi `a //= b` adalah singkatan dari `a = a // b`.

```python
b = 10 # Mengatur ulang nilai b
b //= 3 # Artinya: b = b // 3 (10 dibagi 3, hasil bulatnya 3)
print("Nilai b setelah //= 3:", b) # Output: Nilai b setelah //= 3: 3
```

### Eksponen (`**=`)
Operator `**=` digunakan untuk menghitung pangkat (*eksponen*) dan menetapkannya kembali ke variabel. Ekspresi `a **= b` adalah singkatan dari `a = a ** b`.

```python
a = 5 # Mengatur ulang nilai a
a **= 3 # Artinya: a = a ** 3 (5 pangkat 3)
print("Nilai a setelah **= 3:", a) # Output: Nilai a setelah **= 3: 125
```

## Operator Assignment Bitwise

Operator-operator ini melakukan operasi bitwise (pada level bit) dan menetapkan hasilnya kembali ke variabel. Untuk nilai boolean, operasi ini akan bertindak seperti operator logika biasa.

### Bitwise OR (`|=`)
Operator `|=` melakukan operasi OR bitwise dan menetapkan hasilnya. Ekspresi `a |= b` adalah singkatan dari `a = a | b`.

```python
c = True
c |= False # Artinya: c = c | False
print("Nilai c setelah |= False:", c) # Output: Nilai c setelah |= False: True

c = False
c |= False # Artinya: c = c | False
print("Nilai c setelah |= False (c=False):", c) # Output: Nilai c setelah |= False (c=False): False
```

### Bitwise AND (`&=`)
Operator `&=` melakukan operasi AND bitwise dan menetapkan hasilnya. Ekspresi `a &= b` adalah singkatan dari `a = a & b`.

```python
c = True
c &= False # Artinya: c = c & False
print("Nilai c setelah &= False:", c) # Output: Nilai c setelah &= False: False

c = True # Mengatur ulang nilai c
c &= True # Artinya: c = c & True
print("Nilai c setelah &= True:", c) # Output: Nilai c setelah &= True: True
```

### Bitwise XOR (`^=`)
Operator `^=` melakukan operasi XOR bitwise (exclusive OR) dan menetapkan hasilnya. Ekspresi `a ^= b` adalah singkatan dari `a = a ^ b`.

```python
c = True # Mengatur ulang nilai c
c ^= True # Artinya: c = c ^ True
print("Nilai c setelah ^= True:", c) # Output: Nilai c setelah ^= True: False
```

## Operator Assignment Shifting

Operator-operator ini menggeser bit-bit dalam representasi biner suatu angka dan menetapkan hasilnya kembali ke variabel.

### Geser Kanan (`>>=`)
Operator `>>=` menggeser bit-bit variabel ke kanan sejumlah yang ditentukan dan menetapkan hasilnya. Setiap geseran ke kanan setara dengan pembagian bulat dengan 2. Ekspresi `a >>= b` adalah singkatan dari `a = a >> b`.

```python
d = 0b0100 # Nilai 4 dalam biner
d >>= 2    # Geser kanan 2 kali
print("Nilai d setelah >>= 2:", format(d, '04b'), "(nilai desimal:", d, ")") # Output: Nilai d setelah >>= 2: 0001 (nilai desimal: 1)
```

### Geser Kiri (`<<=`)
Operator `<<=` menggeser bit-bit variabel ke kiri sejumlah yang ditentukan dan menetapkan hasilnya. Setiap geseran ke kiri setara dengan perkalian dengan 2. Ekspresi `a <<= b` adalah singkatan dari `a = a << b`.

```python
d = 1 # Mengatur ulang nilai d (biner 0001)
d <<= 1 # Geser kiri 1 kali
print("Nilai d setelah <<= 1:", format(d, '04b'), "(nilai desimal:", d, ")") # Output: Nilai d setelah <<= 1: 0010 (nilai desimal: 2)
```