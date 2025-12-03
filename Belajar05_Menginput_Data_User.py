# Belajar Mengambil Input Data dari User

## Data Apapun Yg Dimasukan Pasti Type Data (STRING)
# Dibawah ini Syntax Default Input Data Dgn Type Data (STRING) 
data = input("Masukan Data: ")


print("Data = ", data, ",Type =", type(data))



## Merubah/Mencasting Type Input Data Menjadi (INTEGER)
# Artinya Input Data "str"/STRING Harus Dimasukan ke "int"/INTEGER Dgn Tanda Buka Tutup Kurung ()
number_int = int(input("Masukan Angka Satuan: ")) 

# Harus Memasukan Angka Satuan, Tidak Boleh Angka Pecahan Desimal/Angka Dgn Koma (.)
print("Data Angka = ", number_int, ",Type =", type(number_int))



## Merubah/Mencasting Type Input Data Menjadi (FLOAT) 
# Syntax Yg Digunakan (FLOAT) Sama Dgn Syntax (INTEGER) Karna Sama Berupa Angka
# Artinya Input Data "str"/STRING Harus Dimasukan/Dicasting ke "float" Dgn Tanda Buka Tutup Kurung ()
number_float = float(input("Masukan Angka Berapapun: "))

# Harus Memasukan Angka Berapapun, Boleh Angka Dgn Pecahan Desimal/Angka Dgn Tanda Koma (.)
print("Data Angka = ", number_float, ",Type =", type(number_float))



## Merubah/Mencasting Type Input Data menjadi (BOOLEAN)
# Artinya Nilai Bool Hanya akan "False"
# Jika Syntax Input Data "str" Maka Dimasukan/Dicasting ke "int" Terlebih Dahulu Baru Dicasting Lagi ke "bool" Dgn Tanda ()
biner = bool(int(input("Masukan Nilai Bool: ")))

# Harus Angka Satuan Yg Dimasukan, Tidak Boleh Angka Pecahan Desimal/Angka  Dgn Tanda koma (.)
# Setelah itu Nilai Bool akan "True" Jika Yg Dimasukan Adalah Angka Berapun
# Dan Nilai Bool Hnya akan "False" Jika Yg dimasukan adalah Angka "0"
print("Data = ", biner, ",Type Data =", type(biner))
