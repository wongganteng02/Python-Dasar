# Copy Dictionary

friend = {
    'MZ':'Ahmad Muzakki',
    'HR':'Muhammad Heriyanto,S.Pd',
    'FW':'Farih Rahmawan,S.S',
    'MM':'Ma\'ruf,S.Ag',
    'HS':'Ahmad Abdul Hasan,S.Pd'
}
frn = friend

print(f"\nfriend = {friend}\n")
print(f"frn = {frn}\n")

# Jika Data Dalam "friend" Diubah Maka Data Dalam "frn" Juga Ikut Berubah
# Karna Meskipun Beda Varible Tapi Masih Dalam Penyebutan Data Yg Sama
friend['FW'] = "Fawaeid"
print(f"friend = {friend}\n")
print(f"frn = {frn}\n")

# Dengan Data Yg Sama Tapi Dictionary Yg Berbeda(Tidak Merubah Data Awal)
frn = friend.copy() # Mengcopy "friend"
friend['FW'] = "Farih Rahmawan,S.S" # Mengganti Semula "friend"
print(f"frn copy+ganti = {frn}\n") # Tetap Salinan Data Sebelumnya
print(f"friend copy = {friend}\n") # Data Dictionary "friend" Sudah Diubah Tanpa Mengubah "frn"

# Pop Dictionary
# Memindahkan Data Berdasarkan Key Dari Dictionary Ke "data_makruf"
data_makruf = friend.pop('MM') 
print(f"Data Ma'ruf = {data_makruf}")
print(f"friend = {friend}\n")

# PopItem Dictionary
# Memindahkan Data Yg Terakhir Saja Dari Dictionary Ke "data_terakhir"
data_terakhir = friend.popitem()
print(f"Data Terakhir = {data_terakhir}")
print(f"friend = {friend}\n")




