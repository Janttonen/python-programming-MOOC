class Tehtava:
    class_id = 0

    def __init__(self, kuvaus: str, koodari: str, tyomaara: int):
        self.__kuvaus = kuvaus
        self.__koodari = koodari
        self.__tyomaara = tyomaara
        self.__valmis = False
        self.__id = self.luo_id()

    def luo_id(self):
        Tehtava.class_id += 1
        return Tehtava.class_id
    
    @property
    def id(self):
        return self.__id

    @property
    def kuvaus(self):
        return self.__kuvaus
    
    @property
    def koodari(self):
        return self.__koodari
    
    @property
    def tyomaara(self):
        return self.__tyomaara

    def on_valmis(self):
        return self.__valmis
    
    def merkkaa_valmiiksi(self):
        self.__valmis = True

    def __str__(self):
        return f'{self.__id}: {self.__kuvaus} ({self.__tyomaara} tuntia), koodari {self.__koodari} {"EI VALMIS" if self.__valmis == False else "VALMIS"}'

class Tilauskirja():
    def __init__(self):
        self.__tilaukset = []

    def lisaa_tilaus(self, kuvaus: str, koodari: str, tyomaara: int):
        self.__tilaukset.append(Tehtava(kuvaus, koodari, tyomaara))
    
    def kaikki_tilaukset(self):
        return self.__tilaukset
    
    def koodarit(self):
        koodarit = [henkilo.koodari for henkilo in self.__tilaukset]
        return list(set(koodarit))

    def merkkaa_valmiiksi(self, id: int):
        for tilaus in self.__tilaukset:
            if tilaus.id == id:
                tilaus.merkkaa_valmiiksi() 
                return
            
        raise ValueError(f'Tilausta ei löytynyt tunnisteella {str(id)}')

    def valmiit_tilaukset(self):
        return [tilaus for tilaus in self.__tilaukset if tilaus.on_valmis() == True]
    
    def ei_valmiit_tilaukset(self):
        return [tilaus for tilaus in self.__tilaukset if tilaus.on_valmis() == False]
        
    def koodarin_status(self, koodari: str):
        # löydä koodari
        koodarin_tehtavat = [henkilo for henkilo in self.__tilaukset if henkilo.koodari == koodari]
        if len(koodarin_tehtavat) == 0:
            raise ValueError('Koodaria ei löytynyt')
        
        # jaottele tilaukset statuksen mukaan
        valmiit = [tilaus for tilaus in koodarin_tehtavat if tilaus.on_valmis() == True]
        ei_valmiit = [tilaus for tilaus in koodarin_tehtavat if tilaus.on_valmis() == False]

        return (len(valmiit), len(ei_valmiit), sum(tilaus.tyomaara for tilaus in valmiit), sum(tilaus.tyomaara for tilaus in ei_valmiit))

if __name__ == '__main__':
        
    tilaukset = Tilauskirja()
    tilaukset.lisaa_tilaus("koodaa webbikauppa", "Antti", 10)
    tilaukset.lisaa_tilaus("tee mobiilisovellus työaikakirjanpitoon", "Antti", 25)
    tilaukset.lisaa_tilaus("tee ohjelma matematiikan harjoitteluun", "Antti", 100)
    tilaukset.lisaa_tilaus("tee uusi facebook", "Erkki", 1000)

    tilaukset.merkkaa_valmiiksi(1)
    tilaukset.merkkaa_valmiiksi(2)

    status = tilaukset.koodarin_status("Antti")
    print(status)
