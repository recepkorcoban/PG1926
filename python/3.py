def sıfırları_silme(a):
    i=0
    while i<a:
        i+=1
        sayilar.remove("0")        
sayi=input("Bir sayi giriniz(aralarında boşluk bırakarak): ")
sayilar=sayi.split()
print("Girilen sayilar: {}".format(sayilar))
a=sayilar.count("0")
sıfırları_silme(a)
j=0
while j<a:
    
    sayilar.insert(j,"0")
    j+=1
print("Yeni siralama: {}".format(sayilar))