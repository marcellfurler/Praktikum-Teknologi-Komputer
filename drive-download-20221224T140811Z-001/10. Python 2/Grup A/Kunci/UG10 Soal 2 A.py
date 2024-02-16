print("="*5, "Selamat datang di Toko Andi Tersenyum, selamat belanja!", "="*5)
belanja = int(input("Total belanja :Rp."))

if belanja >= 100000 and belanja < 500000:
    disk = belanja*(2/100)
    total = belanja-disk
    print("Biaya yang harus dibayar setelah diskon adalah: Rp.", total)
elif belanja >= 500000 and belanja < 1000000:
    disk = belanja*(5/100)
    total = belanja-disk
    print("Biaya yang harus dibayar setelah diskon adalah: Rp.", total)
elif belanja >= 1000000 :
    disk = belanja*(10/100)
    total = belanja-disk
    print("Biaya yang harus dibayar setelah diskon adalah: Rp.", total)
else: 
    print("Tidak ada diskon! Maka yang Anda bayarkan adalah: Rp.", belanja)
