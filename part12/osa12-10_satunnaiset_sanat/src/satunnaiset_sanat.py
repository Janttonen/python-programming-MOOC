import random

def sanageneraattori(kirjaimet: str, pituus: int, maara: int):
    sanat = 0
    while sanat < maara: 
        sana = ''
        for x in range(pituus):
            sana += (kirjaimet[random.randint(0, len(kirjaimet) - 1)])
        yield sana
        sanat += 1

if __name__ == '__main__':
    sanagen = sanageneraattori("abcdefg", 3, 5)
    for sana in sanagen:
        print(sana)
