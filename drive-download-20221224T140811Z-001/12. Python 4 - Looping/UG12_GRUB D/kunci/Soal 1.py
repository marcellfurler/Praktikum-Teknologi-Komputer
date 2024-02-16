uang = int(input("Masukkan jumlah uang: Rp"))
mulai = input("Ketik 'START' untuk memulai: ")
mulai = mulai.lower()

sisa = 0
susu = 20000
permen = 500
roti = 15000
indomie = 3000
vitamin = 50000

while mulai == "start" :
    belanja = input("Apa barang yang akan Anda beli? ")
    if belanja == "susu":
        if uang >= susu:
            sisa = uang - susu
            print("Sisa uang Anda", sisa)
        else:
            print("Uang tidak cukup")
            sisa = uang
        uang = sisa    
    elif belanja == "permen":
        if uang >= permen:
            sisa = uang - permen
            print("Sisa uang Anda", sisa)
        else:
            print("Uang tidak cukup")
        uang = sisa  
    elif belanja == "roti":
        if uang >= roti:    
            sisa = uang - roti
            print("Sisa uang Anda", sisa)
        else:
            print("Uang tidak cukup")
        uang = sisa  
    elif belanja == "indomie":
        if uang >= indomie:    
            sisa = uang - indomie
            print("Sisa uang Anda", sisa)
        else:
            print("Uang tidak cukup")
        uang = sisa  
    elif belanja == "vitamin":
        if uang >= vitamin:
            sisa = uang - vitamin
            print("Sisa uang Anda", sisa)
        else:
            print("Uang Anda tidak cukup")
            sisa = uang
        uang = sisa  
    elif belanja == "SUDAH":
        break
    else:
        print("Barang tidak tersedia")
        sisa = uang