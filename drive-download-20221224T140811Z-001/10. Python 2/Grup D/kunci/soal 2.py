pemain1 = input("Masukkan nama pemain pertama: ")
pemain2 = input("Masukkan nama pemain kedua: ")
pemain3 = input("Masukkan nama pemain ketiga: ")

kartu1 = int(input("Masukkan jumlah kartu pemain pertama: "))
kartu2 = int(input("Masukkan jumlah kartu pemain kedua: "))
kartu3 = int(input("Masukkan jumlah kartu pemain ketiga: "))

if kartu1 > 21 or kartu2 > 21 or kartu3 > 21:
    print("Jumlah kartu yang dimiliki melebihi batas")
elif (kartu1 > kartu2 and kartu1 > kartu3) and kartu1 <= 21:
    print(pemain1, "menang dengan jumlah kartu sebanyak", kartu1)
elif (kartu2 > kartu1 and kartu2 > kartu3) and kartu2 <= 21:
    print(pemain2, "menang dengan jumlah kartu sebanyak", kartu2)
elif (kartu3 > kartu1 and kartu3 > kartu1) and kartu3 <= 21:
    print(pemain3, "menang dengan jumlah kartu sebanyak", kartu3)
