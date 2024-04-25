class Kurssi():
    def __init__(self, nimi: str):
        self.__nimi = nimi
        self.__arvosana = 0
        self.__op = 0

    def nimi(self):
        return self.__nimi
    
    def arvosana(self):
        return self.__arvosana
    
    def op(self):
        return self.__op
    
    def paivita_arvosana(self, arvosana: int):
       if self.__arvosana < arvosana and arvosana <= 5 and arvosana >= 0:
            self.__arvosana = arvosana

    def paivita_op(self, op: int):
        self.__op = op

    def __str__(self):
        return f'{self.__nimi} ({self.__op} op) arvosana {self.__arvosana}'

class Opintorekisteri():
    def __init__(self):
        self.__suoritukset = {}

    def lisaa_suoritus(self, nimi: str, arvosana: int, op: int):
        if not nimi in self.__suoritukset:
            self.__suoritukset[nimi] = Kurssi(nimi)
            self.__suoritukset[nimi].paivita_op(op)
        self.__suoritukset[nimi].paivita_arvosana(arvosana)
        
    def hae_suoritus(self, nimi: str):
        if not nimi in self.__suoritukset:
            return None
        return self.__suoritukset[nimi]
    
    def kaikki_suoritukset(self):
        return self.__suoritukset

class Tiedonkasittelija():
    def __init__(self, kurssit: dict):
        self.__kurssit = kurssit
        self.__arvosanat = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
        self.__arvosanat_yht = 0
        self.__op_yht = 0
        self.__ka = 0

    def arvosanat(self):
        return self.__arvosanat
    
    def arvosanat_yht(self):
        return self.__arvosanat_yht
    
    def opintopisteet(self):
        return self.__op_yht
    
    def keskiarvo(self):
        return self.__ka
    
    def kasittele(self):
        for kurssi in self.__kurssit:
            self.__op_yht += self.__kurssit[kurssi].op()
            self.__arvosanat_yht += self.__kurssit[kurssi].arvosana()
            self.__arvosanat[self.__kurssit[kurssi].arvosana()] += 1

        self.__ka = self.__arvosanat_yht / len(self.__kurssit)
 
class OpintorekisteriSovellus():
    def __init__(self):
        self.__suoritukset = Opintorekisteri()

    def ohje(self):
        print("1 lisää suoritus")
        print("2 hae suoritus")
        print("3 tilastot")
        print("0 lopetus")
    
    def suorituksen_lisays(self):
        kurssi = input("kurssi: ")
        arvosana = int(input("arvosana: "))
        op = int(input("opintopisteet: "))

        self.__suoritukset.lisaa_suoritus(kurssi, arvosana, op)        

    def haku(self):
        kurssi = input("kurssi: ")
        tiedot = self.__suoritukset.hae_suoritus(kurssi)

        if tiedot == None:
            print("ei suoritusta")
        print(tiedot)

    def tilastot(self):
        kurssit = self.__suoritukset.kaikki_suoritukset()
        tiedot = Tiedonkasittelija(kurssit)
        tiedot.kasittele()
        
        print(f'suorituksia {len(kurssit)} kurssilta, yhteensä {tiedot.opintopisteet()} opintopistettä')
        print(f'keskiarvo {tiedot.keskiarvo():.1f}')
        print(f'arvosanajakauma')

        for arvosana, maara in tiedot.arvosanat().items():
            print(f'{arvosana}: {"x" * maara}')

    def suorita(self):
        self.ohje()
        while True:
            print("")
            komento = input("komento: ")
            if komento == "0":
                break
            elif komento == "1":
                self.suorituksen_lisays()
            elif komento == "2":
                self.haku()
            elif komento == "3":
                self.tilastot()
            else:
                self.ohje()


sovellus = OpintorekisteriSovellus()
sovellus.suorita()
