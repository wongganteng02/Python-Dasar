## Penggunaan *args
# Mempermudah Jika Yg Diinputkan Itu Banyak


# Cara Biasa tanpa *args
# Yg Inputnya 3

def fungsi(nama, umur, pekerjaan):
    print(f"Umur {nama} Adalah {umur}, Dia Bekerja Sebagai {pekerjaan}")

fungsi("WongGanteng", 19, "Petani")


# Menggunakan List

def fungsi0(datalist):
    data = datalist.copy()
    nama = data[0]
    umur = data[1]
    pekerjaan = data[2]
    print(f"Umur {nama} Adalah {umur}, Saya Bekerja Sebagai {pekerjaan}")

fungsi0(["Saya", 20, "Guru"])


# Menggunakan *args
# args Adalah Variable Sehingga bisa dirubah namanya
# Jika Menggunakan *args/*... Typenya Berubah Menjadi Tuple

def fungsi1(*args):
    nama = args[0]
    umur = args[1]
    pekerjaan = args[2]
    print(f"Umur {nama} Adalah {umur}, Dia Bekerja Sebagai {pekerjaan}")

fungsi1(f"WongSangar", 23, "Jukir Liar" )


# Digunakan Jika Inputnya Banyak Tanpa Membuat Argument Yg Sesuai Input
# Tuple Tidak Support Operasi Perhitungan Kecuali Di Konversi Terlebih Dahulu
# Atau Di Loop dulu

def pangkat(*yondaktau):
    output = 1
    for angka in yondaktau:
        output += angka


    return output

hasil = pangkat(1,2,3,4,5,6,7,8,9)
print(f"Hasil: {hasil}")
