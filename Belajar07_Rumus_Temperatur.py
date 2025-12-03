## Rumus Konversi Dari Temperatur Celcius 

# Celcius ke Celcius    = float(input("Masukan Suhu Dalam Celcius : "))
# Celcius ke Reamor     = 4 / 5 * celcius
# Celcius ke Fahrenheit = 9 / 5 * celcius + 32
# Celcius ke Kelvin     = celcius + 273

## Rumus Konversi Dari Temperatur Reamor

# Reamor ke Reamor      = float(input("Masukan Suhu Dalam Reamor : "))
# Reamor ke Celcius     = 5 / 4 * reamor
# Reamor ke Fahrenheit  = 9 / 4 * reamor + 32
# Reamor ke Kelvin      = 5 / 4 + 273

## Rumus Konversi Dari Temperatur Fahrenheit

# Fahrenheit ke Fahrenheit = float(input("Masukan Suhu Dalam Fahrenheit : "))
# Fahrenheit ke Celcius    = 5 / 9 * (fahrenheit - 32)
# Fahrenheit ke Reamor     = 4 / 9 * (fahrenheit - 32)
# Fahrenheit ke Kelvin = Fahrenheit Harus DiKonversikan Terlebih Dahulu Ke Celcius Baru Celcius DiKonversikan Lagi Ke Kelvin  
# Contoh Rumus Fahrenheit ke Kelvin :
fahrenheit = float(input("Masukan Suhu Dalam Fahrenheit : "))
celcius = 5 / 9 * (fahrenheit - 32)
kelvin = celcius + 273
print("Suhu Dalam Kelvin Adalah : ", kelvin, "Kelvin")

## Rumus Konversi Dari Temperatur Kelvin

# Kelvin ke Kelvin     = float(input("Masukan Suhu Dalam Kelvin : "))
# Kelvin ke Celcius    = kelvin - 273
# Kelvin ke Reamor     = 4 / 5 * (kelvin - 273)
# Kelvin ke Fahrenheit = Kelvin Harus DiKonversikan Terlebih Dahulu Ke Celcius Baru Celcius DiKonversika Lagi Ke Fahrenheit
# Contoh Rumus Kelvin ke Fahrenheit :
kelvin = float(input("Masukan Suhu Dalam Kelvin : "))
celcius = kelvin - 273
fahrenheit = 9 / 5 * celcius + 32
print("Suhu Dalam Farenheit Adalah : ", fahrenheit, "Fahrenheit")
