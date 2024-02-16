def reamur(data):
    return (4/5)*data
def fahrenheit(data):
    return (9/5)*data+32
def kelvin(data):
    return data + 273

print("="*7+" Konversi Skala Celcius "+"="*7,"\n1. Reamur\n2. Fahrenheit\n3. Kelvin")
pilihan = int(input("Masukkan pilihan: "))
bilangan = int(input("Masukkan angka yang ingin dikonversi (dalam skala Celcius) :  "))

if pilihan == 1:
    suhu = reamur(bilangan)
    print(f"{bilangan} derajat celcius dikonversi menjadi {suhu} derajat reamur")
elif pilihan == 2:
    suhu = fahrenheit(bilangan)
    print(f"{bilangan} derajat celcius dikonversi menjadi {suhu} derajat fahrenheit")
elif pilihan == 3:
    suhu = kelvin(bilangan)
    print(f"{bilangan} derajat celcius dikonversi menjadi {suhu} kelvin")
else:
    print("Pilihan yang anda input tidak terdaftar pada daftar pilihan")