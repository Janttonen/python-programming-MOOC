class Sarja:
    def __init__(self, nimi: str, kaudet: int, genret: list):
        self.nimi = nimi
        self.kaudet = kaudet
        self.genret = genret
        self.arvostelut = []

    def arvostele(self, arvosana: int):
        if (arvosana >= 0) and (arvosana <= 5):
            self.arvostelut.append(arvosana)
    
    def __str__(self):
        arvostelut = ''

        if (len(self.arvostelut) == 0):
            arvostelut = 'ei arvosteluja'
        else:
            arvostelut = f'arvosteluja {len(self.arvostelut)}, keskiarvo {(sum(self.arvostelut) / len(self.arvostelut)):0.1f} pistettä'

        return f'{self.nimi} ({self.kaudet} esityskautta)\ngenret: {", ".join(self.genret)}\n{arvostelut}'


def arvosana_vahintaan(arvosana: float, sarjat: list):
    ok_sarjat = []

    for sarja in sarjat:
        if(sum(sarja.arvostelut) >= arvosana):
            ok_sarjat.append(sarja)

    return ok_sarjat

def sisaltaa_genren(genre: str, sarjat: list):
    ok_sarjat = []

    for sarja in sarjat:
        if genre in sarja.genret:
            ok_sarjat.append(sarja)

    return ok_sarjat

if __name__ =='__main__':
    s1 = Sarja("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
    s1.arvostele(5)

    s2 = Sarja("South Park", 24, ["Animation", "Comedy"])
    s2.arvostele(3)

    s3 = Sarja("Friends", 10, ["Romance", "Comedy"])
    s3.arvostele(2)

    sarjat = [s1, s2, s3]

    print("arvosana vähintään 4.5:")
    for sarja in arvosana_vahintaan(4.5, sarjat):
        print(sarja.nimi)

    print("genre Comedy:")
    for sarja in sisaltaa_genren("Comedy", sarjat):
        print(sarja.nimi)
