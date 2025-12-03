
## --DATA LIST--


print("\n=====MENGHITUNG BANYAK DATA ANGKA=====")
data_angka = [1,2,3,2,4,5,3,4,1,8,3,2,6,3,4,4,3]
print(f"Data Berupa Angka: {data_angka}")

# Count Data / Menghitung ada Berapa Data Angka
data_4 = data_angka.count(4)
data_3 = data_angka.count(3)

print(f"Jumlah Data Angka 4 = {data_4}")
print(f"Jumlah Data Angka 3 = {data_3}")


## Menghitung Posisi / Ambil Posisi Data
# Data Pertama Indexnya Dimulai Dari 0 Dan Data Yg Diambil / Dicari Harus Sama Besar Kecilnya Huruf
print("\n=====MENGHITUNG POSISI INDEX DATA=====")
data = ["PT","PADMA","JARKA","ABADI"]
print(f"Data Sebelum Diambil: {data}")

index = data.index("PT")
print(f"Menghitung Index Data Ke Berapa: {index}")
index = data.index("ABADI")
print(f"Menghitung Index Data Ke Berapa: {index}")


## Mengurutkan Data List
# Untuk Data Berupa Angka 
print("\n=====MENGURUTKAN DATA ANGKA=====")
print(f"Data Angka Sebelum Diurutkan: {data_angka}")
data_angka.sort()
print(f"Data Angka Sesudah Diurutkan: {data_angka}")

# Untuk Data Berupa String
print("\n=====MENGURUTKAN DATA STRING=====")
print(f"Data String Sebelum Diurutkan: {data}")
data.sort()
print(f"Data String Sesudah Diurutkan: {data}")

# Membalik Urutan Data Angka
print("\n=====MEMBALIK DATA=====")
data_angka.reverse()
data.reverse()
print(f"Membalik Urutan Data: \n{data_angka}\n{data}")
