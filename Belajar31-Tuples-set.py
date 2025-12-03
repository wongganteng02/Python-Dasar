# List
data_list = [4,21,45,3,8,32] # Menggunkan Kurung Siku
print(f"\nData Kurung Siku = {data_list}")
print(data_list[0]) # Mengambil Data Dari Index
data_list[1] = 5 # Manipulasi List Kurung Siku
print(data_list)

# Tuples
data_tuples = (12,65,73,64,37)
print(f"\nData Kurung Lengkung = {data_tuples}")
print(data_tuples[2])
# Hanya Bisa Mengambil Data Dari Index 
# Tidak Bisa Memanipulasi Data Dengan Apapun Dalam Kurung Lengkung

# Sets
data_sets = {32,4,72,34,1,10}
print(f"\nData Kurung Kurawal = {data_sets}")
data_sets.remove(72)
data_sets.add("Sayang")
print(data_sets)
# Data Sets Hanya Bisa Ditambahkan Atau Dihapus Jadi Tidak Bisa Dimanipulasi Dgn Apapun
# Data Sets Tidak Memiliki Index Dan Tidak Bisa Mengambil Data Dengan Index
# Sehingga Data Tidak Berurutan
