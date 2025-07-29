#Cara pembuatan tipe data Dictionary Python
foo = {1: "Belajar", 2: "Python", 3: "di Duniailkom"}
bar = {"mengapa": "Belajar", "apa": "Python", "dimana": "di Duniailkom"}
baz = {1: "Belajar", "apa": "Python", "dimana": "di Duniailkom"}

print(type(foo))
print(type(bar))
print(type(baz))
print("\n")

print(foo)
print(bar)
print(baz)
print("\n")

foo = {1: "Belajar",
       2: ["Pascal", "C", "Python"],
       "website": "Duniailkom",
       "menyerah": False,
       "target": 2022,
       "riwayat_sekolah": {
           "SD": "SDN 3 Hijau Daun",
           "SMP": "SMP 7 Hijau Lumut",
           "SMA": "SMAN 8 Hijau Rumput"}
       }

print(foo)
print("\n")

#Cara mengakses element Dictionary Python
foo = {"kegiatan": "Belajar Python", 
       "website": "Duniailkom", 
       "hasil": "Yakin bisa!" }

print(foo["website"])
print("\n")

#Cara mengubah element Dictionary Python
foo = {"kegiatan": "Belajar Python", 
       "website": "Duniailkom", 
       "hasil": "Yakin bisa!" }

foo["kegiatan"] = "Belajar Bahasa Pemrograman"
print(foo)
print("\n")

#Cara menambah element Dictionary Python
foo = {"kegiatan": "Belajar Python", 
       "website": "Duniailkom", 
       "hasil": "Yakin bisa!" }

foo["target"] = 2020
print(foo)
print("\n")

#Cara menghapus element Dictionary Python
foo = {"kegiatan": "Belajar Python", 
       "website": "Duniailkom", 
       "hasil": "Yakin bisa!" }

del foo["kegiatan"]
print(foo)
print("\n")

#Pembuatan Dictionary dengan constructor dict()
foo = dict ( kegiatan = "Belajar Python",
             website = "Duniailkom",
             hasil = "Yakin bisa!" )

print(foo)
