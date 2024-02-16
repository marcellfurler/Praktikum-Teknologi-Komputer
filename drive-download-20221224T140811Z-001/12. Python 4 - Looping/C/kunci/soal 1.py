kata = input("Masukan Kata atau angka : ")
for char in range(len(kata) - 1, -1, -1):
    print(kata[char], end="")
print()
