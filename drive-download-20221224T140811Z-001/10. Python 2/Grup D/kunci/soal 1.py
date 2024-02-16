print("\(^o^) Selamat datang di Kalkulator Sederhana (^o^)/")
print("Ketik 1 untuk menghitung penjumlahan. ")
print("Ketik 2 untuk menghitung pengurangan. ")
print("Ketik 3 untuk menghitung perkalian. ")
print("Ketik 4 untuk menghitung pembagian. ")
print("Ketik 5 untuk menghitung sisa hasil bagi(modulus). ")
print("Ketik 6 untuk menghitung pemangkatan. ")

inputan = int(input("Masukkan pilihan Anda: "))

if inputan == 1:
    a = int(input("Masukkan bilangan pertama: "))
    b = int(input("Masukkan bilangan kedua: "))
    hasil = a + b
    print("Hasil dari", a, "dijumlahkan dengan", b, "adalah", hasil)

elif inputan == 2:
    a = int(input("Masukkan bilangan pertama: "))
    b = int(input("Masukkan bilangan kedua: "))
    hasil = a - b
    print("Hasil dari", a, "dikurangkan dengan", b, "adalah", hasil)

elif inputan == 3:
    a = int(input("Masukkan bilangan pertama: "))
    b = int(input("Masukkan bilangan kedua: "))
    hasil = a * b
    print("Hasil dari", a, "dikalikan dengan", b, "adalah", hasil)

elif inputan == 4:
    a = int(input("Masukkan bilangan pertama: "))
    b = int(input("Masukkan bilangan kedua: "))
    hasil = a / b
    print("Hasil dari", a, "dibagi dengan", b, "adalah", hasil)

elif inputan == 5:
    a = int(input("Masukkan bilangan pertama: "))
    b = int(input("Masukkan bilangan kedua: "))
    hasil = a % b
    print("Hasil dari", a, "dimodulus dengan", b, "adalah", hasil)

elif inputan == 6:
    a = int(input("Masukkan bilangan pertama: "))
    b = int(input("Masukkan bilangan kedua: "))
    hasil = a ** b
    print("Hasil dari", a, "dipangkatkan dengan", b, "adalah", hasil)

else:
    print("Input yang anda masukkan tidak valid")
