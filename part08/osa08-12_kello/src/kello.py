class Kello:
    def __init__(self, tunnit: int, minuutit: int, sekunnit: int):
        self.sekunnit = sekunnit
        self.minuutit = minuutit
        self.tunnit = tunnit

    def tick(self):

            if (self.sekunnit < 59):
                self.sekunnit += 1
            else:
                if (self.minuutit < 59):
                    self.minuutit += 1
                    self.sekunnit = 0
                else:
                    if (self.tunnit < 23):
                        self.tunnit += 1
                        self.minuutit = 0
                        self.sekunnit = 0
                    else:
                        self.tunnit = 0
                        self.minuutit = 0
                        self.sekunnit = 0

    def aseta(self, tunnit: int, minuutit: int):
        self.tunnit = tunnit
        self.minuutit = minuutit
        self.sekunnit = 0
        
    def __str__(self):
        return f"{self.tunnit:02d}:{self.minuutit:02d}:{self.sekunnit:02d}"
    
if __name__ == '__main__':
    kello = Kello(23, 59, 55)
    print(kello)
    kello.tick()
    print(kello)
    kello.tick()
    print(kello)
    kello.tick()
    print(kello)
    kello.tick()
    print(kello)
    kello.tick()
    print(kello)
    kello.tick()
    print(kello)

    kello.aseta(12, 5)
    print(kello)
