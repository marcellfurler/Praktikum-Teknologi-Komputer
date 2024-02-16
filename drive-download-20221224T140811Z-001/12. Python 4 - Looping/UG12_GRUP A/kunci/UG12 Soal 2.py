n1 = input("masukkan nama : ")
n=len(n1)

for i in range(n+1):
    for j in range(0,i):
        print (n1[j], end="")
    for j in range(i,1):
        print(" ", end="")
    print()

for i in range(n,0,-1):
    for y in range(i - 1):
        print(n1[y], end="")
    for y in range(n - i):
        print("", end="")
    print()