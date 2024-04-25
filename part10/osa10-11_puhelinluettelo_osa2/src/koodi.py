class Henkilo():
    def __init__(self, nimi: str):
        self.__nimi = nimi
        self.__numerot = []
        self.__osoite = None

    def nimi(self):
        return self.__nimi
    
    def numerot(self):
        return self.__numerot
    
    def osoite(self):
        return self.__osoite

    def lisaa_numero(self, numero: str):
        if not numero in self.__numerot:
            self.__numerot.append(numero)

    def lisaa_osoite(self, osoite: str):
        if self.__osoite == None and len(osoite) > 0:
            self.__osoite = osoite

    def __str__(self):
        return f"{', '.join(self.__numerot) if len(self.__numerot) > 0 else 'numero ei tiedossa'}\n{self.__osoite if self.__osoite != None else 'osoite ei tiedossa'}"
    
class Puhelinluettelo:
    def __init__(self):
        self.__henkilot = {}

    def hae_tiedot(self, nimi: str):
        if not nimi in self.__henkilot:
            return None
        return self.__henkilot[nimi]
    
    def lisaa_numero(self, nimi: str, numero: str):
        if not nimi in self.__henkilot:
            self.__henkilot[nimi] = Henkilo(nimi)

        self.__henkilot[nimi].lisaa_numero(numero)

    def lisaa_osoite(self, nimi: str, osoite: str):
        if not nimi in self.__henkilot:
            self.__henkilot[nimi] = Henkilo(nimi)

        self.__henkilot[nimi].lisaa_osoite(osoite)

    def kaikki_tiedot(self):
        return self.__henkilot

class PuhelinluetteloSovellus:
    def __init__(self):
        self.__luettelo = Puhelinluettelo()

    def ohje(self):
        print("komennot: ")
        print("0 lopetus")
        print("1 numeron lisäys")
        print("2 haku")
        print("3 osoitteen lisäys")

    def numeron_lisays(self):
        nimi = input("nimi: ")
        numero = input("numero: ")
        self.__luettelo.lisaa_numero(nimi, numero)

    def osoitteen_lisays(self):
        nimi = input("nimi: ")
        osoite = input("osoite: ")
        self.__luettelo.lisaa_osoite(nimi, osoite)

    def haku(self):
        nimi = input("nimi: ")
        henkilo = self.__luettelo.hae_tiedot(nimi)
        
        if henkilo == None:
            print("numero ei tiedossa")
            print("osoite ei tiedossa")
        print(henkilo)
        
    def suorita(self):
        self.ohje()
        while True:
            print("")
            komento = input("komento: ")
            if komento == "0":
                break
            elif komento == "1":
                self.numeron_lisays()
            elif komento == "2":
                self.haku()
            elif komento == "3":
                self.osoitteen_lisays()
            else:
                self.ohje()


# kun testaat, mitään muuta koodia ei saa olla luokkien ulkopuolella kuin seuraavat rivit
sovellus = PuhelinluetteloSovellus()
sovellus.suorita()
