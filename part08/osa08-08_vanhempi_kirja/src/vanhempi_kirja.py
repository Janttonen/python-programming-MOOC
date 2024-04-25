# ÄLÄ MUUTA ALLA OLEVAA LUOKKAA Kirja
# Kirjoita ratkaisui Kirja-luokan jälkeen

class Kirja:
    def __init__(self, nimi: str, kirjoittaja: str, genre: str, kirjoitusvuosi: int):
        self.nimi = nimi
        self.kirjoittaja = kirjoittaja
        self.genre = genre
        self.kirjoitusvuosi = kirjoitusvuosi


def vanhempi_kirja(kirja1: Kirja, kirja2: Kirja):
    vanhempi_kirja = None

    if (kirja1.kirjoitusvuosi < kirja2.kirjoitusvuosi):
        vanhempi_kirja = kirja1
    elif (kirja2.kirjoitusvuosi < kirja1.kirjoitusvuosi):
        vanhempi_kirja = kirja2
    else:
        print(f'{kirja1.nimi} ja {kirja2.nimi} kirjoitettiin vuonna {kirja1.kirjoitusvuosi}')
        return
   
    print(f'{vanhempi_kirja.nimi} on vanhempi, se kirjoitettiin {vanhempi_kirja.kirjoitusvuosi}')

if __name__ =='__main__':
    python = Kirja("Fluent Python", "Luciano Ramalho", "ohjelmointi", 2015)
    everest = Kirja("Huipulta huipulle", "Carina Räihä", "elämänkerta", 2010)
    norma = Kirja("Norma", "Sofi Oksanen", "rikos", 2015)

    vanhempi_kirja(python, everest)
    vanhempi_kirja(python, norma)
