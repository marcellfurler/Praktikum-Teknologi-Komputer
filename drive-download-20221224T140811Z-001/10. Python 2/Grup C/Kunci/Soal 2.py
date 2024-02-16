#input
bulan = int(input("Masukkan bulan (1-12): "))

#proses
if( bulan == 1 ):
    jumlah_hari = 31
elif( bulan == 2 ):
    jumlah_hari = 28
elif( bulan == 3 ):
    jumlah_hari = 31
elif( bulan == 4 ):
    jumlah_hari = 30
elif( bulan == 5 ):
    jumlah_hari = 31
elif( bulan == 6 ):
    jumlah_hari = 30
elif( bulan == 7 ):
    jumlah_hari = 31
elif( bulan == 8 ):
    jumlah_hari = 31
elif( bulan == 9 ):
    jumlah_hari = 30
elif( bulan == 10 ):
    jumlah_hari = 31
elif( bulan == 11 ):
    jumlah_hari = 30
elif( bulan == 12 ):
    jumlah_hari = 31
else:
    print("bahwa bulan yang anda inputkan tidak valid.")

#output
print("Jumlah Hari:",jumlah_hari)


#proses cara 2
if bulan % 2 == 0 and bulan!=2:
    if bulan <8:
        jumlah_hari = 30
    else:
        jumlah_hari = 31
elif bulan % 2 == 1:
    if bulan <8:
        jumlah_hari =31
    else:
        jumlah_hari = 30
elif bulan == 2 :
    jumlah_hari = 28
else:
    print("Bulan yang anda masukkan tidak valid!")