## List --> array, Mengakses / Mengmabil Data Menggunkan Index

data_list = ["PT","Tokai","Dharma","Indonesia"]

print(data_list[0])

# Dictionary (dict) --> Associative array
# Associative array Menggunakan Identifier Dgn Kata Kunci = key

data_dict = {
    'key':'value1',
    'pt':'PT',
    'tk':'Tokai',
    'dh':'Dharma',
    'ind':'Indonesia',
    'dl':data_list,
    'num':2005
} 
# key Dimasukan Ke Dalam print Sebagaimana Mengambil Data Dgn Index 
print(data_dict['tk'])
print(data_dict['dl'])
print(data_dict['num'])

