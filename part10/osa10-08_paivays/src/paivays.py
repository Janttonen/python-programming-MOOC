class Paivays:
    def __init__(self, pp: int, kk: int, vv: int):
        self.pp = pp
        self.kk = kk
        self.vv = vv
        # laske kaikki paivat
        self.pp_yht = pp + (kk * 30) + (vv * 360)

    def __str__(self):
        return f'{self.pp}.{self.kk}.{self.vv}'
    
    def __eq__(self, toinen):
        return self.pp_yht == toinen.pp_yht
    
    def __ne__(self, toinen):
        return self.pp_yht != toinen.pp_yht
    
    def __lt__(self, toinen):
        return self.pp_yht < toinen.pp_yht
    
    def __gt__(self, toinen):
        return self.pp_yht > toinen.pp_yht
    
    def __add__(self, pp):
        pp_yht = self.pp_yht + pp
        vv = pp_yht // 360
        kk = (pp_yht - vv * 360) // 30
        pp = pp_yht - (vv * 360) - (kk * 30)

        return Paivays(pp, kk, vv)

    def __sub__(self, toinen):
        return abs(self.pp_yht - toinen.pp_yht)
    
if __name__ == '__main__':
    p1 = Paivays(4, 10, 2020)
    p2 = Paivays(2, 11, 2020)
    p3 = Paivays(28, 12, 1985)

    print(p2-p1)
    print(p1-p2)
    print(p1-p3)