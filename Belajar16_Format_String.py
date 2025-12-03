# FORMAT STRING

## Fungsi Format Sama Dengan Manipulasi String Dgn Tanda + Bedanya Cuma Lebih Simple Format Daripada Manipulasi /(Concatenate) 
# Contoh Generic / String
nama = "Kusuma"
format_str = f"Deri {nama}" # f sebelum Tanda Petik Adalah Format
# Berarti Yg Di print Dulu Adalah Yg Format Bukan Variable Paling Atas
# Dengan Menambahkan Variable Didalam Tanda "{}"
print(format_str)

# Contoh Boolean
boolean = False
format_str = f"Boolean = {boolean}"

print(format_str)

# Contoh Angka
angka = 500.5
format_str = f"Angka = {angka}"

print(format_str)

# Bilangan Bulat
angka = 20
format_str = f"Angka Bulat = {angka}"

print(format_str)

# Bilangan Ribuan
# Pyton Aka Menyesuaikan Koma Pada Angka Ribuan Atau Jutaan
angka = 500000
format_str = f"Angka Ribuan = {angka:,}" # Tanda "," Artinya "." Dan Sebaliknya

print(format_str)

# Bilangan Desimal (Otomatis)
angka = 700.5
format_str = f"Angka Desimal = {angka:.2f}"
# Tanda "." Untuk Menandai Tanda "." Yg Terdapat Di Angka
# "2" Untuk Berapa Angka Yg Dibalakng Tanda "."
# "f" Adalah Menyalin Format

print(format_str)

# Menampilkan Leading Zero / Angka Didepannya
angka = 700.54321
format_str = f"Angka Leading Zero = {angka:08.3f}"
# .3f Adalah Cetak 3 Angka Yg Dibelakang Tanda "." = 700.543 
# 8 Adalah Urutan Angka Yg Tercetak Termasuk Tanda "." Dan Dilebihkan 1 Untuk Menambahkan 1 Urutan dari Depan Yg Akan Diisi 0
# 0 Adalah Angka Yg Ditambahkan Dari Sisa 1 Urutan Depan Dan (HANYA BISA DISI DENGAN ANGKA 0)

print(format_str)

# Menampilkan Tanda "+" / "-"
angka_minus = -10
angka_plus = -10.54321
format_minus = f"Angka Minus = {angka_minus:+}"
format_plus = f"Angka Plus = {angka_plus:+.3f}"
# Angka Minus Memiliki Tanda Deafault Sendiri Tidak Seperti Angka Plus
# Tanda "+" Berfungsi Untuk Selalu Menampilkan Tanda Minus Dan Plus
# Dan Bisa Digabung Juga Dengan Cara Desimal Jika Angka Adalah Desimal

print(format_minus)
print(format_plus)

# Memformat Persen %
persentase = 0.0234
format_persen = f"Format Persen = {persentase:.3%}"
# 
# Karna 0 Didepan Tidak Ada Nilainya Jadi Yg Terhitung Hanya 234
# Dan 3 Angka Dibelakang Tanda "." Jika Tidak Cukup Maka Ditambahkan 0 Dibelakangnya

print(format_persen)

# Melakukan Operasi Aritmatika Didalam Format
harga_diri = 17000
jumlah = 8
format_aritmatika = f"Total Harga = {harga_diri * jumlah:,}"

print(format_aritmatika)

# (OPTIONAL)
# Format Angka Lain (Binary, Octal, Hexadecimal)
angka = 300
format_binary = f"Binary : {bin(angka)}"
format_octal = f"Octal = {oct(angka)}"
format_hex = f"Hex = {hex(angka)}"

print(format_binary)
print(format_octal)
print(format_hex)