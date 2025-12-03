# Latihan Konversi Temperatur

## Program Konversi/Merubah (Celcius) Ke (Celcius, Reamor, Fahrenheit, Kelvin)
# Rumus Temperatur Ada Di Setelah File ini
print("\nPROGRAM KONVERSI TEMPERATUR\n")

celcius = float(input("Masukan Suhu Dalam Celcius : "))
print("Suhu Adalah : ",celcius,"Celcius")

reamor = 4 / 5 * celcius
print("Suhu Dalam Reamor Adalah : ", reamor, "Reamor")

fahrenheit = 9 / 5 * celcius + 32
print("Suhu Dalam Fahrenheit Adalah : ", fahrenheit, "Fahrenheit")

kelvin = celcius + 273
print("Suhu Dalam Kelvin Adalah : ", kelvin, "Kelvin")