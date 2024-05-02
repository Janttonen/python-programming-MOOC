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
            
        raise Exception(f'virheellinen syöte')

    def valmiit_tilaukset(self):
        return [tilaus for tilaus in self.__tilaukset if tilaus.on_valmis() == True]
    
    def ei_valmiit_tilaukset(self):
        return [tilaus for tilaus in self.__tilaukset if tilaus.on_valmis() == False]
        
    def koodarin_status(self, koodari: str):
        koodarin_tehtavat = [henkilo for henkilo in self.__tilaukset if henkilo.koodari == koodari]
        if len(koodarin_tehtavat) == 0:
            raise Exception('virheellinen syöte')
        
        # jaottele tilaukset statuksen mukaan
        valmiit = [tilaus for tilaus in koodarin_tehtavat if tilaus.on_valmis() == True]
        ei_valmiit = [tilaus for tilaus in koodarin_tehtavat if tilaus.on_valmis() == False]

        return (len(valmiit), len(ei_valmiit), sum(tilaus.tyomaara for tilaus in valmiit), sum(tilaus.tyomaara for tilaus in ei_valmiit))

class TilauskirjaSovellus():
    def __init__(self):
        self.__tilauskirja = Tilauskirja()

    def ohje(self):
        print('komennot: ')
        print('0 lopetus')
        print('1 lisää tilaus')
        print('2 listaa valmiit')
        print('3 listaa ei valmiit')
        print('4 merkitse tehtävä valmiiksi')
        print('5 koodarit')
        print('6 koodarin status')
    
    def tilauksen_lisays(self):
            kuvaus = input('kuvaus: ')
            info = input('koodari ja työmääräarvio: ')

            # python find integer from string
            # https://stackoverflow.com/questions/11339210/how-to-get-integer-values-from-a-string-in-python
            tyomaara = ''.join(n for n in info if n.isdigit())
            koodari = ''.join(n for n in info if n.isalpha()).strip()
            
            if kuvaus == '' or koodari == '' or tyomaara == '':
                raise Exception('virheellinen syöte')
            
            self.__tilauskirja.lisaa_tilaus(kuvaus, koodari, int(tyomaara))
            print('lisätty!')

    def listaa_valmiit(self):
        tilaukset = self.__tilauskirja.valmiit_tilaukset()

        if len(tilaukset) == 0:
            print('ei valmiita')
            return
        
        for tilaus in tilaukset:
            print(tilaus)

    def listaa_ei_valmiit(self):
        tilaukset = self.__tilauskirja.ei_valmiit_tilaukset()

        if len(tilaukset) == 0:
            print('lista tyhjä')
            return
        
        for tilaus in tilaukset:
            print(tilaus)

    def merkitse_valmiiksi(self):
        id = input('tunniste: ')

        if id.isnumeric() == False:
            raise Exception('virheellinen syöte')
        
        self.__tilauskirja.merkkaa_valmiiksi(int(id))
        print('merkitty valmiiksi')

    def koodarit(self):
        koodarit = self.__tilauskirja.koodarit()

        for koodari in koodarit:
            print(koodari)

    def koodarin_status(self):
        koodari = input('koodari: ')
        status = self.__tilauskirja.koodarin_status(koodari)
        print(f'työt: valmiina {status[0]} ei valmiina {status[1]}, tunteja: tehty {status[2]} tekemättä {status[3]}')
        

    def suorita(self):
        self.ohje()
        while True:
            try:
                print('')
                komento = input('komento: ')
                if komento == '0':
                    break
                elif komento == '1':
                    self.tilauksen_lisays()
                elif komento == '2':
                    self.listaa_valmiit()
                elif komento == '3':
                    self.listaa_ei_valmiit()
                elif komento =='4':
                    self.merkitse_valmiiksi()
                elif komento == '5':
                    self.koodarit()
                elif komento == '6':
                    self.koodarin_status()
                else:
                    self.ohje()
            except Exception as err:
                print(err)

sovellus = TilauskirjaSovellus()
sovellus.suorita()
