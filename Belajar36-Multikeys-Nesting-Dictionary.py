# ==============================
# Multikeys & Nesting Dictionary
# ==============================

import datetime as dt # Impor Datetime Dengan Syntax dt
import os

# Membuat Data Dictionary Dgn Penyusunan Lebih Rapi
mahasiswa1 = {
    'nama':'Deri Kusumawardani',
    'kelas':'Mojokerto',
    'prodi':'Informatika',
    'beasiswa': True,
    'nim': 25552000086,
    'ttl': dt.datetime(2005,12,2)
}

mahasiswa2 = {
    'nama':'Muhammad Saiful Amin Achyar',
    'kelas':'Mojokerto',
    'prodi':'Informatika',
    'beasiswa': True,
    'nim': 25552000105,
    'ttl': dt.datetime(2006,7,10)
}

mahasiswa3 = {
    'nama':'Yola Isrotul Augia',
    'kelas':'Mojokerto',
    'prodi':'Informatika',
    'beasiswa': True,
    'nim': 25552000116,
    'ttl': dt.datetime(2006,8,20)
}

mahasiswa4 = {
    'nama':'Manda Teguh Wijaya',
    'kelas':'Mojokerto',
    'prodi':'Informatika',
    'beasiswa': True,
    'nim': 25552000092,
    'ttl': dt.datetime(2004,3,27)
}

mahasiswa5 = {
    'nama':'Alfiani Putri Wahyudi',
    'kelas':'Mojokerto',
    'prodi':'Informatika',
    'beasiswa': True,
    'nim': 25552000081,
    'ttl': dt.datetime(2006,12,1)
}

# Buat Dict Baru Untuk Membuat Key Baru Dgn Value Variable Data Dict Sebelumnya
# Tanpa Merubah Data
os.system("cls") 
data_mahasiswa = { 
    'DKW': mahasiswa1,
    'MSAA': mahasiswa2,
    'YIA': mahasiswa3,
    'MTW': mahasiswa4,
    'APW': mahasiswa5
}

# Buat Struktur / Kolom Dan Syntax Rata Kanan(>) Rata Kiri(<) Tengah(^)
# Beserta Hitungan Berapa Baris Yg Dibutukan Value Kolom
print(f"{'KEY':<6} {'Nama':<28} {'Nim':<13} {'Kelas':<12} {'Prodi':<12} {'Beasiswa':^11} {'TTL':^11}")
print("-"*97)

for mahasiswa in data_mahasiswa: # Loop Data Dictionary Baru Menggunakan (constant)

    # Memisahkan Value Dari Data Dictionary Yg Baru Ke Data Dictionary Sebelumnya
    KEY = mahasiswa # Loop Untuk Menampilkan Key
    
    NAMA = data_mahasiswa[KEY]['nama'] # Loop Menampilkan Value Dari key 'nama'
    KELAS = data_mahasiswa[KEY]['kelas'] # Loop Menampilkan Value Dari key 'kelas'
    PRODI = data_mahasiswa[KEY]['prodi'] # Loop Menampilkan Value Dari key 'prodi'
    BEASISWA = data_mahasiswa[KEY]['beasiswa'] # Loop Menampilkan Value Dari key 'beasiswa'
    NIM = data_mahasiswa[KEY]['nim'] # Loop Menampilkan Value Dari key 'nim'
    TTL = data_mahasiswa[KEY]['ttl'].strftime('%x') # Loop Menampilkan Value Dari key 'ttl'

    # Menampilkan Semua Value Dengan Menyesuaikan Struktur Kolom Beserta Ratanya
    print(f"{KEY:<6} {NAMA:<28} {NIM:<13} {KELAS:<12} {PRODI:<12} {BEASISWA:^11} {TTL:^11}")



