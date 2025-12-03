## Pengenalan String

#Cara Buat string

data = "Isi Data String" # Ini Adalah string
print(data)
print(type(data))

print("\n======SINGLE QUOTE ('')======")
data = 'String Yang Menggunakan Single Quote'
print(data)

print('\n======DOUBLE QUOTE ("")======')
data = "String Yang Menggunakan Double Qoute" 
print(data)

print('\n======GABUNGAN SINGLE & DOUBLE QUOTE ('')======')
print('"Menggunakan Single Quote Yg Di Dalamnya Terdapat Double Quote"')
print("'Menggunakan Double Quote Yg Didalamnya Terdapat Single Quote'")
print("Sekarang Adalah Hari Jum'at") 

# Menggunakan Tanda Backlash(\)
# Membuat Tanda Single Quote Tanpa Penutup Menjadi String Dengan Tanda (\)
print("\n======BLACKLASH UNTUK SINGLE QUOTE (')======")
print('Waktunya Sholat Jum\'at')
print('Ba\'da Shubuh Membaca Al-Qur\'an')

# Membuat Tampilan Storage Dalam String Yg Terdapat Tanda Backlash
# Menambahkan Tanda Backlash Satu Lagi Di Samping Tanda Backlash Storage
print("\n======BLACKLASH UNTUK BLACKLASH======")
print("C:\\Lokal\\User\\user")

# Menggunakan Tanda Tab / Tanda (\t)
# Tanda (\t) Berfungsi Sebagai Penambah Spasi / Menjauhkan Jarak Antar Huruf Sebelumn Dan Setelahnya
print('\n======TAB======')
print("Hobi\tSaya Programmer")

# Menggunakan Tanda Backspace (\b)
# Tanda (\b) Berfungsi Sebagai Menghapus Satu Huruf Atau Satu Spasi Sebelumnya
print('\n======BACKSPACE======')
print("Hobi\bsaya Programmer")

# Menggunakan Tanda Newline (\n)
# Tanda (\n) Berfungsi Sebagai Membuat Garis Baru
print('\n======NEW LINE======')
print("Saya Adalah Orang Biasa\nHobi Saya Adalah Menjadi Programmer")

#  Menggunakan Tanda String Literal / RAW
print('\n======RAW======')
print('C:\new folder') # Akan Salah Pathnya Karna ada Tanda (\n) Yg Bergabung Dengan String
# Caranya Menggunakan RAW String Atau Tanda (r) Sebelum Tanda Quote
# Tanda (r) Sebelum Tanda Quote Berfungsi Agar Semua Karakter Yg Didalam Tanda Quote Setelahnya Menjadi Karakter String Semua
print(r"C:\new folder")

# Menggunakan Tanda Multiline Literal String Yaitu tanda Single Quote 3 Pasang (''' ''') / Tanda Double Quote 3 Pasang (""" """) 
# Tanda (''' ''') / (""" """) Berfungsi Agar Tata letak Karakter Di Tulis Sesuai Dengan Yg DiTampilkan
print("\n======SINGLE 3 PASANG / DOUBLE QUOTE 3 PASANG======")
print("""
Nama : Wong Ganteng
Hobi : Programmer
""")
# Bisa Juga Digabung Dengan Raw
print('\n=====GABUNGAN 3 PASANG SINGLE / DOUBLE DENGAN DENGAN RAW (r)=====')
print("""
Nama : Wong Ganteng
Hobi : Programmer
Website : www.wongganteng.co/newid
""")












