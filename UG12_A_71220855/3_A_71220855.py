x= int(input('Masukkan Pembatas : '))
y= int(input('Masukan Angka yang dilarang : '))

for a in range(x):
    if a == y:
        continue
    print(a, end="")