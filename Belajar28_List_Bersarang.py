## Membuat list didalam list


# List Biasa
data_0 = [1,2,3]
data_1 = [4,5,6]

data_list = [1,2,3,4,5,6]
print(f"list Biasa: {data_list}")

# Membuat list didalam list
print("\n=====BENTUK LIST BERSARANG BIASA=====")
list_1 = [data_0,data_1]
print(f"List  Didalam list: {list_1}")

# Bisa Dicampur Dengan List apapun 
list_1 = [data_0,data_1,data_list]
print(f"List  Didalam list: {list_1}")


# Contoh Penggunaan List Bersarang / List Dalam List

print("\n=====FUNGSI LIST BERSARANG=====")
siswa_0 = ["Muhammad Hafiz Isnani",16,"Laki-laki","Surabaya"]
siswa_1 = ["Wong Ganteng",19,"Laki-laki","Gresik"]
siswa_2 = ["Auliya Urrohmah",20,"Perempuan","Sidoarjo"]

list_siswa = [siswa_0,siswa_1,siswa_2]
print(f"List Siswa: {list_siswa}\n")

for i in list_siswa:
    print(f"Nama\t\t: {i[0]}")
    print(f"Umur\t\t: {i[1]}")
    print(f"Jenis Kelamin\t: {i[2]}")
    print(f"Domisili\t: {i[3]}\n")
