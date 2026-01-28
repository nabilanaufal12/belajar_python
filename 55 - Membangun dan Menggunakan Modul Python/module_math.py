# Module Math

def penjumlahan(*args):
    """
    Docstring for penjumlahan
    
    :param args: Description
    """
    hasil = 0

    for i in args:
        hasil += i
    return hasil

def perkalian(*args):
    """
    Docstring for perkalian
    
    :param args: Description
    """
    hasil = 1

    for i in args:
        hasil *= i
    return hasil

def pangkat(n):
    """
    Docstring for pangkat
    
    :param n: Description
    """
    return lambda angka: angka ** n