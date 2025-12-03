## List Menggunakan Loop


# For Loop
print("\n=====FOR LOOP=====")
list_num = [1,2,3,4,5,9,10]

for num in list_num:
    print(f"Angka: {num}")

list_name = ["Yoga","Azhar","Ihzam","Hafizh"]

for name in list_name:
    print(f"Nama = {name}")

# For Loop Dan Range
print("\n=====FOR LOOP & RANGE=====")
list_num = [34,34,123,35,83,0,524]
panjang = len(list_num)

for i in range(panjang):
    print(f"Angka = {list_num[i]}")

# While Loop
print("\n=====WHILE LOOP=====")
list_num = [34,34,123,35,83,0,524]
panjang = len(list_num)
i = 0
while i < panjang:
    print(f"Angka = {list_num[i]}")
    i += 1

# List Comprehension
print("\n=====COMPREHENSION=====")
data = ["Ravino",76,"Fahri",35,65]

[print(i) for i in data]

num = [34,34,123,35,83,0,524]
angka_kuadrat = [i**2 for i in num]
print(f"Angka Berkuadrat = {angka_kuadrat}")

# enumurate
print("\n=====ENUMERATE=====")
data_list = ["Ravino",76,"Fahri",35,65]

for index,data in enumerate(data_list):
    print(f"Index = {index}")
    print(f"Data = {data}")
