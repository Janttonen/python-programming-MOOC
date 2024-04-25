# Tee ratkaisusi tähän:
class  Lukutilasto:
    def __init__(self):
        self.lukuja = 0
        self.lukujen_summa = 0

    def lisaa_luku(self, luku:int):
        self.lukuja += 1
        self.lukujen_summa += luku

    def lukujen_maara(self):
        return self.lukuja

    def summa(self):
        return self.lukujen_summa
    
    def keskiarvo(self):
        if (self.lukujen_summa != 0) and (self.lukuja != 0):
            return self.lukujen_summa / self.lukuja
    

tilasto1 = Lukutilasto() 
tilasto_parilliset = Lukutilasto()
tilasto_parittomat = Lukutilasto()

print('Anna lukuja:')
while(True):
    luku = int(input())

    if luku == -1:
        print(f'Summa: {tilasto1.summa()}')
        print(f'Keskiarvo: {tilasto1.keskiarvo()}')
        print(f'Parillisten summa: {tilasto_parilliset.summa()}')
        print(f'Parittomien summa: {tilasto_parittomat.summa()}')
        break

    if (luku % 2 == 0):
        tilasto_parilliset.lisaa_luku(luku)
    else:
        tilasto_parittomat.lisaa_luku(luku)

    tilasto1.lisaa_luku(luku)