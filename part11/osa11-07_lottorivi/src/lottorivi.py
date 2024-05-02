class Lottorivi:
    def __init__(self, kierros : int, numerot : list):
        self.kierros = kierros
        self.numerot = numerot

    def osumien_maara(self, pelattu_rivi: list):
        return len([numero for numero in pelattu_rivi if numero in self.numerot])
    
    def osumat_paikoillaan(self, pelattu_rivi: list):
        # https://www.geeksforgeeks.org/python-list-comprehension-with-two-lists/
        return [numero if numero == lotto_numero else -1 for numero, lotto_numero in zip(pelattu_rivi,self.numerot)]

if __name__ == '__main__':
    oikea = Lottorivi(8, [1,2,3,10,20,30,33])
    oma_rivi = [1,4,7,10,11,20,30]

    print(oikea.osumat_paikoillaan(oma_rivi))