x=(input("Masukan Nama Mahasiswa : "))
y=(input("Masukan NIM-nya : "))
if ((int(str(y)[2:4])==20 or 21 or 22) and ((int(str(y)[:2])==71))):
    print(x+(" merupakan Mahasiswa Informatika angkatan 20 hingga 22"))
else:
    print(x+(" bukan merupakan Mahasiswa Informatika angkatan 20 hingga 22"))
