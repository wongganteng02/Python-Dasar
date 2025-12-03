# Operasi Aritmatika

#  +, -, *, /, **, %, //, ().

a = 14
b = 4

## Operasi Penambahan
hasil_penambahan = a + b 
print(a,'+',b,'=',hasil_penambahan)

## Operasi Pengurangan
hasil_pengurangan = a - b 
print(a,'-',b,'=',hasil_pengurangan)

## Operasi Perkalian Dgn Tanda (*) Bukan Tanda (x)
hasil_perkalian = a * b
print(a,'*',b,'=',hasil_perkalian)

## Operasi Pembagian Dgn Tanda (/)
hasil_pembagian = a / b
print(a,'/',b,'=',hasil_pembagian)

## Operasi Eksponen/Pangkat Dgn Tanda (**)
# Artinya "a" Dipangkatkan "b"
hasil_pangkat = a ** b
print(a,'**',b,'=',hasil_pangkat)

## Operasi Modulus Adalah Sisa Dari Angka Yg Bisa Dibagikan
# Menggunakan Tanda (%)
hasil_modulus = a % b
print(a,'%',b,'=',hasil_modulus) 

## Operasi Floor Division Adalah Berapa Angka Yg Bisa Dibagikan/ Kebalikan Dari (Modulus)
# Menggunakan Tanda (//)
hasil_floor_division = a // b
print(a,'//',b,'=',hasil_floor_division)

## Prioritas Operasi, Operational Predence
# Perhitungan Yg Lebih Didahulukan Adalah :
# 1. Yang Didalam Kurung ()
# 2. Eksponen/Angka Yg Di Pangkatkan
# 3. Perkalian, Pembagian, Modulus, Floor Division
# 4. Pertambahan, Pengurangan
c = 11
d = 7
f = 9
hasil = c ** (d - f) // c * d / f % c + d
print(c,'**','(',d,'-',f,')','//',c,'*',d,'/',f,'%',c,'+',d,'=',hasil)
