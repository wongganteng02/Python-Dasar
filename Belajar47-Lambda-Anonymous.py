## Lambda Funtcion


def f_kuadrat(num1):
    return num1**2

print(f"Hasil Kuadra Fungsi Biasa = {f_kuadrat(7)}")


# Menggunakan lambda
# variable = lambda argument : expression
kuadrat = lambda num : num**2
print(f"Hasil Kuadrat Lambda Function = {kuadrat(6)}")

# Bisa Juga Menggunakan Argument Lebih Dari 1
bagi = lambda num1,num2 : num1/num2
print(f"Hasil Pembagian Lambda Function = {bagi(10,5)}")

# Sorting List Biasa
data_list = ["Putra","Wijaya","Kusuma"]
data_list.sort()
print(f"Hasil Sorting {data_list}")

# Sorting List Dgn Panjang / key=len
def panjang(nama):
    return len(nama)

data_list.sort(key=panjang)
print(f"Hasil Sort Dgn Panjang = {data_list}")

# Sorting Menggunakan Lambda
data_list1 = ["Illah","Ali","Ar-Ridho"]
data_list1.sort(key=lambda nama: len(nama))
print(f"Hasil Sort Dgn Panjang Dan Lambda = {data_list1} ")

# Menggunakan Filter Lambda Function
data_angka = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

def kurang_dari(angka):
    return angka < 5

hasil_angka = list(filter(kurang_dari,data_angka))
hasil_angka = list(filter(lambda x: x<5,data_angka))
print(f"Hasil List Kurang dari 5 = {hasil_angka}")

# Untuk Genap
data_genap = list(filter(lambda x:(x%2==0), data_angka))
print(f"Hasil List Genap = {data_genap}")

# Untu Ganjil
data_ganjil = list(filter(lambda x: (x%2==1),data_angka))
print(f"Hasil List Ganjil = {data_ganjil}")

# Lamnbda Untuk Menyesuaikan Sorting Dimulai Dari List Awal Hingga Hasil

def kurang(nama,num,clas):
    print(f"{nama} {num} {clas}")

kurang("We","x:",15)
kurang("C","x:",19)
kurang("For","x:",27)
