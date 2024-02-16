print ("SELAMAT DATANG DI PROGRAM PEMBUAT PIRAMIDA BERLUBANG")
n = int(input("Masukkan Angka : "))
print (" ")
for i in range(n):
    for j in range(n - i - 1):
        print(" ", end="")

    for k in range(2 * i + 1):
        if k == 0 or k == 2 * 1:
            print("*", end="")
        else:
            if i == n - 1:
                print("*", end="")
            else:
                print("", end="")
    print()
