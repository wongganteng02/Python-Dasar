## Buat Program List Buku


list_buku = []
while True: # Loop / Pengulangan Program
    print("\n====Masukan Data Buku====")
    judul = input("Masukan Judul Buku\t: ") # Input
    penulis = input("Masukan Nama Penulis\t: ") # Input

    new_book = [judul,penulis] # Jadikan Satu 2 Data input Kedalam 1 Variable
    list_buku.append(new_book) # Menyimpan Data baru Dari Varibale Jadi Satu (input) Kedalam Variale Yg Memiliki List Kosong

    print("No.\t| Judul\t\t\t| Penulis") # Mengatur Tata Letak Yg Pas Dengan Tab
    for index,book in enumerate(list_buku): # Mengambil Index dan Data Yg Disimpan Di Variable List Kosong Dgn enumerate
        print(f"{index+1}\t| {book[0]}\t\t| {book[1]}") # Menampilkan Setiap Index +1, Data Judul, Data Penulis

    lanjut = input("Apakah Lanjut Mencari?(y/n) > ") # WARNING

    if lanjut == "n": # Jika "n" Maka Program Akan Berhenti
        break         # Jika Selain "n" Maka Program Akan Terus Berlanjut
    
print("PROGRAM SELESAI")
        


    


