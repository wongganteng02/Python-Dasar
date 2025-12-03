# sisi adalah dari baris atas sampai baris bawah
sisi = int(input("Masukkan Angka Ganjil: "))

## SEGITIGA ATAS
# Membuat Urutan Dengan Logika, List ke 1 Sampai Dengan Sisi Yaitu 5 + 1
# + 1 Karna Default range Akan Mengurangi 1 Dari Nilai Akhir Yaitu Sisi
for i in range(1, sisi + 1):
    print(" " * (sisi - i) + "*" * (2 * i - 1))

for i in range(sisi - 1, 0, -1):
    print(" " * (sisi - i) + "*" * (2 * i - 1))




'''
for i in range(1, sisi + 1) = Membuat Urutan Dengan Logika, List ke 1 Sampai Dengan Sisi Yaitu 5 + 1.
+ 1 Karna Default range Akan Mengurangi 1 Dari Nilai Akhir Yaitu Sisi.
" " * (sisi - i) = 5 - List Dari 1 Sampai 5 --> Membuat Spasi

"+" * (2 * i - 1) = 2 x List Dari 1 Sampai 5 - 1 --> Membuat Tanda +

'''