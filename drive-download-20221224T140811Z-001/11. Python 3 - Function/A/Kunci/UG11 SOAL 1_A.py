def hitungKata(string,kata):
    hitung = string.lower().count(kata)
    return hitung

def ubahKata(string,old,new,jumlah=1):
    return string.replace(old,new,jumlah)

print('='*7+' Program Manipulasi String '+'='*7)
print('Pilihan Menu :\n1. Hitung Kata\n2. Ubah Kata')
pilihan = int(input('Pilihan anda : '))
string = input('Masukkan sebuah kalimat/kata : ')
if pilihan == 1:
    kata = input('Masukkan kata yang ingin dihitung : ')
    banyak = hitungKata(string,kata)
    print(f'Terdapat sebanyak {banyak} kata {kata} di dalam kalimat')
elif pilihan == 2:
    kata = input('Masukkan kata yang ingin di ubah : ')
    baru = input('Masukkan kata pengganti : ')
    hasil = ubahKata(string,kata,baru)
    print(f'String berhasil diubah menjadi : {hasil}')
else:
    print("Pilihan yang anda input tidak terdaftar di daftar pilihan")