# Latihan Fungsi

## Membuat Program Luas Dan Keliling Persegi Panjang

# Jika Program terlalu Panjang Dan Menggunakan Perulangan (while)
# Disarankan Menggunakan Fungsi(def) Untuk Setiap Tugas Program / Memecah Fungsi

'''
import os

while True:
    os.system("cls)
    print(f"{"PROGRAM PERSEGI PANJANG":^45}")
    print(f"{"HITUNG LUAS DAN KELILING😍":^46}")
    print(f"{"="*45:^45}")

    PANJANG = int(input("Masukkan Panjang: "))
    LEBAR = int(input("Masukkan Lebar: "))

    LUAS = PANJANG*LEBAR
    KELILING = 2*(PANJANG+LEBAR)

    print(f"\nLuasnya Adalah: {LUAS}")
    print(f"Kelilingnya Adalah: {KELILING}")
'''

import os

# Fungsi Tampilan Header
def header():
    os.system("cls")
    print(f"{"PROGRAM PERSEGI PANJANG":^45}")
    print(f"{"HITUNG LUAS DAN KELILING😍":^46}")
    print(f"{"="*45:^45}")

# Fungsi Input User
def input_user():
    panjang = int(input("Masukkan Panjang: "))
    lebar = int(input("Masukkan Lebar: "))
    return lebar,panjang

def pesan_pilih():
    print(f"\nOperasi Tersedia:")
    print(f"1. Hitung Luas")
    print(f"2. Hitung Keliling")

# Fungsi Menghitung Luas
def LUAS(lebar,panjang):
    return lebar*panjang

# Fungsi Menghitung Keliling
def KELILING(lebar,panjang):
    return 2*(lebar+panjang)

# Fungsi Menampilkan Pesan Dan Hasil Perhitungan
def HASIL(rumus,nilai):
    print(f"Hasil Perhitungan {rumus} Adalah: {nilai}")

# Perulangan(while) Yang Menjadi Program Utama /
# Menerima Pengembalian Nilai Disetiap Fungsi
while True:
    header()
    LEBAR,PANJANG = input_user() # Variable Untuk Simpan Nilai Dari Fungsi input_user
    pesan_pilih()

    pilih = int(input("Pilih Salah Satu Operasi Diatas Menggunakan Angka > "))
    if pilih == 1:
        hitung_luas = LUAS(LEBAR,PANJANG)
        HASIL("Luas",hitung_luas)

    elif pilih == 2:
        hitung_keliling = KELILING(LEBAR,PANJANG)
        HASIL("Keliling",hitung_keliling)

    else:
        print(f"Input Yang Kamu Masukkan Tidak Valid")

    lanjut = input("\nApakah Lanjut (y/n)? ")
    if lanjut == "n":
        break

print("SUDAH SELESAI YAH!!😘")

