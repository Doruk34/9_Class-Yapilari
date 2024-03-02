class Merhaba():
    print("Merhaba Python")

Merhaba

liste1 = [1,2,3,4]
sonuc = type(liste1)
print(sonuc)

liste1.append(5)

class Kisiler():
    print("merhaba")
    def info():
        ad = input("Adınız: ")
        soyad = input("Soyadınız: ")
    def baska_birsey():
        pass
    
Kisiler1 = Kisiler
Kisiler2 = Kisiler

print(type(Kisiler1))
print(type(Kisiler2))

print(Kisiler1==Kisiler2)

# print(Kisiler1.info())
Kisiler1.info()

# Kisiler()
