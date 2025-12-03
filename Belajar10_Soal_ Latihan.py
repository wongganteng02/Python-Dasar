### (-) = "or"
### (+) = "and"
## Soal 1
# ------0++++++5--------8+++++++11------
print("\n",10*"=","\n")
inpuUser1 = float(input("Masukkan Angka!!\nLebih Dari 0\nAtau\nKurang Dari Lima\nDan\nLebih Dari 8\nAtau\nKurang Dari 11\n : "))

nol1 = (inpuUser1 > 0)
limo1 = (inpuUser1 < 5)
wolu1 = (inpuUser1 > 8)
suwelas1 = (inpuUser1 < 11)

print("Lebih  Dari 0  = ",nol1)
print("Kurang Dari 5  = ",limo1)
print("Lebih  Dari 8  = ",wolu1)
print("Kurang Dari 11 = ",suwelas1)

correct1 = nol1 and limo1 or wolu1 and suwelas1
print("Hasil Correct Soal 1 Adalah = ",correct1)

## Soal 2
# +++++0-----5+++++8-----11+++++
print("\n",10*"=","\n")
inputUser2 = float(input("Masukkan Angka!!\nKurang Dari 0\nAtau\nLebih Dari 5\nDan\nKurang Dari 8\nDan\nKurang Dari 8\nAtau\nLebih Dari 11\n: "))

nol2 = (inputUser2 < 0)
limo2 = (inputUser2 > 5)
wolu2 = (inputUser2 < 8)
suwelas2 = (inputUser2 > 11)

print("Kurang Dari 0  = ",nol2)
print("Lebih  Dari 5  = ",limo2)
print("Kurang Dari 8  = ",wolu2)
print("Lebih  Dari 11 = ",suwelas2)

correct2 = nol2 or limo2 and wolu2 or suwelas2
print("Hasil Correct Soal 2 Adalah = ",correct2)

# JAWABAN (VARIABLE) VERSI B.JAWA X B.INGGIRS X B.PYTHON