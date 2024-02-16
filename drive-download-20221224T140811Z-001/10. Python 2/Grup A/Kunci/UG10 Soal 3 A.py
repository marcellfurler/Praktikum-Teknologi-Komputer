pertama = int(input("Masukkan nilai soal 1: "))
kedua = int(input("Masukkan nilai soal 2: "))
ketiga = int(input("Masukkan nilai soal 3: "))
umur = int(input("Masukkan umur anda: "))

a = pertama*(50/100)
b = kedua*(30/100)
c = ketiga*(20/100)
rata2= a+b+c

if umur <=25:
    if rata2 >= 80:
        print ("Rata-rata nilai Anda: ", rata2)
        print ("Selamat Anda lulus!")
    else:
        print ("Rata-rata nilai Anda: ", rata2)
        print ("Coba lagi tahun depan!")
else:
    if rata2 >= 90:
        print ("Rata-rata nilai Anda: ", rata2)
        print ("Selamat Anda lulus!")
    else:
        print ("Rata-rata nilai Anda: ", rata2)
        print ("Coba lagi tahun depan!")