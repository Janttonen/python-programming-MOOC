class Sekuntikello:
    def __init__(self):
        self.sekunnit = 0
        self.minuutit = 0

    def tick(self):

            if (self.sekunnit < 59):
                self.sekunnit += 1
            else:
                if (self.minuutit < 59):
                    self.minuutit += 1
                    self.sekunnit = 0
                else:
                    self.minuutit = 0
                    self.sekunnit = 0


    def __str__(self):
        return f"{self.minuutit:02d}:{self.sekunnit:02d}"
    
if __name__ == '__main__':
    kello = Sekuntikello()
    for i in range(3600):
        print(kello)
        kello.tick()

        