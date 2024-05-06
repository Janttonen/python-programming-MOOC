import json

class Pelaaja():
    def __init__(self, nimi: str, kansalaisuus: str, syotot: int, maalit: int, rangaistukset: int, joukkue: str, pelit: int):
        self.__nimi = nimi
        self.__kansalaisuus = kansalaisuus
        self.__syotot = syotot
        self.__maalit = maalit
        self.__rangaistukset = rangaistukset
        self.__joukkue = joukkue
        self.__pelit = pelit

    @property
    def nimi(self):
        return self.__nimi
    
    @property
    def kansalaisuus(self):
        return self.__kansalaisuus

    @property
    def syotot(self):
        return self.__syotot
    
    @property
    def maalit(self):
        return self.__maalit
    
    @property
    def rangaistukset(self):
        return self.__rangaistukset

    @property
    def joukkue(self):
        return self.__joukkue

    @property
    def pelit(self):
        return self.__pelit

    def __str__(self):
        return f'{self.__nimi:21}{self.__joukkue:3}{self.__maalit:4} + {self.__syotot:2} = {(self.__maalit+self.__syotot):3}'

class Tilasto():
    def __init__(self):
        self.__pelaajat = []

    def lue_tiedosto(self, tiedosto: str):
        with open(tiedosto) as file:
            data = file.read()
        return json.loads(data)

    def lisaa_pelaajat(self, pelaajat: list):
        for pelaaja in pelaajat:
            p = Pelaaja(pelaaja['name'], pelaaja['nationality'], pelaaja['assists'], pelaaja['goals'], pelaaja['penalties'], pelaaja['team'], pelaaja['games'])
            self.__pelaajat.append(p)

    def hae_pelaaja(self):
        nimi = input('nimi: ')
        for p in self.__pelaajat:
            if p.nimi == nimi:
                print(p)

    def hae_joukkueet(self):
        joukkueet = set(list(map(lambda p: p.joukkue, self.__pelaajat)))
        for joukkue in sorted(joukkueet):
            print(joukkue)

    def hae_maat(self):
        maat = set(list(map(lambda p: p.kansalaisuus, self.__pelaajat)))
        for maa in sorted(maat):
            print(maa)

    def hae_joukkueen_pelaajat(self):
        joukkue = input('joukkue: ')
        pelaajat = list(filter(lambda p: p.joukkue == joukkue, self.__pelaajat))
        for pelaaja in sorted(pelaajat, key=lambda p: (p.syotot + p.maalit), reverse = True):
            print(pelaaja)

    def hae_maan_pelaajat(self):
        maa = input('maa: ')
        pelaajat = list(filter(lambda p: p.kansalaisuus == maa, self.__pelaajat))
        for pelaaja in sorted(pelaajat, key=lambda p: (p.syotot + p.maalit), reverse = True):
            print(pelaaja)

    def eniten_pisteita(self):
        maara = int(input('kuinka monta: '))
        pelaajat = sorted(self.__pelaajat, key=lambda p: ((p.syotot + p.maalit), p.maalit), reverse = True)
        for i in range(0, maara):
            print(pelaajat[i])

    def eniten_maaleja(self):
        maara = int(input('kuinka monta: '))
        # https://stackoverflow.com/questions/37693373/how-to-sort-a-list-with-two-keys-but-one-in-reverse-order
        pelaajat = sorted(self.__pelaajat, key=lambda p: (p.maalit, -p.pelit), reverse = True)
        for i in range(0, maara):
            print(pelaajat[i])
            
class TilastoSovellus():
    def __init__(self):
        self.__tilasto = Tilasto()

    def ohje(self):
        print()
        print('komennot: ')
        print('0 lopeta')
        print('1 hae pelaaja')
        print('2 joukkueet')
        print('3 maat')
        print('4 joukkueen pelaajat')
        print('5 maan pelaajat')
        print('6 eniten pisteitä')
        print('7 eniten maaleja')

    def suorita(self):
        if True:
            tiedosto = input('tiedosto: ')
        else:
            tiedosto = "osa.json"

        kaikki_pelaajat = self.__tilasto.lue_tiedosto(tiedosto)
        print(f'luettiin {len(kaikki_pelaajat)} pelaajan tiedot')
        self.__tilasto.lisaa_pelaajat(kaikki_pelaajat)

        while True:
            self.ohje()
            print()
            komento = input('komento: ')

            if komento == '0':
                break
            elif komento == '1':
                self.__tilasto.hae_pelaaja()
            elif komento == '2':
                self.__tilasto.hae_joukkueet()
            elif komento == '3':
                self.__tilasto.hae_maat()
            elif komento == '4':
                self.__tilasto.hae_joukkueen_pelaajat()
            elif komento == '5':
                self.__tilasto.hae_maan_pelaajat()
            elif komento == '6':
                self.__tilasto.eniten_pisteita()
            elif komento == '7':
                self.__tilasto.eniten_maaleja()
            else:
                self.ohje()

sovellus = TilastoSovellus()
sovellus.suorita()

