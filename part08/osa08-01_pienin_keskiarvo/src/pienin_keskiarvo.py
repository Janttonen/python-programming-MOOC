def pienin_keskiarvo(henkilo1: dict, henkilo2: dict, henkilo3: dict):
    smallest_avg = {}

    for name in [henkilo1, henkilo2, henkilo3]:
        num = 0

        for key, value in name.items():
            if (key.startswith('tulos')):
                num += value

        avg = num / len(name) - 1
        name['keskiarvo'] = avg

        if not smallest_avg:
            smallest_avg = name.copy()
        
        if name['keskiarvo'] < smallest_avg['keskiarvo']:
            smallest_avg = name.copy()

    smallest_avg.pop('keskiarvo')

    return smallest_avg

if __name__ == '__main__':

    henkilo1 = {"nimi": "Keijo", "tulos1": 2, "tulos2": 3, "tulos3": 3}
    henkilo2 = {"nimi": "Reijo", "tulos1": 5, "tulos2": 1, "tulos3": 8}
    henkilo3 = {"nimi": "Veijo", "tulos1": 3, "tulos2": 1, "tulos3": 1}

    print(pienin_keskiarvo(henkilo1, henkilo2, henkilo3))