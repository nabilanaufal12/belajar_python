# Operator Membership (in / not in) di Python --- IGNORE ---

nama_belakang = "Santoso"
nama_tengah = "D"
nama_depan = "Bell"

print("Nama belakang :", nama_belakang)
print("Nama tengah  :", nama_tengah)
print("Nama depan   :", nama_depan)

# Menyambung string menggunakan operator +
nama_lengkap = nama_belakang + " " + nama_tengah + "'" + nama_depan
print("Nama lengkap menggunakan + :", nama_lengkap)

# Cek keanggotaan karakter dalam string menggunakan operator in dan not in
cek_d = 'd' in nama_lengkap
print("Apakah 'd' ada dalam nama lengkap? :", cek_d)

cek_D = 'D' in nama_lengkap
print("Apakah 'D' ada dalam nama lengkap? :", cek_D)

cek_d_tidak_ada = 'd' not in nama_lengkap
print("Apakah 'd' tidak ada dalam nama lengkap? :", cek_d_tidak_ada)

cek_D_tidak_ada = 'D' not in nama_lengkap
print("Apakah 'D' tidak ada dalam nama lengkap? :", cek_D_tidak_ada)