class Maksukortti:
    def __init__(self, alkusaldo: float):
        self.saldo = alkusaldo

    def __str__(self):
        return f'Kortilla on rahaa {self.saldo:0.1f} euroa'
    
    def syo_edullisesti(self):
        if (self.saldo >= 2.60):
            self.saldo -= 2.60

    def syo_maukkaasti(self):
        if (self.saldo >= 4.60):
            self.saldo -= 4.60
    
    def lataa_rahaa(self, raha: int):
        if (raha < 0):
            raise ValueError(f'Kortille ei saa ladata negatiivista summaa')
        
        self.saldo += raha



pekan_kortti = Maksukortti(20)
matin_kortti = Maksukortti(30)

pekan_kortti.syo_maukkaasti()
print(f'Pekka: {pekan_kortti}')

matin_kortti.syo_edullisesti()
print(f'Matti: {matin_kortti}')

pekan_kortti.lataa_rahaa(20)
print(f'Pekka: {pekan_kortti}')

matin_kortti.syo_maukkaasti()
print(f'Matti: {matin_kortti}')

pekan_kortti.syo_edullisesti()
pekan_kortti.syo_edullisesti()
print(f'Pekka: {pekan_kortti}')

matin_kortti.lataa_rahaa(50)
print(f'Matti: {matin_kortti}')
