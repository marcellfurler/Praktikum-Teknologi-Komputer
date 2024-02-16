def cetakHuruf(string):
    if len(string) % 2 != 0:
        return string[:3]
    else:
        return string[-3:]


kata = input('Masukkan kata : ')
hasil = cetakHuruf(kata)
print(f'Huruf paling ujung pada kata {kata} adalah {hasil}')
