## Operasi Dictionary

data_dict = {
    "wg":"Wong Ganteng",
    "st":"Santri Twoline"
}

lendict = len(data_dict)
print(f"Panjang Dictionary: {lendict}")

# Mengecek key exist Ada atau Tidak
key = 'wg'
checkey = key in data_dict
print(f"Apakah {key} Ada Di Data Dictionary? {checkey}")

# Mengakses atau Mengambil Value (read) Dgn get
print(data_dict["st"]) # Mengakases Data Dengan Tanda Kurung Siku / List
                       # Jika key Tidak Ada Maka Output Akan Error
print(data_dict.get("st")) # Mengakses Data Dengan get Dan Tanda Kurung Lengkung
print(data_dict.get("pt")) # Jika Key Tidak Ada Maka Output akan "None"

# Mengupdate Data Dictionary
'''
Jika key itu Sudah Ada Maka Akan Mengupdate / Memperbarui Value Yg Ditambahkan
Namun Jika key Tidak Ada Maka Otomatis Akan Menambahkan key dan value Baru Lagi
'''
data_dict.update({"wg":"wongganteng0212@gmail.com"})
print(data_dict)
data_dict.update({"ind":"Indonesia"})
print(data_dict)

# Mendelete Data Dictionary
del data_dict["ind"]
print(data_dict)


