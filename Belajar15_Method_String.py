# Operator Dalam Bentuk Method
## Merubah Case dari String
# Merubah Semua String Menjadi Uppercase

print("\n====UPPER DAN LOWER====")
contohupper_normal = "bro!"
print("Normal = " + contohupper_normal)
contoh1_uppercase = contohupper_normal.upper()
print("Upper = " + contoh1_uppercase)

# Merubah Semua String Menjadi Lowercase
contohlower_normal = "HAY BRO!"
print("Normal = " + contohlower_normal)
contoh2_lowercase = contohlower_normal.lower()
print("Lower = " + contoh2_lowercase)

## Pengecekan isX Method
# Contoh Pengecekan, Apakah Semua Karakter String Adalah Lowercase / Uppercase
print("\n====IS LOWER DAN IS UPPER====")
contohcek = "hai sayanag"
apakah_lower = contohcek.islower() # Hasilnya boolean Jadi Harus Casting ke "str"
print(contohcek + " is lower = " + str(apakah_lower))
apakah_upper = contohcek.isupper() # Hasilnya boolean Jadi Harus Casting ke "str"
print(contohcek + " is upper = " + str(apakah_upper))

# isalpha() ---> Untuk Mengecek Apakah Karakter String Semuanya Huruf
# isdecimal() ---> Untuk Mengecek Apakah Karakter String Semuanya Angka
# isalnum() ---> Untuk Mengecek Apakah Karakter String Terdiri dari Huruf Dan Angka
# isspace() ---> Untuk Mengecek Apakah Karakter String Memiliki Spasi, Tab \t, Newline \n
# istitle() ---> Untuk Mengcek Apakah Semua Kata Di Karakter String itu Dimulai Dengan Huruf Kapital

## Contoh Cek istitle()
print("\n====IS TITLE====")
judul = "Aku Cinta Kamu"
cek_judul = judul.istitle()
print(judul + " is title = " + str(cek_judul))

## Mengecek Komponen startswith() Dan endswith()
print("\n====START DAN END====")
cek_start = "Kulo Tresno Jenengan dek!".startswith("Kulo Tresno")
print("start = " + str(cek_start))
cek_end = "Kulo Remen Kale Jenengan".endswith("Kale Jenengan")
print("end = " + str(cek_end))

## Penggabungan Komponen join() Dan split()
# .jon() ---> Untuk Menggabungkan Kata String Yg Berupa List / Yg Terdapat Di Dalam Tanda []
print("\n====JOIN DAN SPLIT====")
pisah = ["Cinta","Itu","Buta"]
digabung_koma = ", ".join(pisah)
print(pisah)
print(digabung_koma)

digabung_spasi = " ".join(pisah)
print(digabung_spasi)

gabung = " huwek ".join(pisah)
print(gabung)

# .split() ---> Untuk Mengembalikan Seperti Awal Lagi Y Berupa List
gabung = "Cinta huwek Itu huwek Buta".split("huwek")
print(gabung)

# Alokasi Karakter rjust(), ljust(), center()
print("\n====KIRI TENGAH KANAN====")
print(5*"=" + "Data" + "="*5)

# Menempatkan kata ke kanan Dengan Jarak 20 Urutan Dari Dalam Tanda Petik 2 ''
rata_kanan = "Kanan".rjust(20)
print("'"+rata_kanan+"'")

# Menempatkan kata ke kiri Dengan Jarak 20 Urutan Dari Dalam Tanda Petik 2 ''
rata_kiri = "Kiri".ljust(10)
print("'"+rata_kiri+"'")

# Menempatkan kata ke Tengah Dengan Jarak 30 Urutan Dari Dalam Tanda Petik 2 ''
rata_tengah = "Tengah".center(30)
print("'"+rata_tengah+"'")

# Menempatkan kata ke Tengah Dengan Jarak 30 Urutan Dari Dalam Tanda Petik 2 ''
rata_tengah = "Tengah".center(30,"=")
print("'"+rata_tengah+"'")

## .strip() ---> Kebalikan Dari .rjust .ljust .center / Mengembalikan Karakter Yg Normal
# Menghapus Alokasi
print("\n====STRIP====")
kanan = rata_kanan.strip(" ")
print("'"+kanan+"'")
kiri = rata_kiri.strip(" ")
print("'"+kiri+"'")
tengah = rata_tengah.strip("=")
print("'"+tengah+"'")

# .capitalize() ---> Untuk Huruf Awal Kata Menjadi Upper / Huruf Kapital
print("\n====CAPITALIZE====")
a = "hay sayang!"
b = a.capitalize()
print(a)
print(b)

