a=int(input("Masukan Nilai Soal 1 : "))
b=int(input("Masukan Nilai Soal 2 : "))
c=int(input("Masukan umur Anda : "))
x=a+b/2
d=print(f"Rata-rata anda : {x}")
if x==0:
    print(f"Rata-rata nilai anda : {x}")
elif c<=25:
    print("Selamat, anda lulus!")
elif x<=75:
    print(f"Coba lagi tahun depan! : {x}")
elif x>=80:
    print("Selamat, anda lulus!")
else:
    print("Coba lagi tahun depan")