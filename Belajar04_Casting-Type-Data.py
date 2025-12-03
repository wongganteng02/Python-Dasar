# Belajar Casting/Konversi Type
# Merubah Dari satu Type Data Ke Type data Yg Lain
# type Data = int, str, float, bool

## Merubah Type data (INTEGER) --> (INTEGER, FLOAT, STRING, BOOL)
print("======INTEGER======")
a_int   = 0
a_float = float(a_int) # Artinya Variabel (a_float) Menggunakan type data (FLOAT) Dgn Value (9) dari type data (INTEGER) 
a_str   = str(a_int) # Artinya Variable (a_str) Menggunakan type data (STRING) Dgn Value (9) dari type data (INTEGER)
a_bool  = bool(a_int) # Artinya Variable (a_bool) Menggunakan type data (BOOL) Dgn Value type data (INTEGER)

# Artinya Cetak. Data =  Value Yg Sudah Diubah type datanya Dari Variable Sebelumnya, Type Data = type data Value  
print("Data = ", a_int, ",Type Data =", type(a_int)) 
print("Data = ", a_float, ",Type Data =", type(a_float)) # Value akan Bertambah ",0" Jika Value (INTEGER)/(a_int) Adalah Angka Satuan Tanpa Koma
print("Data = ", a_str, ",Type Data =", type(a_str)) 
print("Data = ", a_bool, ",Type Data =", type(a_bool)) # Value akan "True" Jika Value (INTEGER)/(a_int) Adalah Angka Selain "0"



## Merubah Type data (FLOAT) --> (FLOAT, INTEGER, STRING, BOOL)
print("======FLOAT======")
b_float = 9.9
b_int   = int(b_float)
b_str   = str(b_float)
b_bool  = bool(b_float)

print("Data = ", b_float, ",Type Data =", type(b_float))
print("Data = ", b_int, ",Type Data =", type(b_int)) # Value Akan Dibulatkan Ke Angka Pertama Sebelum (,) Menjadi Angka Satuan
print("Data = ", b_str, ",Type Data =", type(b_str))
print("Data = ", b_bool, ",Type Data =", type(b_bool)) # Value akan "True" Jika Value (FLOAT)/(b_float) Adalah Angka Selain "0" 
# Dan akan "False" Jika Value (FLOAT)/(b_float) Adalah Angka "0"



## Merubah Type data (BOOLEAN) --> (BOOL, INTEGER, FLOAT, STRING)
print("======BOOLEAN======")
c_bool  = True
c_int   = int(c_bool)
c_float = float(c_bool)
c_str   = str(c_bool)

print("Data = ", c_bool, ",Type Data =", type(c_bool)) # Value type data "bool" Harus (True/false)
print("Data = ", c_int, ",Type Data =", type(c_int)) # Value Dibulatkan Ke Atas/Angka Satuan Bukan Turun/Minus
print("Data = ", c_float, ",Type Data =", type(c_float)) # Value akan Membulatkan Ke Angka Satuan Dengan Tambahan ",0" Menjadi "1,0" 
print("Data = ", c_str, ",Type Data =", type(c_str)) # Value (str) Tetap Sama Karna Berupa Teks



## Merubah Type data (STRING) --> (STRING<, INTEGER, FLOAT, BOOL)
print("======STRING======")
d_str   = "9" 
d_int   = int(d_str)
d_float = float(d_str)
d_bool  = bool(d_str)

print("Data = ", d_str, ",Type Data =", type(d_str)) # JIka (STRING) Tidak Diubah Type Datanya Maka Valuenya Bisa Menggunakan Semua Karakter
print("Data = ", d_int, ",Type Data =", type(d_int)) # Value (STRING) Harus Berupa Angka, Tidak Boleh Ada Huruf 
print("Data = ", d_float, ",Type Data =", type(d_float)) # Value (FLOAT) Harus Berupa Angka, Tidak Boleh ada Huruf
print("Data = ", d_bool, ",Type Data =", type(d_bool)) # Value (BOOL) Hanya Bisa "False" Jika Value (STRING) Tidak Di isi 