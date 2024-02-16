batas = int(input("Masukkan Pembatas : "))
larang = int(input("Masukkan Angka yang dilarang : "))

for a in range(batas):
    if (a == larang or a == batas):
        continue
    print(a,end=' ')
print()