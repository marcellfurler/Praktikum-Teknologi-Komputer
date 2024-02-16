tahun = int(input("Masukkan Tahun: "))

if (tahun % 4) == 0:
    if (tahun % 100) == 0:
        if (tahun % 400) == 0:
            print(tahun, "merupakan Tahun Kabisat.")
        else:
            print(tahun, "bukan merupakan Tahun Kabisat.")
    else:
        print(tahun, "merupakan Tahun Kabisat.")
else:
    print(tahun, "bukan merupakan Tahun Kabisat.")
