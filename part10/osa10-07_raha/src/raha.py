class Raha:
    def __init__(self, eurot: int, sentit: int):
        self.__eurot = eurot
        self.__sentit = sentit

    def __str__(self):
        return f"{self.__eurot}.{self.__sentit:02d} eur"
    
    def __eq__(self, toinen):
        return (self.__eurot, self.__sentit) == (toinen.__eurot, toinen.__sentit)
    
    def __ne__(self, toinen):
        return (self.__eurot, self.__sentit) != (toinen.__eurot, toinen.__sentit)
    
    def __lt__(self, toinen):
        return (self.__eurot, self.__sentit) < (toinen.__eurot, toinen.__sentit)
    
    def __gt__(self, toinen):
        return (self.__eurot, self.__sentit) > (toinen.__eurot, toinen.__sentit)
    
    def __add__(self, toinen):
        # miten kannattaa tehää
        return
    
    def __add__(self, toinen):
        if self.__lt__(toinen) == True:
            raise ValueError(f"negatiivinen tulos ei sallittu")
        

if __name__ == '__main__':
    e1 = Raha(4, 5)
    e2 = Raha(2, 95)

    e3 = e1 + e2
    #e4 = e1 - e2

    print(e3)