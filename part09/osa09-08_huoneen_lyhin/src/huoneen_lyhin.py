class Henkilo:
    def __init__(self, nimi: str, pituus: int):
        self.nimi = nimi
        self.pituus = pituus

    def __str__(self):
        return f'{self.nimi} ({self.pituus} cm)'

class Huone:
    def __init__(self):
        self.henkilot = []
    
    def lisaa(self, henkilo: Henkilo):
        self.henkilot.append(henkilo)
    
    def on_tyhja(self):
        if (len(self.henkilot) > 0):
            return False
        return True
    
    def tulosta_tiedot(self):
        yhteis_pituus = 0
        for henkilo in self.henkilot:
            yhteis_pituus += henkilo.pituus
        
        print(f'Huoneessa {len(self.henkilot)} henkilöä, yhteispituus {yhteis_pituus} cm')

        for henkilo in self.henkilot:
            print(henkilo)
    
    def lyhin(self):
        if (self.on_tyhja() == False):
            lyhin = self.henkilot[0]

            for henkilo in self.henkilot:
                if (henkilo.pituus < lyhin.pituus):
                    lyhin = henkilo

            return lyhin
        return None
    
    def poista_lyhin(self):
        if (self.on_tyhja() == False):
            lyhin_henkilo = self.lyhin()
            self.henkilot.pop(self.henkilot.index(lyhin_henkilo))
            return lyhin_henkilo
        return None
    
if __name__ == '__main__':
    huone = Huone()

    huone.lisaa(Henkilo("Lea", 183))
    huone.lisaa(Henkilo("Kenya", 182))
    huone.lisaa(Henkilo("Nina", 172))
    huone.lisaa(Henkilo("Auli", 186))
    huone.tulosta_tiedot()

    print()

    poistettu = huone.poista_lyhin()
    print(f"Otettiin huoneesta {poistettu.nimi}")

    print()

    huone.tulosta_tiedot()
