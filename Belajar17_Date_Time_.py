# Date And Time

import datetime as dt # impor library datetime Dengan Atribut dt

hari_ini = dt.date.today()
print("")
print(hari_ini)
print(f"Hari ini Adalah, Hari: {hari_ini:%A}\n") # (%A) --> Menampilkan Hari Dengan Bahasa Inggris

hari_lahir = dt.date(2005,12,2)
print(hari_lahir)
print(f"02-12-2005 Adalah Hari: {hari_lahir:%a}\n") # (%a) --> Menampilkan Hari Dalam Bentuk Singkatan nama Hari, Contoh Minggu = sun

hari_lahir_mantan = dt.date(2005,9,20)
print(hari_lahir_mantan)
print(f"20-09-2005 Adalah Hari: {hari_lahir_mantan:%w}\n") # (%w) --> Menampilkan Hari Dalam Bentuk Angka, Dimulai Hari Minggu = 0


print(5*"="+"PROGRAM DATE TIME"+"="*5)
print("Masukkan Data Lahir Anda!")
date = int(input("Tanggal \t: "))
month = int(input("Bulan \t\t: "))
year = int(input("Tahun \t\t: "))

born = dt.date(year,month,date)
print(f"Data Lahir Anda Adalah Hari: {born:%A}\n")

print(5*"="+"PROGRAM DATE UMUR"+"="*5)
hari_ini = dt.date.today()
age_day = hari_ini - born # Sekarang - Data Lahir = ...days 

age_year = age_day.days // 365 # 1 Tahun = 365 Hari. Jadi Umur Hasil Berupa Hari Flour Division 365 Hari
                               # (.days) --> Berfungsi Menghilangkan Output Default Kata "days" 

age_month = (age_day.days % 365) // 30 # 1 Tahun = 365 Hari. Jadi Umur Hasil Berupa Hari Modulus 365 Hari Terus Di Flour Division 1 Bulan Yaitu 30 Hari
                               # (.days) --> Berfungsi Menghilangkan Output Default Kata "days" 
print(f"Umur Anda Dalm Bentuk Hari Adalah\t\t: {age_day}\n")
print(f"Umur Anda Dalam Bentuk Tahun Adalah\t\t: {age_year} Tahun\n")
print(f"Umur Anda Dalam Bentuk Sisa Bulan Adalah\t: Lebih {age_month} Bulan")


