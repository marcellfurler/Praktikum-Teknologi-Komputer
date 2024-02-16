print("==========Program Manipulasi String==========")
print("Pilihan Menu : ")
print("1. Hitung Kata")
print("2. Ubah Kata")
pilihan=input("Pilihan Anda : ")
masukan=input("Masukan Sebuah Kalimat/Kata : ")

def hitung_kata():
    a=input("Masukan Kata yang ingin dihitung : ")
    abc=masukan.count(a)
    print("Terdapat sebanyak",abc, "kata" ,a, "di dalam kalimat")


def ubah_kata():
    x=input("Masukan Kata yang ingin diubah : ")
    y=input("Masukan kata pengganti : ")
    z=masukan.replace(x,y)
    print("String berhasil diubah menjadi : ",z)

if pilihan=="1":
    hitung_kata()
elif pilihan=="2":
    ubah_kata()
else:
    print("Pilihan yang anda input tidak terdaftar di daftar pilihan!")