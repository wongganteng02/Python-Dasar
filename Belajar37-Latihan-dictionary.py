import datetime as dt
import os

# Dictionary Utama Untuk Menyimpan Semua Data Dari Dictionary Sementara
data_mahasiswa = {}  

while True: # Mengulang Semua Elemen Termasuk Input Data
    os.system("cls") # Fungsi Clear PowerShell Dari Modul "import os"

    # Intro Input Data
    print("="*25) 
    print(f"{'WELOCOME TO DATABASE':^25}")
    print(f"{'DATA MAHASISWA':^25}")
    print("="*25)

    mahasiswa = {} # Dictionary Untuk Menyimpan Hasil Input Sementara  

    # Input Data Yg Akan Dimasukan Ke Dictionary Sementara
    # Sebagai Value Dari Key Dalam Bentuk kolom masing-masing 
    mahasiswa['nama'] = input("Nama Mahasiswa: ")
    mahasiswa['prodi'] = input("Nama Prodi: ")
    mahasiswa['nim'] = int(input("NIM Mahasiwa: "))
    TAHUN = int(input("Tahun Lahir (YYYY): "))
    BULAN = int(input("Bulan Lahir (1-12): "))
    TANGGAL = int(input("Tanggal Lahir (1-31): "))
    mahasiswa['ttl'] = dt.datetime(TAHUN,BULAN,TANGGAL)

    # Membuat Key Dengan Input
    # .strip --> Menghapus Karakter Jika Ada Spasi Agar Tidak Error
    # .upper --> Mengkonversi Input key Agar Menjadi Huruf Besar Semua 
    KEY = input("Key Mahasiswa 3-4 Huruf: ").strip().upper()
    data_mahasiswa.update({KEY: mahasiswa})

    # Buat Struktur / Kolom Dan Syntax Rata Kanan(>) Rata Kiri(<) Tengah(^)
    # Beserta Hitungan Berapa Baris Yg Dibutukan Value Kolom
    print(f"\n{'KEY':<6} {'Nama':<28} {'Nim':<13} {'Prodi':<12} {'TTL':^11}")
    print("-"*72)

    for KEY in data_mahasiswa: # Loop Data Dictionary Baru Menggunakan (constant)

        NAMA = data_mahasiswa[KEY]['nama'] # Loop Menampilkan Value Dari key 'nama'
        PRODI = data_mahasiswa[KEY]['prodi'] # Loop Menampilkan Value Dari key 'prodi''
        NIM = data_mahasiswa[KEY]['nim'] # Loop Menampilkan Value Dari key 'nim'
        TTL = data_mahasiswa[KEY]['ttl'].strftime('%x') # Loop Menampilkan Value Dari key 'ttl'

        # Menampilkan Semua Value Dengan Menyesuaikan Struktur Kolom Beserta Ratanya
        print(f"{KEY:<6} {NAMA:<28} {NIM:<13} {PRODI:<12} {TTL:^11}")

    print("\n")
    is_done = input("Wes Mari ta input te...(y/n)? ")
    if is_done == "y":
        break

print("PROGRAM SELESAI")
