def parilliset(alku: int, maksimi: int):
    while alku <= maksimi:
        if alku % 2 == 0:
            yield alku
            alku += 2
        else:
            alku += 1

if __name__ == '__main__':
    luvut = parilliset(2, 10)
    for luku in luvut:
        print(luku)