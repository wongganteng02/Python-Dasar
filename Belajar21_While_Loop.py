## WHILE LOOP (PERULANGAN)

'''
print Akan dicetak berulang kali Jika Nilai Awal Tidak Disimpan
Dengan Cara Ditambahkan 1 Setiap Perulangan, Sampai Kondisi While 
Tidak Sesuai.
Sehingga Pengulangan Akan Berhenti / Melewati While
'''
num = 0
print(num)

while num < 3:
    num += 1 # Bisa Juga angka = +1
    print(f'Alamak Gantengnyo😍')


## SOAL LATIHAN WHILE
print('\n====LATIHAN CREATE PIN BANK====\n')
print('''Buatkan Program Agar Pengguna Memasukkan Pin 4 Digit
Dengan 3 kali Percobaan      
''')
print('BANK JATIM')

pin = int(input('Enter your PIN: '))
kesempatan = 1

while pin != 1010 and kesempatan < 3:
  kesempatan += 1
  pin = int(input('Incorrect PIN. Enter your PIN again: '))

if pin == 1010:
  print('PIN accepted!')

else:
   print('Kesempatan Anda Telah Habis')