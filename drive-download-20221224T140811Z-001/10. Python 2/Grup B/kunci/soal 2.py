print("========== PROGRAM PENGHITUNG PYTHAGORAS ==========")

a = int(input("Masukkan bilangan bulat pertama: "))
b = int(input("Masukkan bilangan bulat kedua: "))
c = int(input("Masukkan bilangan bulat ketiga: "))

if (a * 2 + b * 2 == c ** 2):
    print("Merupakan Pythagoras.")
elif (a * 2 + c * 2 == b ** 2):
    print("Merupakan Pythagoras.")
elif (b * 2 + c * 2 == a ** 2):
    print("Merupakan Pythagoras.")
else:
    print("Bukan Merupakan Pythagoras.")
