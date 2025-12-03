## PASS, CONTINUE, BREAK


# PASS
print('\n===PASS===')
angka = 0

while angka < 5:
    angka += 1
    print(f"Angka Sekarang -> {angka}")

    if angka == 3: # Jika Angka Sama Dgn 3 Maka print if  Akan Dijalankan Setelah 3 / Setelah Hasil While
        pass # Ini Tidak Di Berfungsi, hanya untuk menandai baris code.
        print("Anjay")


## CONTINUE
print('\n===CONTINUE===')
while angka < 10:
    angka += 1
    print(f"Angka Sekarang -> {angka}")

    if angka == 8:
        continue # Berfungsi Agar Melewati Program Yg Ada Didalam Continue
        print('Hello Ganteng')

print("Selesai")


## BREAK
print('\n===BREAK===')
while angka < 15:
    angka += 1
    print(f"Angka Sekarang -> {angka}")

    if angka == 13:
        break # Berfungsi Agar Benar-Benar Mengakhiri Program Dengan Kondisi Yg Sama Dan Sesuai
        print('heello Cantik😅')

print('Completed')
