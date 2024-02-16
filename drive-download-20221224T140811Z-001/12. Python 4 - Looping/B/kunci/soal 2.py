print("~~~ Selamat Datang di Kalkulator Sederhana ~~~")
inputan = (input("Masukkan operator matematika yang ingin Anda hitung: "))

if "x" in inputan:
    pilihan = "Y"
    while pilihan == "Y":
        a = int(input("Mau perkalian berapa: "))
        stop = int(input("Print berapa banyak: "))
        kanan = a
        for kiri in range(1, a+1):
            print(kiri, " X ", kanan, " = ", (kiri*kanan))
            kanan -= 1
            if kiri == stop:
                break
        print()
        pilihan = input("Apakah Anda Ingin Menghitung Lagi? (Y/T): ").upper()
    print("Terima Kasih dan Sampai Jumpa Lagi!")
elif ":" in inputan:
    pilihan = "Y"
    while pilihan == "Y":
        a = int(input("Mau pembagian berapa: "))
        stop = int(input("Print berapa banyak: "))
        kanan = a
        for kiri in range(1, a+1):
            print(kiri, " : ", kanan, " = ", (kiri/kanan))
            kanan -= 1
            if kiri == stop:
                break
        print()
        pilihan = input("Apakah Anda Ingin Menghitung Lagi? (Y/T): ").upper()
    print("Terima Kasih dan Sampai Jumpa Lagi!")
elif "+" in inputan:
    pilihan = "Y"
    while pilihan == "Y":
        a = int(input("Mau penjumlahan berapa: "))
        stop = int(input("Print berapa banyak: "))
        kanan = a
        for kiri in range(1, a+1):
            print(kiri, " + ", kanan, " = ", (kanan+kiri))
            kanan -= 1
            if kiri == stop:
                break
        print()
        pilihan = input("Apakah Anda Ingin Menghitung Lagi? (Y/T): ").upper()
    print("Terima Kasih dan Sampai Jumpa Lagi!")
elif "-" in inputan:
    pilihan = "Y"
    while pilihan == "Y":
        a = int(input("Mau pengurangan berapa: "))
        stop = int(input("Print berapa banyak: "))
        kanan = a
        for kiri in range(1, a+1):
            print(kiri, " - ", kanan, " = ", (kiri-kanan))
            kanan -= 1
            if kiri == stop:
                break
        print()
        pilihan = input("Apakah Anda Ingin Menghitung Lagi? (Y/T): ").upper()
    print("Terima Kasih dan Sampai Jumpa Lagi!")
else:
    print("Maaf, Operator Matematika yang anda cari belum tersedia.")
