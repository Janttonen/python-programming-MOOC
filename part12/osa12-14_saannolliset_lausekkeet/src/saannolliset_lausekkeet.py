import re

def on_viikonpaiva(merkkijono: str):
    hyvaksytyt = "ma|ti|ke|to|pe|la|su"

    if re.search(merkkijono, hyvaksytyt):
        return True
    return False

def kaikki_vokaaleja(merkkijono: str):
    hyvaksytyt = "[aeiouyåäöAEIOUYÅÄÖ]"

    for m in merkkijono:
        if re.search(m, hyvaksytyt):
            continue
        else:
            return False
    return True

def kellonaika(merkkijono: str):
    hyvaksytyt = "^([0-1][0-9]|[2][0-4]):[0-5][0-9]:[0-5][0-9]$"

    if re.search(hyvaksytyt, merkkijono):
        return True
    return False

if __name__ == '__main__':
    print(on_viikonpaiva("ma"))
    print(on_viikonpaiva("pe"))
    print(on_viikonpaiva("tu"))

    print()

    print(kaikki_vokaaleja("eioueioieoieouyyyy"))
    print(kaikki_vokaaleja("autoooo"))

    print()

    print(kellonaika("17:43:01"))
    print(kellonaika("AB:01:CD"))
    print(kellonaika("17:59:59"))
    print(kellonaika("33:66:77"))