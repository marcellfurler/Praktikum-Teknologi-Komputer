print("Cappucino seharga Rp. 25.000,00 dengan potongan harga 50%")
print("Vanilla Latte seharga Rp. 22.000,00 dengan potongan harga 60%")
print("Americano seharga Rp. 30.000,00 dengan potongan harga 35%")
print("Brewed Coffee seharga Rp. 20.000,00 dengan potongan harga 40%")

#INPUTAN
print ("===CAFE===\n ===Masukan Jumlah Pesanan===")
a=int(input("Cappucino Diskon 50% Rp 25.000  :"))
b=int(input("Vanilla Latte Diskon 65% Rp 22.000  :"))
c=int(input("Americano diskon 35% Rp 30.000  :"))
d=int(input("Brewed Coffee diskon 40% Rp 20.000  :"))

#PROSES
cap=a*25000*50/100
van=b*22000*65/100
Ame=c*30000*35/100
BCD=d*20000*40/100
jumlah=cap+van+Ame+BCD

#CETAK
print('======Total========')
print("Total Cappucino  :",cap)
print("Total Vanila Latte   :",van)
print("Total Americano  :",Ame)
print("Total Brewed Coffee  :",BCD)
print("Jumlah total Biaya yang harus dibayar adalah :",jumlah)

