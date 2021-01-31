class Ogrenci:
    def __init__(self,isim,soyisim,yaş,not_ort):
        self.isim=isim
        self.soyisim=soyisim
        self.yaş=yaş
        self.not_ortalaması=not_ort
    def info(self):
        print("{} {} ın yaşı {} dir ve notu {} dür".format(self.isim,self.soyisim,self.yaş,self.not_ortalaması))
bir=Ogrenci("RECEP","KÖRÇOBAN",21,100)
bir.info()

class Ogretmen:
    def __init__(self,isim,soyisim,yaş,maaş,alanı,top_gir_sınıf):
        self.isim=isim
        self.soyisim=soyisim
        self.yaş=yaş
        self.maaş=maaş
        self.alanı=alanı
        self.top_sınıf=top_gir_sınıf
    def info(self):
        print("{} {} ın yaşı {} dir {}TL maaş almaktadır.{} dersine ve toplam {} sınıfa girer".format(self.isim,self.soyisim,self.yaş,self.maaş,self.alanı,self.top_sınıf))    

bir=Ogretmen("ali","kaya",21,8500,"Mat",3)
bir.info()

class Calısanlar:
    def __init__ (self,isim,soyisim,yaş,maaş,görevi,çalıştığı_günler):
        self.isim=isim
        self.soyisim=soyisim
        self.yaş=yaş
        self.maaş=maaş
        self.görevi=görevi
        self.çalıştığı_günler=çalıştığı_günler
    def info(self):
        print("""
            isim={}
            soyisim={}
            yaş={}
            maaş={}
            görevi={}
            çalıştığı günler={}
            """.format(self.isim,self.soyisim,self.yaş,self.maaş,self.görevi,self.çalıştığı_günler))

bir=Calısanlar("tuğba","kara",35,4500,"Kat Görevlisi","PZT-SALI")
bir.info()

class Yönetim:
    def __init__(self,isim,soyisim,maaş,görev):
        self.isim=isim
        self.soyisim=soyisim
        self.maaş=maaş
        self.görev=görev
    def info(self):
        print("""
            isim={}
            soyisim={}
            maaş={}
            görevi={}
            """.format(self.isim,self.soyisim,self.maaş,self.görev))    
        
bir=Yönetim("YAVUZ","kara",8000,"MÜDÜR")
bir.info()

class Sınıf:
    def __init__(self,kişi_sayisi):
        self.kişi_sayisi=kişi_sayisi
    def toplam_mevcut(self):
        print("Toplam mevcut= {}".format(self.kişi_sayisi))

birinci_sınıf=Sınıf(25)
ikinci_sınıf=Sınıf(30)
birinci_sınıf.toplam_mevcut()
ikinci_sınıf.toplam_mevcut()