print("="*50)
print("="*15, "REAL MAGHRIB FC","="*15)
username=str(input("Masukan Username Anda : "))
if username=="cakjidan" and "raulgonjales" and "karimbenjema":
    print("="*5,"Selamat datang",username,"="*5)
else :
    AD=print("Access Denied")

print("1. Tambah Data Pemain")
print("2. Hapus Data Pemain")
print("3. Tampilkan Data Pemain")
print("4. Exit")
masuk = input("Masukan Pilihan Anda : ")


if masuk=="1":
    tambahan=str(input("Tambahkan Data Pemain : "))
    print("Data",tambahan,"berhasil ditambahkan")
    print("1. Tambah Data Pemain")
    print("2. Hapus Data Pemain")
    print("3. Tampilkan Data Pemain")
    print("4. Exit")
    masuk = input("Masukan Pilihan Anda : ")
elif masuk=="2":
    data=input("Masukan Data yang akan Dihapus : ")
    print("Data",data,"berhasil ditambahkan")
    print("1. Tambah Data Pemain")
    print("2. Hapus Data Pemain")
    print("3. Tampilkan Data Pemain")
    print("4. Exit")
    masuk = input("Masukan Pilihan Anda : ")
elif masuk=="3":
    print("")
elif masuk=="4":
    print("Adios",username)
