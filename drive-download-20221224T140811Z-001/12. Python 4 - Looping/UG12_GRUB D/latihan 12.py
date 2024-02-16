# no 1
string = ''
bar = 1

x = int(input("masukkan angka :"))

while bar <= x:
    kol = bar

    while kol > 0:
        string = string + " * "
        kol = kol - 1

    string = string + "\n"
    bar = bar + 1
print(string)

# no 2
str = ""
baris = 1

x = int(input("Masukkan angka :"))
print ("\n")
while baris <= x:
    kolom = baris
    while kolom >1:
        str = str + "   "
        kolom = kolom - 1
    left = 0
    while left <= (x - baris) :
        str = str + " * "
        left = left + 1
    right = left
    while right >1 :
        str = str + " * "
        right = right - 1
    
    str = str + "\n\n"
    baris = baris + 1
print(str)

# no 3
baris = 5

for i in range (0, baris):
    k = 1
    print(k, end=" ")
    for j in range (baris -i -1, 0, -1):
        print("* ", end=" ")
        k = k + 1
        print(k, end=" ")
    print("\n")
    
#no 4
inputan = int(input("Masukan Angka:"))

for i in range(inputan):
    for j in range(inputan - i - 1):
        print(" ", end="")
    for k in range(2 * i + -2):
        if k == 0 or k == 2 * i:
            print("**", end="")
        else:
            if i == inputan - 1:
                print("*", end="")
            else:
                print(" ", end="")
    print()
