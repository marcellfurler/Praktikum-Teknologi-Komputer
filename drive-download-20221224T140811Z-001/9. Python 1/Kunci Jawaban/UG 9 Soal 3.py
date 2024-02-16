#Zhivaldo Fabio
#71200608

print ("="*10, "CATATAN BELANJA", "="*10)

belanja1 = ["Sikat Gigi", "Odol", "Shampoo", "Sabun", "Ciduk"]
belanja2 = ["Teh", "Gula", "Garam", "Micin", "Kecap"]

print ("="*10, "Daftar 1", "="*10)
print ("Daftar Belanja 1:", belanja1)
print ()
print ("="*10, "Daftar 2", "="*10)
print ("Daftar Belanja 2:", belanja2)

print ()
print ("Jawab dengan angka [1/2]")
print ("1. Rubah Belanjaan")
print ("2. Keluar")

choice = input("Masukkan Pilihan: ")

if choice == "1":
    rubah1 = input("Masukkan nama item ke daftar 1: ")
    baris1 = int(input("Masukkan index yang ingin dirubah: "))
    belanja1[baris1] = rubah1
    
    rubah2 = input("Masukkan nama item ke daftar 2: ")
    baris2 = int(input("Masukkan index yang ingin dirubah: "))
    belanja2[baris2] = rubah2
    
    print ()
    print ("="*10, "Daftar 1", "="*10)
    print ("Daftar Belanja 1:", belanja1)
    print ()
    print ("="*10, "Daftar 2", "="*10)
    print ("Daftar Belanja 2:", belanja2)
elif choice == "2":
    print ("Selamat berbelanja!")
    exit()
else:
    print ("WRONG INPUT")
    

