class Maksukortti:
    def __init__(self, saldo: float):
        self.saldo = saldo

    def lataa_rahaa(self, lisays: float):
        self.saldo += lisays

    def ota_rahaa(self, maara: float):
        if (self.saldo >= maara):
            self.saldo -= maara
            return True
        
        return False

class Kassapaate:
    def __init__(self):
        # kassassa on aluksi 1000 euroa rahaa
        self.rahaa = 1000
        self.edulliset = 0
        self.maukkaat = 0

    def syo_edullisesti(self, maksu: float):
        if (maksu >= 2.5):
            self.rahaa += 2.5
            self.edulliset += 1
            return maksu - 2.5
        
        return maksu

    def syo_maukkaasti(self, maksu: float):
        if (maksu >= 4.3):
            self.rahaa += 4.3
            self.maukkaat += 1
            return maksu - 4.3
        
        return maksu

    def syo_edullisesti_kortilla(self, kortti:Maksukortti):
        if (kortti.saldo >= 2.5):
            self.edulliset += 1
            kortti.saldo -= 2.5
            return True
        
        return False


    def syo_maukkaasti_kortilla(self, kortti:Maksukortti):
        if (kortti.saldo >= 4.3):
            self.maukkaat += 1
            kortti.saldo -= 4.3
            return True
        
        return False

    def lataa_rahaa_kortille(self, kortti: Maksukortti, summa: float):
        self.rahaa += summa
        kortti.saldo += summa


if __name__ == "__main__":
    kortti = Maksukortti(10)
    print("Rahaa", kortti.saldo)
    tulos = kortti.ota_rahaa(8)
    print("Onnistuiko otto:", tulos)
    print("Rahaa", kortti.saldo)
    tulos = kortti.ota_rahaa(4)
    print("Onnistuiko otto:", tulos)
    print("Rahaa", kortti.saldo)

    exactum = Kassapaate()

    antin_kortti = Maksukortti(2)
    print(f"Kortilla rahaa {antin_kortti.saldo} euroa")

    tulos = exactum.syo_maukkaasti_kortilla(antin_kortti)
    print("Riittikö raha:", tulos)

    exactum.lataa_rahaa_kortille(antin_kortti, 100)
    print(f"Kortilla rahaa {antin_kortti.saldo} euroa")

    tulos = exactum.syo_maukkaasti_kortilla(antin_kortti)
    print("Riittikö raha:", tulos)
    print(f"Kortilla rahaa {antin_kortti.saldo} euroa")

    print("Kassassa rahaa", exactum.rahaa)
    print("Edullisia lounaita myyty", exactum.edulliset)
    print("Maukkaita lounaita myyty", exactum.maukkaat)