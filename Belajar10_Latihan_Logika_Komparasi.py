# latihan Operasi Logika Dan Operasi Komperasii

## Membuat Gabungan Area Rentan Dari Angka

## +++++++3-------10+++++++
print("\n",10*"=","\n")
inputUser = float(input("Masukkan Angka Yang Bernilai\nKurang Dari 3\nAtau\nLebih Dari 10\n :"))

## (KOMPARASI)
# 3--------
# Memeriksa Apakah Angka Yg Dimasukkan Kurang Dari 3
iskurangdari = (inputUser < 3)
print("Kurang Dari 3 = ",iskurangdari)

## (KOMPARASI)
# ------10+++++
# Memeriksa Apakah Angka Yg Dimasukkan Lebih Dari 10
islebihdari = (inputUser > 10)
print("Lebih Dari 10 = ",islebihdari)

## (LOGIKA)
# +++++3-----10+++++
# Digabungkan Dari Hasil Yang Diperiksa
# Jika Angka Yang Dimasukkan Kurang Dari 3 Atau Lebih Dari 10 Maka Hasilnya akan "True"
# jika Sebaliknya Angka Yang Dimasukkan Lebih Dari 3 atau Kurang dari 10 Maka hasilnya akan "False"
# "or" Adalah Jika Salah Satu Nilai Keyword Adalah "True" Maka Hasilnya "True"
# Namun Sebaliknya Jika Salah Satu Nilai Keyword Tidak ada Yg "True" Maka Hasilnya "False"
isCorrect = iskurangdari or islebihdari
print("Is Correct Adalah = ", isCorrect)

## ------3++++++10------
# Angka 3 Yang Beirisan Dengan Angka 10
print("\n",10*"=","\n")
inputUser = float(input("Masukkan Angka Yang Bernilai\nLebih Dari 3\nAtau\nKurang Dari 10\n :"))

# -------3++++++
islebihdari = (inputUser > 3)
print("Lebih Dari 3 = ",islebihdari)

# +++++++10-----
iskurangdari = (inputUser < 10)
print("Kurang dari 10 = ",iskurangdari)

## ----3+++++++10----
# Digabungkan Dari Hasil Yang Diperiksa Secara Beririsan
# Jika Angka Yang Dimasukkan Lebih Dari 3 Atau Kurang Dari 10 Maka Hasilnya akan "True"
# jika Sebaliknya Angka Yang Dimasukkan Kurang Dari 3 atau Lebih dari 10 Maka Hasilnya akan "False"
# "and" Adalah Jika Salah Satu Nilai Keyword Adalah "False" Maka Hasilnya "False"
# Namun Sebaliknya Jika Salah Satu Nilai Keyword Tidak ada Yg "False" Maka Hasilnya "False"
isCorrect = iskurangdari and islebihdari
print("Is Correct Adalah = ", isCorrect)










