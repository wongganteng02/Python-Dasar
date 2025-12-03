## Operator Bitwice, Operator Biner, Binary

## Hasil (Fokus Angka Binary)
# Bitwice OR Disini Menggunakan Tanda ini (|) Bukan "or"
a = 11
b = 7
c = a | b
print("\n========OR========\n")
print("Nilai a :",a,"   Binary :",format(a,'08b'))
print("Nilai b :",b,"   Binary :",format(b,"08b"))
print("=====OR DENGAN TANDA (|)=====")
print("Nilai c :",c,"   Binary :",format(c,"08b"))

##  Hasil (Fokus Angka Binary)
# Bitwice AND Disini Menggunakan Tanda ini (&) Bukan "and"
c = a & b
print("\n========AND========\n")
print("Nilai a :",a,"   Binary :",format(a,"08b"))
print("Nilai b :",b,"   Binary :",format(b,"08b"))
print("=====AND DENGAN TANDA (&)=====")
print("Nilai c :",c,"   Binary :",format(c,"08b"))

## Hasil (Fokus Angka Binary)
# Bitwice XOR Disini Sama Tetap Menggunakan Tanda ini (^)
c = a ^ b
print("\n========XOR========\n")
print("Nilai a :",a,"   Binary :",format(a,"08b"))
print("Nilai b :",b,"   Binary :",format(b,"08b"))
print("=====XOR DENGAN TANDA (^)=====")
print("Nilai c :",c,"   Binary :",format(c,"08b"))

## Bitwice NOT Disini Menggunakan Tanda (~)
# Rumus Hasil NOT Fokus Ke Angka Nilai Bukan Ke Angka Binary
# Rumus NOT : Nilai + 1 + (-) =  -Nilai + 1
c = ~a
print("\n========NOT=========\n")
print("Nilai a :",a,"    Binary :",format(a,"08b"))
print("=====NOT DENGAN TANDA (~)=====")
print("Nilai c :",c,"    Binary :",format(c,"08b"))

## Rumus Hasil Flip Fokus Ke Angka Binary Bukan Ke Angka Nilai
# Di Flip / Membalik Angka Binary "a" Yg Didalam Variable "c" Dengan Semua Angka Binary 
# Menjadi (11111111) Sama Dengan Code "0xFF" Sedangkan Tanda "&" Bukan "and" Tapi Termasuk Rumus Flip 
print("====FLIP (MEMBALIK ANGKA BINARY)====")
flip_c = ~a & 0xFF
print("Nilai c :", flip_c,"    Binary :",format(flip_c & 0xFF,"08b"))

## Shifting (Fokus Angka Binary)
# Shift Right (Geser Ke Kanan) Dengan Tanda ">>" Berapa Kali
# Menggeser Angka Binary Yg Mempunyai Nilai 1 Dari Kiri Ke Kanan Beberapa Kali
c = a >> 2
print("\n========SHIFTING=========\n")
print("Nilai a :",a,"    Binary :",format(a,"08b"))
print("=====SHIFT RIGHT DENGAN TANDA (>>)=====")
print("Nilai c :",c,"    Binary :",format(c,"08b"))

## Shifting (Fokus Angka Binary)
# Shift Left (Geser Ke Kiri) Dengan Tanda "<<" Berapa Kali
# Menggeser Angka Binary Yg Mempunyai Nilai 1 Dari Kanan Ke Kiri Beberapa Kali
c = a << 2
print("\n========SHIFTING=========\n")
print("Nilai a :",a,"    Binary :",format(a,"08b"))
print("=====SHIFT LEFT DENGAN TANDA (<<)=====")
print("Nilai c :",c,"    Binary :",format(c,"08b"))









