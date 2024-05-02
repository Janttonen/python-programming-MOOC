def yleisimmat_sanat(tiedoston_nimi: str, raja: int):
    with open (tiedoston_nimi, encoding="utf-8") as tiedosto:
        sisalto = tiedosto.read()
        sisalto = sisalto.replace("\n", " ").replace(".","").replace(",","").replace("’", "").split(" ")
        return {sana: sisalto.count(sana) for sana in sisalto if sisalto.count(sana) >= raja} 
    
if __name__ == '__main__':
    sanat = yleisimmat_sanat("comprehensions.txt", 3)
    print(sanat)