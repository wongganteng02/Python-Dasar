# Penggunaan Type Hints (Opsional)

## Type Hints Berfungsi Sebagai Penanda Type Argument Dan Type return
# Jika Membuat Project Besar Disarankan Menggunakan Type Hints
# Agar Lebih Mudah Untuk Mengetehui Type Data Dalam Fungsi

def pangkat(argument:int) -> int: # Ini Yg Dimaksud Type Hints
    output = 10 ** argument
    return output

HASIL = pangkat(7)
print(HASIL)
