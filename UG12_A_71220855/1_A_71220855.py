x=int(input("Masukan awal deret : "))
y=int(input("Masukan akhir deret : "))
for a in range(x,y):
    if a%2!=0 and a%3!=0 and a%6!=0:
        print(a, '', end='')
    
