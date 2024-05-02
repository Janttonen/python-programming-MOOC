import math

def neliojuuret(luvut: list):
    return [math.sqrt(luku) for luku in luvut]


if __name__ == '__main__':
    rivit = neliojuuret([1,2,3,4])
    for rivi in rivit:
        print(rivi)
