print("~~~~~ Table Matematika Nich ~~~~~")
print("Pilihan Model Matematika")
print("1. Perkalian")
print("2. Pembagian")
model = int(input("Masukkan model matematika yang diinginkan 1/2 : "))
angka = int(input("Menampilkan table matematika dengan angka: "))

if model == 1:
    for i in range(1, 11):
        print(angka, 'x', i, '=', angka*i)
elif model == 2:
    for i in range(50, 66):
        print(i, ':', angka, '=', i/angka)
else: 
    print("Pilihan tidak tersedia, jangan ngasal!")