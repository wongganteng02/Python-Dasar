# Variable adalah tempat menyimpan data

# Assigment Nilai


# Penulisan Variable Boleh huruf/angka 
a = 10
x = 100
# Penulisan Variable Berupa angka tidak boleh didepan dan harus dibelakang huru
ax100 = 1000
# Penulisan Variable Tidak Boleh Dipisahkan Dgn Spasi/tanda apapun selain underscore(_)
ax_1000 = 10000
# Penulisan Value/nilai dari Variable jika menggunakan huruf/angka Disarankan Menggunakan Tanda petik 2("") agar membuat nilai sendiri
# Bukan Membuat value/nilai dari Variable Sebelumnya (Jika sama)
# Penulisan Value/nilai dari Variable jika menggunakan tanda petik 2 ("") Yg berisi angka/huruf Boleh dipisahkan Dgn Spasi
ax_10000 = "a x" 


# Penulisan Variable Beserta value/nilai Boleh Dideklarasikan secara sekaligus Dgn Dipisahkan tanda (,) & (Spasi)
a, x, ax100, a_x1000, a_x10000 = "10", "100", "1000", "10000", "a x"

print(a)
print(x)
print(ax100)
print(ax_1000)
print(ax_10000)

'''
Variable Di Python itu Ditulis Secara Expsplisit
Jadi tidak harus menyertakan TypeData Value/nilai dari Variable
'''


# Mengubah Value/nilai Yg Berbeda dari Variabel Sebelumnya
ax_1000 = 105
# Syntax Dibawah ini untuk mengetahui Type data Yg Digunakan
print(type(ax_1000))
# Dibawah ini Kata Yg Terdapat dalam Kurung Adalah Kata Yg Ditampilkan Di Terminal 
print("Nilai ax 1000 : ", ax_1000)


# Assignment indirect (Valuenya Tidak langsung ke Variable Awal Tapi ke Variable Sebelumnya)
ax = ax_1000
print("Nilai ax : ", ax)