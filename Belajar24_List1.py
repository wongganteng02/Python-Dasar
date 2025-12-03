## --- LIST ---

# Kumpulan Data Dalam Bentuk Numbers
data_angka = [1,2,3,4,5] # Outputnya Akan Sama Persis Dengan Value dari Variable (data_angka)
print(data_angka) # Jadi Hasilnya Bukan Berbentuk List Meskipun Menggunakan Tanda List

# Kumpulan Data Dalam Bentuk String
data_string = ['Deri','Kusuma','Wardani'] # Outputnya Akan Sama Persis Dengan Value dari Variable (data_angka)
print(data_string) # Jadi Hasilnya Bukan Berbentuk List Meskipun Menggunakan Tanda List

# Kumpulan Data Dalam Bntuk Boolean
data_bool = [False,True,True,False] # Outputnya Akan Sama Persis Dengan Value dari Variable (data_angka)
print(data_bool) # Jadi Hasilnya Bukan Berbentuk List Meskipun Menggunakan Tanda List

# Kumpulan Data Dalam Bentuk Campuran
data_campuran = [2,"WONG","GANTENG",True,12] # Outputnya Akan Sama Persis Dengan Value dari Variable (data_angka)
print(data_campuran) # Jadi Hasilnya Bukan Berbentuk List Meskipun Menggunakan Tanda List


## Cara Alternatif Membuat List Dengan range
# Jika Menggunakan range Defaultnya Listnya Akan Mengurangi Satu Nilai Akhir
data_range = range(1,5) # Outputnya Akan Sama Persis Dengan Value dari Variable (data_angka) Bukan Berbentuk List
data_list = list(data_range) # list akan Merubah / Mengconvert Value Variable Menjadi Bentuk List Dalam Satu Baris
# Bisa Juga Hanya 1 Baris Dengan Code: list(range(1,5))Hasilnya Sama Saja
print(data_list)

## Membuat List Dengan For Loop
# range(listawal,listakhir,kelipatan)
'''
Perbedaan
[i * 3 for i in range(1,20,2)]                = Bentuk Semua list Dalam Satu Baris
Dengan                          = Operasinya Sama-sama Buat List Bedanya
for i in range(1,20,2):                       = Bentuk Setiap list Dalam Setiap baris
         i = i * 3
'''
data_list_for = [i * 3 for i in range(1,20,2)]
print(data_list_for)

## Membuat List Dengan for Dan if
list_for_if = [i for i in range(1,21,3) if i != 10] 
# if Untuk Mengkhususkan list Dengan Operasi Komparasi Dan Operasi Aritmatika
# Sehingga Outputnya akan Mengecualikan list Tersebut Dan ditampilkan Sesuai Operasi
print(list_for_if)

## Membuat List Dengan for Dan if Menggunakan Operasi Campuran
# Menghasilkan Hanya Angka Genap
list_for_if = [i for i in range(1,20) if i % 2 == 0]
# Artinya = Hanya Menampilkan Angka List Yg Hasil Sisanya / Modulus 2 Dan Yg Hasilnya = 0
print(list_for_if)

## Membuat List Dengan for Dan if Menggunakan Operasi Campuran
# Menghasilkan Hanya Angka Ganjil
list_for_if = [i for i in range(1,20) if i % 2 != 0] 
# Tanpa Menggunakan Operasi != 0 Hasilnya Tetap Sama Yaitu Hanya Menampilkan Ganjil
# Artinya = Hanya Menampilkan Angka List Yg Hasil Sisanya / Modulus 2 Dan Yg Hasilnya != 0 / Selain 0
print(list_for_if)