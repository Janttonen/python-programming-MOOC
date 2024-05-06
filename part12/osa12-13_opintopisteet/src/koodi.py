from functools import reduce

class Suoritus:
    def __init__(self, kurssi: str, arvosana: int, opintopisteet: int):
        self.kurssi = kurssi
        self.arvosana = arvosana
        self.opintopisteet = opintopisteet

    def __str__(self):
        return f"{self.kurssi} ({self.opintopisteet} op) arvosana {self.arvosana}"

def kaikkien_opintopisteiden_summa(suoritukset: list):
    return reduce(lambda summa, suoritus: summa + suoritus.opintopisteet, suoritukset, 0)

def hyvaksyttyjen_opintopisteiden_summa(suoritukset: list):
    hyvaksytyt = filter(lambda suoritus: suoritus.arvosana >= 1, suoritukset)
    return reduce(lambda summa, suoritus: summa + suoritus.opintopisteet, hyvaksytyt, 0)

def keskiarvo(suoritukset: list):
    hyvaksytyt = list(filter(lambda suoritus: suoritus.arvosana >= 1, suoritukset))
    return reduce(lambda summa, suoritus: summa + suoritus.arvosana, hyvaksytyt, 0) / len(hyvaksytyt)
    
if __name__ == '__main__':
    s1 = Suoritus("Ohjelmoinnin perusteet", 5, 5)
    s2 = Suoritus("Ohjelmoinnin jatkokutssi", 0, 4)
    s3 = Suoritus("Tietorakenteet ja algoritmit", 3, 10)
    summa = hyvaksyttyjen_opintopisteiden_summa([s1, s2, s3])
    print(summa)

    ka = keskiarvo([s1, s2, s3])
    print(ka)