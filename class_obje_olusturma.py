class Kisiler():

    # Class objesi(Attribute)

    adres_bilgisi = "Adres Bilgisi Bulunamadı!"

    def __init__(self,ad,yil):
        self.ad = ad
        self.yil = yil
        print("Yapıcı Methot Oluşturuldu")
 

    # Object

Kisiler1 = Kisiler(ad="İbrahim",yil=1995)

Kisiler2 = Kisiler(ad="Ali",yil=1980)

# veya

Kisiler1 = Kisiler("İbrahim",1995)

Kisiler2 = Kisiler("Ali",1980)

print(Kisiler1)
print(Kisiler2)

# Güncelleme

Kisiler1.ad = "Veli"
Kisiler1.adres_bilgisi = "Kars"

print(Kisiler1.ad)

# print(f"Ad: {Kisiler1.ad} Doğum Yılı: {Kisiler1.yil} Adres: {Kisiler1.adres_bilgisi}")
# print(f"Ad: {Kisiler2.ad} Doğum Yılı: {Kisiler2.yil} Adres: {Kisiler2.adres_bilgisi}")

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"

p1 = Person("John", 36)

print(p1)

class Giris: 
    def __init__(self,adi,mail,sifre,yas): 
        self.adi = adi 
        self.mail = mail 
        self.sifre = sifre 
        self.yas = yas 

    def adi_cagir(self):
        print(f"Adım {self.adi} Mail: {self.mail} sifrem: {self.sifre} yaşım: {self.yas}")

    def mail_cagir(self): 
        return self.mail

k1 = Giris(adi="ahmet",mail="ahmetf@gmail.com",sifre=12324,yas=20)

k1.adi_cagir()

k1.mail_cagir()

