'''
def penjumlahan(x, y):
    return x + y


def pengurangan(x, y):
    return x - y


def perkalian(x, y):
    return x * y


def pembagian(x, y):
    return x / y

print('=' * 25)
print('Operasi Matematika')
print('  1. Jumlah \t [+]')
print('  2. Kurang \t [-]')
print('  3. Kali \t [*]')
print('  4. Bagi \t [/]')
print('=' * 25)

operasi = input('Pilih operasi (1/2/3/4): ')

print('=' * 25)

if operasi in ('1', '2', '3', '4'):
    bilangan_1 = eval(input('Masukkan bilangan pertama: '))
    bilangan_2 = eval(input('Masukkan bilangan kedua: '))

    if operasi == '1':
        print("Hasil operasi dari",bilangan_1, "+", bilangan_2, "=", penjumlahan(bilangan_1, bilangan_2))

    elif operasi == '2':
        print("Hasil operasi dari",bilangan_1, "-", bilangan_2, "=", pengurangan(bilangan_1, bilangan_2))

    elif operasi == '3':
        print("Hasil operasi dari",bilangan_1, "*", bilangan_2, "=", perkalian(bilangan_1, bilangan_2))

    elif operasi == '4':
        print("Hasil operasi dari",bilangan_1, "/", bilangan_2, "=", pembagian(bilangan_1, bilangan_2))
    
    
else:
    print("Invalid Input")

print()

=====================================================================================


def kelipatan_sembilan(angka):
    if angka % 9 == 0:
        return "Benar"
    else:
        print ("Salah")
        return (angka % 9)

print ("Pemeriksa Kelipatan 9")
klip = int (input("Masukkan Kelipatan 9 yang ingin diperiksa: "))

print (kelipatan_sembilan(klip))

'''