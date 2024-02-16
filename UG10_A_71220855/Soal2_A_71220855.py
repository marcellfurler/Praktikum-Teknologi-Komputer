print("==== Selamat Datang di Toko Andi Tersenyum, Selamat Belanja!====")
x=int(input("Total Belanja : Rp."))
a=x-x*2/100
b=x-x*5/100
c=x-x*10/100
if x<=100000:
    print(f"Tidak Ada Diskon! Maka yang anda bayar adalah : Rp {x}")
elif x>=100000:
    print(f"Biaya yang harus dibayar setelah diskon adalah : Rp.",a)
elif x>=500000:
    print(f"Biaya yang harus dibayar setelah diskon adalah : Rp.",b)
elif x>=1000000:
    print(f"Biaya yang harus dibayar setelah diskon adalah : Rp.",c)