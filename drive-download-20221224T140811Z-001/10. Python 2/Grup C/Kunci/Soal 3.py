daftar = input("Masukkan daftar pesanan : ")

daftar = str.title(daftar).split(", ")
print("Daftar pesanan : ",daftar)

tambah = input("Masukkan pesanan yang ingin ditambahkan : ")

if str.title(tambah) not in daftar:
    daftar.append(tambah.upper())
    print("Hasil penambahan pada daftar pesanan : ",daftar)
else:
    print(tambah.upper(),"sudah berada dalam daftar pesanan.")
print()