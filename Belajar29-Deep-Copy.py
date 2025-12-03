## GAK PAHAM😭😭😢😭

data_0 = [1,2]
data_1 = [3,4]

data_list_bersarang = [data_0,data_1]
data_list_bersarang_copy = data_list_bersarang.copy()

print(f"Data List Bersarang Biasa: {data_list_bersarang}")
print(f"Data List Bersarang Copy: {data_list_bersarang_copy}")

# Mengmabil Data
data = data_list_bersarang[1][1] # Mengambil Dan Menyesuaikan dengan 2 Index
print(f"Data Sesuai Index List: {data}")

# Addres Semua Data List Bersarang 
print(f"Addres List Biasa: {hex(id(data_list_bersarang))}")
print(f"Addres List Copy: {hex(id(data_list_bersarang_copy))}")

# Mengambil Data Dari Index
print(f"Addres List Biasa: {hex(id(data_list_bersarang[0]))}")
print(f"Addres List Copy: {hex(id(data_list_bersarang_copy[0]))}")