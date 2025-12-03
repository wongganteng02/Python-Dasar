## SOAL ELSE
'''
Dalam kimia, pH adalah skala yang digunakan untuk menentukan tingkat keasaman atau kebasaan suatu cairan.

Buat program file.py yang memeriksa apakah tingkat pH bersifat dasar, asam, atau netral.

Pertama, buat ph variabel dan minta pengguna untuk memasukkan nilai antara 0 dan 14.

Tuliskan sebuah pernyataan if, elif, else yang:

Jika ph lebih besar dari 7, keluarkan "Dasar".
Jika ph kurang dari 7, keluarkan "Asam".
Jika tidak, keluarkan "Netral".
'''

ph = int(input("Masukkan Nilai 0-14 = "))

if ph > 7: # Kondisi 1
  print('Dasar')
elif ph < 7: # Kondisi 2
  print('Asam')
else: # Kondisi Yg Salah / Kondisi Selain Kondisi 1 Dan Kondisi 2
  print('Netral')


## PENJELASAN ELIF
'''
elif = else if 
Ditambahkan Secara Optional Diantara if dan else
Memberikan Kondisi Tambahan Yg Perlu Diperiksa
Terkadang 2 Pernyataan Seperti if dan else saja Tidak Cukup

Dan elif Bisa Ditambahkan Beberapa Kali
Tapi Yg Dieksekusi Tetap Hanya 1 Yaitu Yg Sesuai Dgn Kondisi Awal
'''


print("\n=====PROGRAM KALULATOR SEDERHANA=====\n")
angka1 = float(input('Masukan Angka Pertama: '))
operator = input('Masukan Operator Perhitungan (+,-,*,/) : ')
angka2 = float(input('Masukan Angka Kedua: '))

if operator == '+':
    hasil = angka1 + angka2
    print(f'hasilnya Adalah = {hasil}')
elif operator == '-':
    hasil = angka1 - angka2
    print(f'hasilnya Adalah = {hasil}')
elif operator == '*':
    hasil = angka1 * angka2
    print(f'hasilnya Adalah = {hasil}')
elif operator == '/':
    hasil = angka1 / angka2
    print(f'hasilnya Adalah = {hasil}')

else:
   print('\nSalah Goblok, Kamu Bodoh Sekali😂')