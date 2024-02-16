a=input("Masukan nama : ")
b=len(a)

for i in range(b):
    for col in range(i+1):
        print (a[col], end= '')
    print()

for i in range(b, 0, -1):
    for col in range(0, i -1):
        print (a[col], end= '')
    print()