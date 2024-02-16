#bilangan ganjil yang tidak habis dibagi 3 dan dibagi 6

awal = int(input("Masukkan awal deret: "))
ahkir = int(input("Masukkan ahkir deret: "))
for i in range(awal,ahkir):
    if i%6 == 0 or i%3==0:
        continue
    else:
        if i%2!=0:
            print(i,end=' ')