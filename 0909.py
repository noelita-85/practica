from abc import ABC, abstractmethod

class Personaje(ABC):
    def __init__(self):
        self.atacar = None

    @abstractmethod
    def atacar(self):
        pass

class Guerrero(Personaje):
    def __init__(self):
        super().__init__()
        self.atacar = "Ataca con espada"
class Mago(Personaje):
    def __init__(self):
        super().__init__()
        self.atacar = "Ataca con fuego"

class Arquero(Personaje):
    def __init__(self):
        super().__init__()
        self.atacar = "Ataca con flechas"
        
Personaje=[Guerrero(), Mago(), Arquero()]
print(atacar.Personaje)
 
