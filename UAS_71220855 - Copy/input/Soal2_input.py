nama=str(input("Masukan Nama Anda : "))
nim=input("Masukan NIM Anda : ")

if nim[0:2]=="71" and (int(nim[2:4])==22) :
    print("Hallo",nama,"! selamat mengerjakan")
else :
    print("Tidak bisa mengerjakan karena anda bukan mahasiswa informatika angkatan 22")

# soal1
soal1=print("Hardware yang gunanya untuk menyimpan data sementara yaitu . . . \na. RAM \nb. Prosessor \nc. Motherboard \nd. SSD")
jawaban1=input("Masukan Jawaban Anda : ")
if jawaban1=="a":
    print("Jawaban anda Benar!")
    nilai=print("Nilai anda 50")
    x=50
else:
    print("Jawaban Anda Salah!")
    x2=0
# soal2
soal2=print("1000-7= . . .(dalam biner) \na. 1111100011 \nb. 1111100001 \nc. 1011100001 \nd. 1111000001")
jawaban2=input("Masukan Jawaban Anda : ")

if jawaban2=="b":
    print("Jawaban anda Benar!")
    nilai2=print("Nilai anda 50")
    y=50
else:
    print("Jawaban Anda Salah!")
    y2=0

print("Total Nilai Anda ",(x+y))