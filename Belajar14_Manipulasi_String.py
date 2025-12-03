# Operasi Manipulasi String

# 1. Menyambung String (concatenate)
# Menyambung Dengan Dengan Tanda (+) Dan Tanda " " Untuk Spasi Antar Setiap Kata
nama_pertama = "Deri"
nama_tengah = "Kusuma"
nama_akhir = "Wardani"

nama_lengkap = nama_pertama + " " + nama_tengah + " " + nama_akhir
print(nama_lengkap)

# 2. Menghitung Panjang String / Ada Berapa Karakter Didalam (nama_lengkap)
# Spasi Tetap Dihitung
# str() Tanda Ini Berfungsi Agar Hasil Yg Berupa Number Menjadi Bersifat Karakter
# Dihitung Dari Angka 1
# Menggunakan Assigment len()
panjang = len(nama_lengkap)
print("Ada Berapa Karakter Dari String (" + nama_lengkap + ") = " + str(panjang))


# 3. Operator Untuk String "in" (Apakah Ada)
# Mengecek Apakah Ada Komponen Char(Character) String Di Dalam String
# K (Kus) 
# in (Didalam) 
# nama_lengkap (Deri Kusuma Wardani) 
# Hasil = "True" Karna Huruf "K" Di String (Kus) Memang Huruf Kapital / Uppercase
K = "Kus"
status = K in nama_lengkap
print("Apakah Ada String (" + K + ") Di Dalam String (" + nama_lengkap + ") = " + str(status))


# 4. Operator String "not in" (Apakah tidak Ada)
# Besar Kecil Huruf Sanga Berbeda
# k=(kus) 
# not in (Tidak Didalam) 
# nama_lengkap (Deri Kusuma Wardani)
# Hasil = "True" karna Huruf "k" Di String (kus) Memang Tidak Ada Kata (kus) Dengan Huruf "k" kecil / Lowercase
k = "kus"
status = k not in nama_lengkap
print("Apakah Ada String (" + k + ") Di Dalam String (" + nama_lengkap + ") = " + str(status))


# 5. Mengulang String
# Bisa langsung Di Print Tanpa Input
# Bisa dibalik, * Dulu Baru String " "
print("ha"*7)
print(" Betul"*3)


# 6. indexing Per Karakter / Mengecek Karakter Dari Urutan Ke 0 (Hanya Untuk 1 Karakter Dan Tidak Minus)
# Menggunakan Tanda [] Untuk Tempat 
print("Index Ke 0 : " + nama_lengkap[0])
print("Index Ke 1 : " + nama_lengkap[1])
# Jika Ke Minus Contoh (-1) Adalah Mengambil Karakter String Dari Belakang
print("Index Ke -1 Adalah : " + nama_lengkap[-1])
print("Index Ke -2 Adalah : " + nama_lengkap[-2])


# 7. indexing Semua Karakter / Mengecek Beberapa Karakter
#    Dengan Dilebihkan 1 Urutan
# Tanda (:) Artinya Adalah Sampai
print("index Ke 0-4 Adalah : " + nama_lengkap[0:4])
print("index Ke 5-11 Adalah : " + nama_lengkap[5:12])


# 8. indexing Dengan Kelipatan / Tanda 
#    Contoh [0:19:3] Artinya Dari Urutan 0 Sampai Urutan Ke 19 Dengan Keliatan 3
print("index Ke Kelipatan 0,3,6,9,12,15.18 Adalah : " + nama_lengkap[0:19:3])
print("index Ke Kelipatan 4,8,12,16 Adalah : " + nama_lengkap[4:19:4])


# 9. Code Huruf / ASCI CODE Huruf Uppercase > Lowercase
#    Jadi Setiap Karakter Memiliki Ascii Code Yg Berupa Angka
#    item Paling Kecil / Sesuai Ascii Code 
print("item Paling Kecil Adalah : " + min(nama_lengkap))
#    item Paling Besar / Sesuai Ascii Code
print("item Paling Besar Adalah : " + max(nama_lengkap))


# 10. Mengecek Ascii Code Per Karakter Menggunakan Assigment ord("") 
#     Jika Hasil Berupa Number Maka Harus Menambahkan str()
ascii_code = ord(" ")
print("ASCII Code Spasi itu Berapa : " + str(ascii_code))
#     chr() Untuk Cek Karakter Dari Ascii Code Random
character = 111
print("Karakter Yg ASCII Codenya 111 adalah : " + chr(character))


# 11. Operator Dalam Bentuk Method Bukan Dari Function Python
data = "Deri Kusuma Wardani"
jumlah = data.count("i")
print("Jumlah Huruf i Didalam String (" + data + ") Adalah = " + str(jumlah))

