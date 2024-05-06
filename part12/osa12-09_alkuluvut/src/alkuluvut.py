def alkuluvut():
    luku = 2
    while luku >= 2:
        if tarkista_alkuluku(luku) == True:
            yield luku
        luku += 1

def tarkista_alkuluku(luku: int):
    luvut = [2, 3, 5, 7, 11, 13]
    if luku in luvut:
        return True
    else:
        for i in range(2, luku - 1):
            if luku % i == 0:
                return False
        return True

if __name__ == '__main__':
    luvut = alkuluvut()
    for i in range(10):
        print(next(luvut))
