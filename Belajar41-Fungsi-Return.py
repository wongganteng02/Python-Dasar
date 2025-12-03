''' Fungsi Dengan Kembalian '''

# Template Fungsi Denga Kembalian
'''
def nama_fungsi(argument):
    badan fungsi
    return output
'''

# Fungsi Kuadrat
def kuadrat(input_kuadrat):
    ''' Fungsi Kuadrat '''
    output = input_kuadrat**2
    return output

y = kuadrat(7)
print(f"{y}\n")

print(kuadrat(11))

a = 10 * kuadrat(3)
print(f'{a}\n')

# Fungsi Tambah 
def tambah(angka1,angka2):
    ''' Fungsi return Dengan Multi Input '''
    return angka1 + angka2

a = tambah(10,8)
print(f"{a}\n")

# Fungsi Dengan Return Banyak
def operasi_mtk(angka1,angka2):
    tambah = angka1 + angka2
    kurang = angka1 - angka2
    kali = angka1 * angka2
    bagi = angka1 / angka1

    return tambah,kurang,kali,bagi

k,l,m,n = operasi_mtk(9,5)

print(f"Hasil Penambahan = {k}")
print(f"Hasil Pengurangan = {l}")
print(f"Hasil Perkalian = {m}")
print(f"Hasil Pembagian = {n}")

