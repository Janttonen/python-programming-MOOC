def suodata_kielletyt(merkkijono: str, kielletyt: str):
    return "".join([merkki for merkki in list(merkkijono) if merkki not in list(kielletyt)])

if __name__ == '__main__':
    lause = "Suo! kuokka, ja python: hieno yhdistelmä!??!?!"
    suodatettu = suodata_kielletyt(lause, "!?:,.")
    print(suodatettu)
