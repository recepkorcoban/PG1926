def kullanıcıadı(mail_ad):
   kullanıcı_adı=mail_ad[0:mail_ad.index("@"):1]
   y=list(kullanıcı_adı)
   alfabe = "abcçdefgğhıijklmnoöprsştuüvyz"
   harf_listesi = list(alfabe)
   rakamlar = list(range(10))
   sartlar=["_","-"]
   for karakter in y:
    if karakter in sartlar:
        return True
    else:
        return False

def website_adı(mail_ad):
    website_konumu=mail_ad[mail_ad.index("@")+1:mail_ad.index("."):1]
    sartla_1=['a','b',"c","ç","d","e","f","g","ğ","h","ı","i","j","k","l","m","n","o","ö","p","r","s","ş","t","u","ü","v","y","z","0","1","2","3","4","5","6","7","8","9"]
    for a in website_konumu:
        if a in sartla_1:
            return True
        else:
            return False

def mail_dogrulama():
   
    if kullanıcıadı(mail_ad) == t:
        print("Mail adresiniz doğrudur.")
    else:
        print("Mail adresiniz yanlıştır.")

print("*"*15,"MAİL ADRESİ DOĞRULAMA","*"*15)
siteuzantısı=int(input("uzantı uzunluğunu giriniz: "))
mail_ad=input("Mail adresini giriniz: ")
kullanıcıadı(mail_ad)
t,f=True,False
type(kullanıcıadı)
mail_dogrulama()