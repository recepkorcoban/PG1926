sayi=input("Sayilari giriniz(aralarında boşluk bırakarak): ")
liste=sayi.split()
liste.reverse()
tek_sayilar=[]
for i in range(0, len(liste)): 
    liste[i] = int(liste[i])   
print(liste)

a = 0
while a < len(liste)-1:
    if liste[a] % 2 == 1:
        tek_sayilar.append(liste[a])
        print(a) 
    a += 1
print("En buyuk tek sayi: {}".format(tek_sayilar[0]))