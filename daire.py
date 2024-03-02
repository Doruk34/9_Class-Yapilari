class Daire():
    from math import pi
    
    def __init__(self,yari_cap=1):
        self.yari_cap = yari_cap
    
    # Method Fonksiyonu

    def cevre_hesaplama(self):
        return 2*self.pi + self.yari_cap
    def alan_hesaplama(self):
        return self.pi * (self.yari_cap)**2

daire1 = Daire()
daire2 = Daire(5)
print(f"Daire 1 Alan: {daire1.alan_hesaplama()} Daire 1 Çevre: {daire1.cevre_hesaplama()} ")

print(f"Daire 2 Alan: {daire2.alan_hesaplama()} Daire 2 Çevre: {daire2.cevre_hesaplama()} ")
