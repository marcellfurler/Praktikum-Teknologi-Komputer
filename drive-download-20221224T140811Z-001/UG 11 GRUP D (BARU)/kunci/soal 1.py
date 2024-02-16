global f
f = 0

# this t_movie function is used to select movie name


def t_movie():
    global f
    f = f+1
    print("Mau nonton film apa nih? Ada film: ")
    print("1. Frozen ")
    print("2. Keramat")
    print("3. KKN di Desa Penari")
    movie = int(input("Pilih nomor film: "))
    if f == 1:
        if movie == 1:
            theater()
        elif movie == 2:
            theater()
        elif movie == 3:
            theater()
        else:
            print("Pilihan tidak tersedia.")


def theater():
    print("Mau nonton layar bioskop apa: ")
    print("1. Reguler")
    print("2. Dolby almos")
    print("3. Premiere")
    a = int(input("Pilih nomor tipe layar: "))
    ticket = int(input("Berapa banyak tiket? "))
    timing(a)


def timing(a):
    print("Mau nonton jam berapa: ")
    print("1. 12.35")
    print("2. 14.45")
    print("3. 16.55")
    print("4. 19.05")
    time1 = int(input("Masukkan angka pilihan Anda: "))
    if time1 == 1:
        print("Oke berhasil!, silahkan dinikmati di jam 12.35")
    elif time1 == 2:
        print("Oke berhasil!, silahkan dinikmati di jam 14.45")
    elif time1 == 3:
        print("Oke berhasil!, silahkan dinikmati di jam 16.55")
    elif time1 == 4:
        print("Oke berhasil!, silahkan dinikmati di jam 19.05")
    else:
        print("Pillihan tidka tersedia.")


def movie(theater):
    if theater == 1:
        t_movie()
    elif theater == 2:
        t_movie()
    elif theater == 3:
        t_movie()
    else:
        print("Pilihan belum tersedia.")


def tempat():
    print("Halo selamat datang di bioskop! ")
    print("Dimanakah kamu ingin menonton?")
    print("1) XXI Empire")
    print("2) XXI Amplaz")
    print("3) XXI JCM")
    place = int(input("Masukkan pilihanmu: "))
    if place == 1:
        t_movie()
    elif place == 2:
        t_movie()
    elif place == 3:
        t_movie()
    else:
        print("Pilihan tidak tersedia.")


tempat()
