print("~~~~~~~~~~~~~~~ /('v')\ ~~~~~~~~~~~~~~~")
print("PROGRAM PENGHITUNG VOLUME BANGUN RUANG")
print("~~~~~~~~~~~~~~~ \('v')/ ~~~~~~~~~~~~~~~")
print(" ")
print("Pilihlah salah satu bangun ruang yang ingin dihitung volumenya:")
print("1. Tabung")
print("2. Bola")
print("3. Prisma")
print("4. Kerucut")
print(" ")

pilihan = int(input("Masukkan pilihan Anda: "))

if pilihan == 1:
    alas = float(input("Masukkan panjang sisi alas limas: "))
    tinggi = float(input("Masukkan tinggi limas: "))
    limas = (1/3) * alas * alas * tinggi
    print("Volume limas tersebut adalah", limas)

elif pilihan == 2:
    r = float(input("Masukkan panjang jari-jari bola: "))
    bola = (4/3)*3.14*(r**3)
    print("Volume bola tersebut adalah", bola)

elif pilihan == 3:
    print("Pilihlah salah satu dari pilihan di bawah:")
    print("1. Prisma Segitiga")
    print("2. Prisma Segiempat")
    print("3. Prisma Segilima")
    pilih_prisma = int(input("Tentukan pilihan Anda: "))
    if pilih_prisma == 1:
        alas = float(input("Masukkan panjang sisi alas prisma: "))
        tinggi = float(input("Masukkan tinggi alas prisma: "))
        tinggi_prisma = int(input("Masukkan tinggi prisma segitiga: "))
        prisma_segitiga = ((1/2) * alas * tinggi) * tinggi_prisma
        print("Volume prisma segitiga tersebut adalah", prisma_segitiga)
    elif pilih_prisma == 2:
        alas = float(input("Masukkan panjang sisi alas prisma: "))
        tinggi = float(input("Masukkan tinggi alas prisma: "))
        tinggi_prisma = int(input("Masukkan tinggi prisma segiempat: "))
        prisma_segiempat = (alas * tinggi) * tinggi_prisma
        print("Volume prisma segiempat tersebut adalah", prisma_segiempat)
    elif pilih_prisma == 3:
        alas = float(input("Masukkan panjang sisi alas prisma: "))
        tinggi = float(input("Masukkan tinggi alas prisma: "))
        tinggi_prisma = int(input("Masukkan tinggi prisma segilima: "))
        prisma_segilima = ((1/2) * (5 * alas * tinggi)) * tinggi_prisma
        print("Volume prisma segilima tersebut adalah", prisma_segilima)
    else:
        print("Prisma yang Anda cari belum tersedia di Kalkulator ini")

elif pilihan == 4:
    r = float(input("Masukkan jari-jari kerucut: "))
    t = float(input("Masukkan tinggi kerucut: "))
    kerucut = (1/3)*3.14*r*r*t
    print("Volume kerucut tersebut adalah", kerucut)

else:
    print("Pilihan Anda tidak tersedia di menu kalkulator ini")
