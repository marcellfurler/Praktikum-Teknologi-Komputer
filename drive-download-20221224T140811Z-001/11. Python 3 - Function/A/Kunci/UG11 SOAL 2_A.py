def cetakHuruf(string):
    if len(string)%2 != 0:
        mid = len(string)//2
        return string[mid-1:mid+2]
    else:
        return string[:3]+" dan "+string[-3:]

kata = input('Masukkan kata : ')
hasil = cetakHuruf(kata)
print(f'Huruf yang diambil pada kata {kata} adalah {hasil}')