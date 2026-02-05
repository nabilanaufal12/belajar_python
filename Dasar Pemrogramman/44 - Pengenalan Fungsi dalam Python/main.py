# Pengenalan Fungsi dalam Python

def hello_world():
    """Fungsi sederhana yang mencetak 'Hello, World!'."""
    print("Hello, World!")

# Memanggil fungsi hello_world
hello_world()

def sapa(nama):
    """Fungsi untuk menyapa seseorang dengan nama yang diberikan."""
    return f"Halo, {nama}!"

# Memanggil fungsi sapa
nama_user = "Andi"
pesan_sapa = sapa(nama_user)
print(pesan_sapa)  # Output: Halo, Andi!