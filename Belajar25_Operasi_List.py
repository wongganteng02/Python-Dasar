## Operasi List

# Urutan Index Dari Depan Dimulai Dari 0
# Jika Diurutkan Dari Belakang dimulai Dari -1
print("\n=====MENGAMBIL SEMUA DATA TANPA TANDA BACA=====")
data = ["PT","Tirta","Fresindo","Jaya"]
print(" ".join(data))

# Mengambil Data Dari List
print("\n=====MENGAMBIL DATA DALAM LIST=====")
data_awal = data[0]
data_akhir = data[-1]
print(f"Data Pertama Dgn Index 0 Adalah: {data_awal}")
print(f"Data Pertama Dgn Index 3 Adalah: {data_akhir}")

# Menghitung Jumlah Data Dalam List
print("\n=====MENGHITUNG JUMLAH DATA DALAM LIST=====")
panjang_data = len(data)
print(f"Panjang Data = {panjang_data}")


## Manpulasi / Merubah Data List

# Menambahkan Data Dalam List Sesuai Posisi Tanpa Merubah Data Lain
print("\n=====MENAMBAHKAN DATA SESUAI DENGAN POSISI=====")
print(f"Data Sebelum Ditambahkan: {data}")
data.insert(1,"Abadi")
print(f"Data Sesudah Ditambahkan: {data}")

# Menambahkan Di Urutan Paling Akhir
print("\n=====MENAMBAHKAN DATA PALING AKHIR=====")
data.append("Kusuma")
print(f"Data Ditambahkan Urutan Paling Akhir: {data}")

# Menambahkan List Dengan List
print("\n=====MENGGABUNGKAN ANTAR LIST=====")
data_baru = ["ASIA","RAYA"]
data.extend(data_baru)
print(f"List Data Gabungan: {data}")

# Merubah Data Dengan Menggantikan Posisi Data Lain
print("\n=====MERUBAH DATA BESERTA MENGGANTI POSISI DATA=====")
data[2] = "Surya"
print(f"Perubahan Data: {data}")

# Meremove Data Dalam List
# Data Yg diremove Harus Sama Besar Kecilnya Huruf
print("\n=====REMOVE DATA=====")
print(f"Data Sebelum Di Remove: {data}")
data.remove("ASIA")
print(f"Data Sesudah Di Remove: {data}")

# Melihat Data Paling Akhir Yg Di Remove
print("\n=====REMOVE DATA PALING AKHIR=====")
data_akhir = data.pop()
print(f"Melihat Data List Paling Akhir Yg Diremove: {data_akhir}")
# Meremove Data List Paling Belakang
print(f"Hasil Remove Data List Paling Belakang: {data}\n")