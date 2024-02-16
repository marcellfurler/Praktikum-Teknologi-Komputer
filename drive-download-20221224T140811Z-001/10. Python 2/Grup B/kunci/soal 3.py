print("~~ Selamat Datang di Program Pengurutan Bilangan ~~")
print("Tentukan Pilihan Anda!!! [1/2]")
print(" ")
print("1. Ascending")
print("2. Descending")
print(" ")
pilihan = int(input("Masukkan Pilihan yang Anda Inginkan: "))
print(" ")

if pilihan == 1:
    bil1 = int(input("Masukkan bilangan pertama : "))
    bil2 = int(input("Masukkan bilangan kedua : "))
    bil3 = int(input("Masukkan bilangan ketiga : "))
    bil4 = int(input("Masukkan bilangan keempat : "))

    if bil2 > bil1 and bil2 > bil3 and bil2 > bil4:
        if bil1 > bil3 and bil1 > bil4:
            if bil3 > bil4:
                print("Urutan bilangan dari yang terkecil adalah",
                      bil4, bil3, bil1, bil2)
            else:
                print("Urutan bilangan dari yang terkecil adalah",
                      bil3, bil4, bil1, bil2)
    elif bil1 > bil2 and bil1 > bil3 and bil1 > bil4:
        if bil2 > bil3 and bil2 > bil4:
            if bil3 > bil4:
                print("Urutan bilangan dari yang terkecil adalah",
                      bil4, bil3, bil2, bil1)
            else:
                print("Urutan bilangan dari yang terkecil adalah",
                      bil3, bil4, bil2, bil1)
    elif bil3 > bil2 and bil3 > bil1 and bil3 > bil4:
        if bil2 > bil1 and bil2 > bil4:
            if bil1 > bil4:
                print("Urutan bilangan dari yang terkecil adalah",
                      bil4, bil1, bil2, bil3)
            else:
                print("Urutan bilangan dari yang terkecil adalah",
                      bil1, bil4, bil2, bil3)
    elif bil4 > bil2 and bil4 > bil1 and bil4 > bil3:
        if bil2 > bil1 and bil2 > bil3:
            if bil1 > bil3:
                print("Urutan bilangan dari yang terkecil adalah",
                      bil3, bil1, bil2, bil4)
            else:
                print("Urutan bilangan dari yang terkecil adalah",
                      bil1, bil3, bil2, bil4)

elif pilihan == 2:
    bil1 = int(input("Masukkan bilangan pertama : "))
    bil2 = int(input("Masukkan bilangan kedua : "))
    bil3 = int(input("Masukkan bilangan ketiga : "))
    bil4 = int(input("Masukkan bilangan keempat : "))

    if bil2 > bil1 and bil2 > bil3 and bil2 > bil4:
        if bil1 > bil3 and bil1 > bil4:
            if bil3 > bil4:
                print("Urutan bilangan dari yang terbesar adalah",
                      bil2, bil1, bil3, bil4)
            else:
                print("Urutan bilangan dari yang terbesar adalah",
                      bil2, bil1, bil4, bil3)
    elif bil1 > bil2 and bil1 > bil3 and bil1 > bil4:
        if bil2 > bil3 and bil2 > bil4:
            if bil3 > bil4:
                print("Urutan bilangan dari yang terbesar adalah",
                      bil1, bil2, bil3, bil4)
            else:
                print("Urutan bilangan dari yang terbesar adalah",
                      bil1, bil2, bil4, bil3)
    elif bil3 > bil2 and bil3 > bil1 and bil3 > bil4:
        if bil2 > bil1 and bil2 > bil4:
            if bil1 > bil4:
                print("Urutan bilangan dari yang terbesar adalah",
                      bil3, bil2, bil1, bil4)
            else:
                print("Urutan bilangan dari yang terbesar adalah",
                      bil3, bil2, bil4, bil1)
    elif bil4 > bil2 and bil4 > bil1 and bil4 > bil3:
        if bil2 > bil1 and bil2 > bil3:
            if bil1 > bil3:
                print("Urutan bilangan dari yang terbesar adalah",
                      bil4, bil2, bil1, bil3)
            else:
                print("Urutan bilangan dari yang terbesar adalah",
                      bil4, bil2, bil3, bil1)
