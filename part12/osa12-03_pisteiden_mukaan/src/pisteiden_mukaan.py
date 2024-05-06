def jarjesta_pisteiden_mukaan(alkiot: list):
    def jarjesta(alkio: dict):
        return alkio['pisteet']
    return sorted(alkiot, key=jarjesta, reverse=True)

if __name__ =='__main__':
    sarjat = [{ "nimi": "Dexter", "pisteet" : 8.6, "kausia":9 }, { "nimi": "Friends", "pisteet" : 8.9, "kausia":10 },  { "nimi": "Simpsons", "pisteet" : 8.7, "kausia":32 }  ]

    print("IMDB:n mukainen pistemäärä")
    for sarja in jarjesta_pisteiden_mukaan(sarjat):
        print(f"{sarja['nimi']}  {sarja['pisteet']}")
