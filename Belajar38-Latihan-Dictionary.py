import datetime as dt

def list_mahasiswa():
    data_mahasiswa = {}

    while True:
        mahasiswa = {}

        mahasiswa['nama'] = input("Nama Mahasiswa: ")
        mahasiswa['prodi'] = input("Nama Prodi: ")
        mahasiswa['nim'] = int(input("NIM Mahasiwa: "))

        TAHUN = int(input("Tahun Lahir (YYYY): "))
        BULAN = int(input("Bulan Lahir (1-12): "))
        TANGGAL = int(input("Tanggal Lahir (1-31): "))
        mahasiswa['ttl'] = dt.datetime(TAHUN,BULAN,TANGGAL)

        KEY = input("Key Mahasiswa 3-4 Huruf: ").strip().upper()
        data_mahasiswa.update({KEY: mahasiswa})
                                
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
            
    return data_mahasiswa

hasil = list_mahasiswa()
print("PROGRAM SELESAI")