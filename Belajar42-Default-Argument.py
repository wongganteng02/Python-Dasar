# Default Argument

## def namafungsi(argument):
## def namafungsi(argument = nilai default):

# Default Argument Adalah Mengisi Value Parameter Secara Langsung
# Menggunakan Tanda (=)
# Tanpa Memberi value Ketika Memanggil Fungsi itu sendiri

# Tanpa Default
def gombal(nama):
    print(f"Hallo {nama}")

gombal("Sayang🥰\n")

# Dengan Default
def sapa(name = "Ganteng😎"):
    print(f"Hallo {name}")

sapa()
sapa("Cantik😋\n")

# Dengan Default Juga
def nanya(object, pesan = "nanya"):
    print(f"Kamu {pesan} {object}")

nanya("Dimana")
nanya("😗🙄\n")

