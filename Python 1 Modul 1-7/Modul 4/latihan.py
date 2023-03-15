def persegipanjang(panjang,lebar):
    luas = panjang * lebar
    print("luasnya :", luas)
    return luas

print("menghitung luas persegi panjang & persegi")
a = int(input("Masukan Panjang : "))
b = int(input("Masukan Lebar :"))
persegipanjang(a,b)

def persegi(sisi):
    luas = sisi * sisi
    print("Luasnya :", luas)
    return luas 

print("persegi")
c = int(input("Masukan Sisi :"))
persegi(c)
