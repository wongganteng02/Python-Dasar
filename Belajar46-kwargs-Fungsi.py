#  Pelajari **kwargs


## Normal(Tanpa *args)

def ungkap(name, un, prodi):
    print(f"{name} Kuliah di {un} Dan Mengambil Jurusan {prodi}")

ungkap("WongElek", "UISI Gresik", "Teknik Informatika")


## Mengguakan kwargs
# Jika Menggunakan **kwargs/**... Tipenya Berubah menjadi Dictionary
# Sehingga Mengambil Value Dgn Menentukan key Yg Sesuai

def ungkap0(**kwargs):
    name = kwargs["name"]
    un = kwargs["un"]
    prodi = kwargs["prosi"]
    print(f"{name} Kuliah di {un} Dan Mengambil Jurusan {prodi}")

ungkap(name="WongGateli", un="UIN Malang", prodi="Teknik Sipil\n")


## Gabungan *args Dan **kwargs
# if / elif --> Percabangan Tampilan Dari input Antara key Dan Value Yg Dihasilkan **kwargs
# *args --> Ringkasan Nilai Input Untuk Operasi
# For Loop --> Menampilkan Perulangan Dari Hasil *args(Tuple)

def math(*args, **kwargs):
    output = 0
    if kwargs["message"] == "tambah":
        for angka in args:
            output += angka

    elif kwargs["message"] == "kurang":
        for angka in args:
            output -= angka

    elif kwargs["message"] == "kali":
        output = 1
        for angka in args:
            output *= angka

    return output

HASIL = math(1,2,3,4,5, message="tambah")
print(f"Hasil Penambahan: {HASIL}")

HASIL = math(1,2,3,4,5, message="kurang")
print(f"Hasil Pengurangan: {HASIL}")

HASIL = math(1,2,3,4,5, message="kali")
print(f"Hasil Perkalian: {HASIL}")

