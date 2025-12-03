# Looping Dictonary


friends = {
    'SA':'Muhammad Said, S.Pd',
    'SH':'Ahmad Sholihuddin, S.Pd',
    'MS':'Moh.Misbachul Munir, S.Pd',
    'DR':'Deri Kusumawardani',
    'NT':'Moh.Nafi\' Aftoni'
}

# Looping First Try

for fn in friends.keys(): # Looping Untuk Mengambil Semua Key Yg Ada
    print(fn)

# Operator Mengambil 
ky = friends.keys() # Mengambil Semua Key Dalam Bentuk List 
print(ky)

for fn in friends: # Mengambil Semua Value Data Dict
    print(friends.get(fn)) # Variable Data Dict Mengambil Semua Value Dalam Bentuk Loop Dgn .get 

'''
(Tetap Menggunakan Loop)
.get --> Digunakan Untuk Mengambil 1 Value Dgn Cara Memasukan key = (PerValue) / Memasukan
Variable Loop = Mencakup Semua Value

.values --> Hanya Bisa Digunakan Untuk Mengambil Semua Value Secara Langsung
(Lebih Mudah Jika Mengambil Semua Value)  
''' 
value = friends.values() # Mengambil Semua Value Dalam Bentuk List
print(value)

for x in friends.values(): # Mengambil Semua Value Yg Ada (Bukan Dalam Bentuk List)
    print(x)

# Mengambil Semua Item Termasuk Key Dan Value
item = friends.items() # Dalam Bentuk Tuples Didalam List
print(item)

for fn in friends.items(): # Dalam Bentuk Tuples / ()
    print(fn)
    
# Gabungan Key Dan Value Dalam Loop
for key,value in friends.items(): # Dalam Bentuk Key Dan Value Saja
    print(f"Key = {key}      Value = {value}") 




