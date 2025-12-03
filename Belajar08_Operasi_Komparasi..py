# Operasi Komparasi (BOOLEAN)

# >, <, >=, <=, ==, !=, is, is not

x = 7
y = 5

'''
Perbedaan Hasil Antara Lebih Besar/Lebih Kecil Yg Terdapat (<=) / (>=) Dan (<) / (>) Adalah Ketika Angka Yg Dibandingkan itu Nilainya Sama.
Dan Jika Angkanya Sama (5 >= 5) Atau (5 <= 5) Hasilnya "True" Berbeda Dengan Hasil Yg Tidak Memiliki "Sama Dengan" (<) (>)
Karna Perbandingan Yg Memiliki "Sama Dengan" Dimulai Dari Angka Awal Yg Berkoma
Bukan Dimulai Secara Langsung Dari Angka Setelahnya, Hasil "True" Berlaku Di Perbandingan Angka Yg Sama, Dengan 
Menggunakan "Sama Dengan" (<=) (>=).

Untuk Hasil Perbandingan Angka Yg Sama Tanpa Menggunakan "Sama Dengan" Dengan 
Contoh (5 > 5) atau (5 < 5) Hasilnya Akan "False" Karna Perbandingannya Dimulai Dari Angka Setelahnya Jadi Sifat Perbandingannya Itu Normal
Hasil "False" Berlaku Di Perbandingan Angka Yg Sama, Tanpa 
Menggunakan "Sama Dengan" (<) (>)
 
'''


# Nilai (6) Dan (7) Adalah Bilangan Literal/Bilangan Secara Langsung Yg Tidak Ada Variablenya
print("==== LEBIH BESAR ====\n")
hasil = 6 > x
print("Apakah 6 Lebih Besar Dari X = ", hasil)
hasil = 6 > y
print("Apakah 6 Lebih Besar Dari y = ", hasil)
hasil = x > 7
print("Apakah X Lebih Besar Dari 7 = ", hasil)


# Nilai (6) Dan (5) Adalah Bilangan Literal/Bilangan Secara Langsung Yg Tidak Ada Variablenya
print("==== LEBIH KECIL====\n")
hasil = x < 6 
print("Apakah X Lebih Kecil Dari 6 = ", hasil)
hasil = y < 6 
print("Apakah Y Lebih Kecil Dari 6 = ", hasil)
hasil = 5 < y 
print("Apakah 5 Lebih Kecil Dari Y = ", hasil)


# Nilai (6) Dan (7) Adalah Bilangan Literal/Bilangan Secara Langsung Yg Tidak Ada Variablenya
print("==== LEBIH BESAR SAMA DENGAN====\n")
hasil = x >= 6 
print("Apakah X Lebih Besar Sama Dengan 6 = ", hasil)
hasil = y >= 6
print("Apakah Y Lebih Besar Sama Dengan 6 = ", hasil)
hasil = 7 >= x 
print("Apakah 7 Lebih Besar Sama Dengan X = ", hasil)


# Nilai (6) Dan (5) Adalah Bilangan Literal/Bilangan Secara Langsung Yg Tidak Ada Variablenya
print("\n==== LEBIH KECIL SAMA DENGAN====\n")
hasil = y <= 6 
print("Apakah Y Lebih Kecil Sama Dengan 6 = ", hasil)
hasil = 6 <= y 
print("Apakah 6 Lebih Kecil Sama Dengan Y = ", hasil)
hasil = y <= 5 
print("Apakah Y Lebih Kecil Sama Dengan 5 = ", hasil)


# Nilai (5) Dan (6) Adalah Bilangan Literal/Bilangan Secara Langsung Yg Tidak Ada Variablenya
print("==== SAMA DENGAN ====\n")
hasil = x == 6 
print("Apakah X Sama Dengan 6 = ", hasil)
hasil = 5 == y 
print("Apakah 5 Sama Dengan Y = ", hasil)


# Nilai (5) Adalah Bilangan Literal/Bilangan Secara Langsung Yg Tidak Ada Variablenya
print("==== TIDAK SAMA DENGAN ====\n")
hasil = 6 != y 
print("Apakah 6 Tidak Sama Dengan Y = ", hasil)
hasil = x != 7 
print("Apakah X Tidak Sama Dengan 7 = ", hasil)


## (is) Adalah Komparasi Object Identity
# Object Yg Tidak Boleh Ada Bilangan Literal / Angka Secara Langsung
# Perbedaan Dengan "==" / "!=" Dan "is" / "is not" Adalah Yg Didalam (hasil) Dan (print) Harus Huruf / Variable Diatas,
# Yg Memiliki Nilai Berupa Angka
a = 3
b = 4

print("==== SAMA DENGAN (TIDAK MENGUNAKAN BILANGAN LITERAL) ====\n")
hasil = a is b 
print("Nilai A = ",a,",ID = ",hex(id(a))) 
print("Nilai B = ",b,",ID = ",hex(id(b))) 
print("A is B = ", hasil)

print("==== TIDAK SAMA DENGAN (TIDAK MENGUNAKAN BILANGAN LITERAL) ====\n")
hasil = a is not b
print("Nilai A = ",a,",ID = ",hex(id(a))) 
print("Nilai B = ",b,",ID = ",hex(id(b))) 
print("A is not B = ", hasil)