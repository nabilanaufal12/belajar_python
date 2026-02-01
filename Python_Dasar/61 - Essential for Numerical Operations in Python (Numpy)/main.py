# Numpy: Essential for Numerical Operations in Python

import numpy as np

# Numpy Array vs. Python List
list_a = [1, 2, 3, 4]
vector_a = np.array([1, 2, 3, 4])

print(f"list_a = {list_a}")
print(f"\nvector_a = {vector_a}")

# Operasi pengkuadratan
# print(list_a ** 2) akan error
print(f"\nvector_a  ** 2: {vector_a ** 2}")

# Operasi perkalian skalar
print(f"\nlist_a * 2: {list_a * 2}")
print(f"\nvertor_a * 2: {vector_a * 2}")

# Membuat Matriks (Array 2D)
matrix_a = np.array([(1, 2, 3), 
                     (4, 5, 6),
                     (7, 8, 9)])
print(f"\nmatrix_a : \n{matrix_a}")
print(f"\nmatrix_a ** 2: \n{matrix_a ** 2}")

# Fungsi Pembantu untuk Membuat Matriks Khusus
## np.zeros((dimensi))
zeros_a = np.zeros((3, 3))
print(f"\nzeros_a : \n{zeros_a}")

## np.ones((dimensi))
ones_a = np.ones((3, 3))
print(f"\nones_a : \n{ones_a}")

# Operasi Aritmatika Matriks
hasil =  matrix_a + matrix_a ** 2 + ones_a
print(f"\nHasil Penjumlahan Matrix: \n{hasil}")