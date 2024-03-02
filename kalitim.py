class Person: 
    def __init__(self,isim,yas):
        self.isim = isim 
        self.yas = yas 

    def bilgiler(self):
        print(f"Adım: {self.isim} yaşım: {self.yas}")

class Ogrenci(Person):
    def __init__(self, isim, yas , okul ):
        super().__init__(isim, yas)
        self.okul = okul 
        
    def bilgiler(self): 
        super().bilgiler()
        print(f"ve ben {self.okul} ' de öğrenciyim. ")


k1 = Ogrenci("Ahmet","19","ABC")
print(k1)
k1.bilgiler()
