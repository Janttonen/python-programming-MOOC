class ListaApuri:
    @classmethod
    def suurin_frekvenssi(cls, lista: list):
        alkiot = {}
        for i in lista:
            if i not in alkiot:
                alkiot[i] = 1
            else:
                alkiot[i] += 1

        return max(alkiot, key= alkiot.get)
    
    @classmethod
    def tuplia(cls, lista: list):
        alkiot = {}
        tuplat = 0

        for i in lista:
            if i not in alkiot:
                alkiot[i] = 1
            else:
                alkiot[i] += 1

        for i in alkiot.values():
            if i >= 2:
                tuplat += 1

        return tuplat

if __name__ == '__main__':
    luvut = [1, 1, 2, 1, 3, 3, 4, 5, 5, 5, 6, 5, 5, 5]
    print(ListaApuri.suurin_frekvenssi(luvut))
    print(ListaApuri.tuplia(luvut))
