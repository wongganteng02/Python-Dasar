# a = 10, a adalh variabel dengan nilai 10

# type data: Angka berapapun Yang tidak ada komanya (integer)
a = 1
print("data : ", a)
print("- bertipe : ", type(a))

# type data: angka berapapun dengan koma (float)
data_float = 1.7
print("data : ", data_float)
print("- bertipe : ", type(data_float))

# type data: kumpulan semua karakter didalam tanda petik 2 ("") (string)
data_string ="saya beli beras 1,5 kg"
print("data :", data_string)
print("- bertipe : ", type(data_string))

#type data: biner true/false (boolean)
data_bool = False
print("data : ", data_bool)
print("- bertipe : ", type(data_bool))

## type data khusus (Optional Untuk Pemula)

# type data bilangan kompleks
data_complex = complex(7+10)
print("data : ", data_complex)
print("- bertipe : ", type(data_complex))

# type dari bahasa C Dengan mengimpor
# Type Data double Dari Bahasa C, Diimpor Pakai Library Python Yaitu ctypes
from ctypes import c_double

data_c_double = c_double(15.3)
print("data : ", data_c_double)
print("- bertipe : ", type(data_c_double))