angka = int(input("Masukkan angka : "))
hitung_angka = int(input("Masukkan angka yg dihitung : "))
counter = 0
while angka > 0:
    if int(angka % 10) == hitung_angka:
        counter += 1
    angka = int(angka / 10)

print("Angka", hitung_angka, "muncul sebanyak", counter, "kali.")
