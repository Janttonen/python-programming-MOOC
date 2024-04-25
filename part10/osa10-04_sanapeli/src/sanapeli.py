import random

class Sanapeli():
    def __init__(self, kierrokset: int):
        self.voitot1 = 0
        self.voitot2 = 0
        self.kierrokset = kierrokset

    def kierroksen_voittaja(self, pelaaja1_sana: str, pelaaja2_sana: str):
        # arvotaan voittaja
        return random.randint(1, 2)

    def pelaa(self):
        print("Sanapeli:")
        for i in range(1, self.kierrokset+1):
            print(f"kierros {i}")
            vastaus1 = input("pelaaja1: ")
            vastaus2 = input("pelaaja2: ")

            if self.kierroksen_voittaja(vastaus1, vastaus2) == 1:
                self.voitot1 += 1
                print("pelaaja 1 voitti")
            elif self.kierroksen_voittaja(vastaus1, vastaus2) == 2:
                self.voitot2 += 1
                print("pelaaja 2 voitti")
            else:
                pass # tasapeli

        print("peli päättyi, voitot:")
        print(f"pelaaja 1: {self.voitot1}")
        print(f"pelaaja 2: {self.voitot2}")

class PisinSana(Sanapeli):
    def __init__(self, kierrokset: int):
        super().__init__(kierrokset)

    def kierroksen_voittaja(self, pelaaja1_sana: str, pelaaja2_sana: str):
        if len(pelaaja1_sana) > len(pelaaja2_sana):
            return 1
        elif len(pelaaja2_sana) > len(pelaaja1_sana):
            return 2
        return

class EnitenVokaaleja(Sanapeli):
    def __init__(self, kierrokset: int):
        super().__init__(kierrokset)

    def kierroksen_voittaja(self, pelaaja1_sana: str, pelaaja2_sana: str):
        #https://www.geeksforgeeks.org/python-program-count-number-vowels-using-sets-given-string/
        vokaalit = "aeiouyåäöAEIOUYÅÄÖ"
        
        vok_pelaaja1 = sum(pelaaja1_sana.count(vokaali) for vokaali in vokaalit)
        vok_pelaaja2 = sum(pelaaja2_sana.count(vokaali) for vokaali in vokaalit)

        if vok_pelaaja1 > vok_pelaaja2:
            return 1
        elif vok_pelaaja2 > vok_pelaaja1:
            return 2
        return

class KiviPaperiSakset(Sanapeli):
    def __init__(self, kierrokset: int):
        super().__init__(kierrokset)

    def kierroksen_voittaja(self, pelaaja1_sana: str, pelaaja2_sana: str):
        #avain on voittaja ja arvoa häviäjä
        sanat = {'kivi': 'sakset', 'sakset': 'paperi', 'paperi': 'kivi'}
        input_sanat = []

        if pelaaja1_sana.lower() != pelaaja2_sana.lower():
            for sana in [pelaaja1_sana.lower(), pelaaja2_sana.lower()]:
                if sana in sanat:
                    input_sanat.append(sana)
                else:
                    input_sanat.append('')
        
            for key, value in sanat.items():
                for sana in input_sanat:
                    for toinen_sana in input_sanat:
                        if sana == key and toinen_sana == value or sana == key and toinen_sana == '':
                            return input_sanat.index(sana) + 1 
            
        return

if __name__ == '__main__':
    p = KiviPaperiSakset(4)
    p.pelaa()
