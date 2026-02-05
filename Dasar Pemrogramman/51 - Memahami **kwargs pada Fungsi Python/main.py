# Memahami **kwargs pada Fungsi Python

def fungsi(**kwargs):
    print(kwargs)

fungsi(nama="Mizu", tinggi=160, berat=47)

# Mengakses Nilai dalam **kwargs
def fungsi_detail(**kwargs):
    '''
    Docstring for fungsi_detail
    
    :param kwargs: Description
    '''
    nama = kwargs["nama"]
    tinggi = kwargs["tinggi"]
    berat = kwargs["berat"]

    print(f"{nama} memiliki tinggi {tinggi} dan berat {berat}")

fungsi_detail(nama="Mizu", tinggi=160, berat=47)

# Menggabungkan *args dan **kwargs
def math(*args, **kwargs):
    print(f"args : {args}")
    print(f"kwargs : {kwargs}")

math(1, 2, 3, 4, option="tambah")