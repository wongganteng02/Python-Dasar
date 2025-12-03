## Teknik Menduplikat List

print("\n=====LIST AWAL=====")
a = ['Deri','Kusuma','Wardani']
print(f"a = {a}")
b = a # ini pass by reference / memberi referensi data yg sama dengan variabel yg berbeda
print(f"b = {b}")


# Merubah member dari a Dengan angka index didalam list
# Dan ini akan Merubah Kedua List (Kalu Dirubah Dgn Cara ini maka yg lain ikut berubah)
a[1] = "Raden"
b.sort # b = Mengurutkan List a dari Hurus A - Z
print(f"a = {a}")
print(f"b = {b}")

# Cek Addres, Apakah Sama?
print(f"Addres a = {hex(id(a))}") # Addres a Sama Dengan Addres b
print(f"Addres b = {hex(id(b))}") # Addres b Sama Dengan Addres a

# Menduplikat list Dengan Copy
# Agar Tidak Merubah atau Sama Addresnya Dengan List Sebelumnya
print("\n=====DUPLIKAT LIST=====")
c = a.copy() # full duplikat / list data baru

print(f"Hasil Duplikat = {c}\n")

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")

print(f"Addres a = {hex(id(a))}") # Addres a Sama Dengan Addres b
print(f"Addres b = {hex(id(b))}") # Addres b Sama Dengan Addres a
print(f"Addres c = {hex(id(c))}") # Hasilnya Tidak Sama Dgn addres a, meskipun Listny Sama 

# Memodifikasi Data Dari Hasil List Yg Duplikat

print("\n=====MODIF DATA LIST DUPLIKAT=====")
c[2] = "Amangkurat"

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")