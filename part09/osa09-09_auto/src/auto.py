class Auto:
    def __init__(self):
        self.__tankki_litrat = 0
        self.__ajetut_km = 0

    def tankkaa(self):
        self.__tankki_litrat = 60

    def aja(self, km:int):
        for i in range(km):
            if (self.__tankki_litrat > 0):
                self.__tankki_litrat -= 1
                self.__ajetut_km += 1

    def __str__(self):
        return f'Auto: ajettu {self.__ajetut_km} km, bensaa {self.__tankki_litrat} litraa'
    
if __name__ == '__main__':
    auto = Auto()
    print(auto)
    auto.tankkaa()
    print(auto)
    auto.aja(20)
    print(auto)
    auto.aja(50)
    print(auto)
    auto.aja(10)
    print(auto)
    auto.tankkaa()
    auto.tankkaa()
    print(auto)