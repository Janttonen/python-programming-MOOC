def vokaalilla_alkavat(sanat: list):
    return [sana for sana in sanat if sana[0].lower() in ["a", "e", "i", "o", "u", "y", "ä", "ö"]]

if __name__ == '__main__':
    klista = ["auto","mopo","Etana","kissa","Koira","OMENA","appelsiini"]
    for vok in vokaalilla_alkavat(klista):
        print(vok)
