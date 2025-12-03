# Operasi Logika (BOOLEAN)

# not, or, and, xor

## "not" Adalah Kebalikan Dari Nilai Awal Boolean
print("====NOT====")
a = False
b = not a
print("Data a Tanpa  (not) Adalah = ", a)
print("Data b Dengan (not) Adalah = ", b)

## "or" Adalah Khusus Jika Salah Satu Ada True Maka Hasilnya True
# Tapi Jika False Dgn False, Maka Hasilnya Akan False
print("====OR====")
a = True
b = True
c = a or b
print(a," OR",b," =",c)
a = False
b = True
c = a or b
print(a,"OR",b," =",c)
a = True
b = False
c = a or b
print(a," OR",b,"=",c)
a = False
b = False
c = a or b
print(a,"OR",b,"=",c)


## "AND" Adalah Jika Salah Satu Ada False Maka Hasilnya False
# Tapi Jika True Dgn True, Maka Hasilnya Akan True
# Kebalikan Dari (OR) 
print("===AND====")
a = True
b = True
c = a and b
print(a," AND",b," =",c)
a = False
b = True
c = a and b
print(a,"AND",b," =",c)
a = True
b = False
c = a and b
print(a," AND",b,"=",c)
a = False
b = False
c = a and b
print(a,"AND",b,"=",c)


## Sebenarnya "XOR" ITU Bukan termasuk Operasi Logika Tapi Operasi Bitwice,Bisa Dipakai Disini
# Jadi Tidak Menggunakan Kata "xor" Tapi Menggunakan Tanda Ini ^
# "XOR" Adalah Jika Berbeda "True Dengan False" Atau "False Dengan True" Maka Hasilnya True
# Tapi Jika Sama "True Dengan True" Atau "False Dengan False", Maka Hasilnya Akan False
print("===XOR====")
a = True
b = True
c = a ^ b
print(a," XOR",b," =",c)
a = False
b = True
c = a ^ b
print(a,"XOR",b," =",c)
a = True
b = False
c = a ^ b
print(a," XOR",b,"=",c)
a = False
b = False
c = a ^ b
print(a,"XOR",b,"=",c)


