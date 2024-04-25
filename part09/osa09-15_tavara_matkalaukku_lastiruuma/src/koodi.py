class Tavara:
    def __init__(self, nimi: str, paino: int):
        self.__nimi = nimi
        self.__paino = paino

    def nimi(self):
        return self.__nimi

    def paino(self):
        return self.__paino
    
    def __str__(self):
        return f'{self.__nimi} ({self.__paino} kg)'
    
class Matkalaukku:
    def __init__(self, max_paino: int):
        self.__max_paino = max_paino
        self.__tavarat = []

    def lisaa_tavara(self, tavara: Tavara):
        if (tavara.paino() + self.paino()) <= self.__max_paino:
            self.__tavarat.append(tavara)
        return
    
    def raskain_tavara(self):
        if len(self.__tavarat) > 0:
            raskain = self.__tavarat[0]
            for i in self.__tavarat:
                if i.paino() > raskain.paino():
                    raskain = i

            return raskain
        return None
    
    def tulosta_tavarat(self):
        for i in self.__tavarat:
            print(i)

    def paino(self):
        paino = 0
        for i in self.__tavarat:
            paino += i.paino()

        return paino

    def __str__(self):
        return f'{len(self.__tavarat)} tavara ({self.paino()} kg)' if len(self.__tavarat) == 1 else f'{len(self.__tavarat)} tavaraa ({self.paino()} kg)'

class Lastiruuma:
    def __init__(self, max_paino: int):
        self.__max_paino = max_paino
        self.__matkalaukut = []

    def lisaa_matkalaukku(self, matkalaukku: Matkalaukku):
        if (matkalaukku.paino() + self.paino()) <= self.__max_paino:
            self.__matkalaukut.append(matkalaukku)

        return
    
    def paino(self):
        paino = 0
        for i in self.__matkalaukut:
            paino += i.paino()

        return paino
    
    def tulosta_tavarat(self):
        for i in self.__matkalaukut:
            i.tulosta_tavarat()

    def __str__(self):
        return f'{len(self.__matkalaukut)} matkalaukku, tilaa {self.__max_paino - self.paino()} kg' if len(self.__matkalaukut) == 1 else f'{len(self.__matkalaukut)} matkalaukkua, tilaa {self.__max_paino - self.paino()} kg'
    
if __name__ == '__main__':
    kirja = Tavara("Aapiskukko", 2)
    puhelin = Tavara("Nokia 3210", 1)
    tiiliskivi = Tavara("Tiiliskivi", 4)

    adan_laukku = Matkalaukku(10)
    adan_laukku.lisaa_tavara(kirja)
    adan_laukku.lisaa_tavara(puhelin)

    pekan_laukku = Matkalaukku(10)
    pekan_laukku.lisaa_tavara(tiiliskivi)

    lastiruuma = Lastiruuma(1000)
    lastiruuma.lisaa_matkalaukku(adan_laukku)
    lastiruuma.lisaa_matkalaukku(pekan_laukku)

    print("Ruuman matkalaukuissa on seuraavat tavarat:")
    lastiruuma.tulosta_tavarat()