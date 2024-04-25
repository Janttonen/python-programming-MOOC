class Pankkitili:
    def __init__(self, omistaja: str, tilinro: str, saldo: float):
        self.__omistaja = omistaja
        self.__tilinro = tilinro
        self.__saldo = saldo

    def __palvelumaksu(self):
        self.__saldo *= 0.99

    def talleta(self, summa: float):
        if summa > 0:
            self.__saldo += summa
            self.__palvelumaksu()

    def nosta(self, summa: float):
        if summa > 0 and summa <= self.__saldo:
            self.__saldo -= summa
            self.__palvelumaksu()

    @property
    def saldo(self):
        return self.__saldo
    
if __name__ == '__main__':
    tili = Pankkitili("Raimo Rahakas", "12345-6789", 1000)
    tili.nosta(100)
    print(tili.saldo)
    tili.talleta(100)
    print(tili.saldo)



