def buat_huruf(str):
    strlength=len(str)
    if strlength%2==0:
        return str[0]+str[1]+str[2]+ "dan" ,+str[-3]+str[-2]+str[-1]
    else:
        mid=int(strlength/2)
        return str[mid-1]+str[mid]+str[mid+1]

word=input("Masukan Kata : ")
res=buat_huruf(word)
print("Huruf yang diambil pada kata",word, "adalah",res)