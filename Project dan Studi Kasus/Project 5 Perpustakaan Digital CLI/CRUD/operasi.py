from . import database
from .util import random_string
import time
import os

def create_first_data():
    penulis = input("Penulis: ")
    judul = input("Judul: ")
    while(True):
        try:
            tahun = int(input("Tahun: "))
            if len(str(tahun)) == 4:
                break
            else:
                print("Tahun harus angka, silahkan masukan tahun lagi (yyyy)")    
        except:
            print("Tahun harus angka, silahkan masukan tahun lagi (yyyy)")

    data = database.TEMPLATE.copy()

    data["pk"] = random_string(6)
    data["date_add"] = time.strftime("%Y-%m-%d-%H-%M-%S%z",time.gmtime())
    data["penulis"] = penulis + database.TEMPLATE["penulis"] * " "
    data["judul"] = judul + database.TEMPLATE["judul"] * " "
    data["tahun"] = str(tahun)

    data["penulis"] = data["penulis"][:database.TEMPLATE["penulis"]]
    data["judul"] = data["judul"][:database.TEMPLATE["judul"]]

    data_str = f'{data["pk"]},{data["date_add"]},{data["penulis"]},{data["judul"]},{data["tahun"]}\n'

    try:
        with open(database.DB_NAME,'w',encoding="utf-8") as file:
            file.write(data_str)
    except:
        print("Gagal ceat")

def read(**kwargs):
    try:
        with open(database.DB_NAME, 'r') as file:
            content = file.readlines()
            jumlah_buku = len(content)
            if "index" in kwargs:
                index_buku = kwargs["index"]-1
                if index_buku < 0 or index_buku > jumlah_buku:
                    return False
                else:    
                    return content[index_buku]
            else:
                return content
    except:
        print("Membaca database error")
        return False

def create(tahun, judul, penulis):
    data = database.TEMPLATE.copy()

    data["pk"] = random_string(6)
    data["date_add"] = time.strftime("%Y-%m-%d-%H-%M-%S%z",time.gmtime())
    data["penulis"] = penulis + database.TEMPLATE["penulis"] * " "
    data["judul"] = judul + database.TEMPLATE["judul"] * " "
    data["tahun"] = str(tahun)

    data["penulis"] = data["penulis"][:database.TEMPLATE["penulis"]]
    data["judul"] = data["judul"][:database.TEMPLATE["judul"]]

    data_str = f'{data["pk"]},{data["date_add"]},{data["penulis"]},{data["judul"]},{data["tahun"]}\n'
    
    try:
        with open(database.DB_NAME,'a',encoding="utf-8") as file:
            file.write(data_str)
    except:
        print("Data sulit ditambahkan")

def update(no_buku,pk,data_add,tahun,judul,penulis):
    data = database.TEMPLATE.copy()

    data["pk"] = pk
    data["date_add"] = data_add
    data["penulis"] = penulis + database.TEMPLATE["penulis"] * " "
    data["judul"] = judul + database.TEMPLATE["judul"] * " "
    data["tahun"] = str(tahun)

    data["penulis"] = data["penulis"][:database.TEMPLATE["penulis"]]
    data["judul"] = data["judul"][:database.TEMPLATE["judul"]]

    data_str = f'{data["pk"]},{data["date_add"]},{data["penulis"]},{data["judul"]},{data["tahun"]}\n'

    data_len = len(data_str)

    try:
        with open(database.DB_NAME,'r+',encoding="utf-8") as file:
            file.seek(data_len*(no_buku-1))
            file.write(data_str)
    except:
        print("Error dalam update data")

def delete(no_buku):
    try:
        with open(database.DB_NAME,'r') as file:
            counter = 0

            while(True):
                content = file.readline()
                if len(content) == 0:
                    break
                elif counter == no_buku - 1:
                    pass
                else:
                    with open("data_temp.txt",'a',encoding="utf-8") as temp_file:
                        temp_file.write(content)
                counter += 1
    except:
        print("database error")

    os.remove(database.DB_NAME)
    os.rename("data_temp.txt",database.DB_NAME)