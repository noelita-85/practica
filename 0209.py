class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
   
    
    @property
    def positivo(self):
        if self.precio > 0: 
            return self.precio

Prod1 = Producto("Pc", 100000)  
print(Prod1.positivo)           
            


class Cuenta:

    def __init__(self, titular, cantidad):
        self.titular = titular
        self.cantidad = cantidad

    @property
    def saldo(self):
        return self.cantidad

    def depositar(self, cantidad):
        if cantidad > 0:
            self.cantidad += cantidad
        else:
            print("No se puede depositar una cantidad negativa.")

    def retirar(self, cantidad):
        if cantidad > 0:
            self.cantidad -= cantidad
        else:
            print("No se puede retirar una cantidad negativa.")   

cuenta = Cuenta("Noelia", 10000)

print(cuenta.saldo)

cuenta.depositar(5000)
print(cuenta.saldo)

cuenta.retirar(2000)
print(cuenta.saldo)     


class Empleado:
    def __init__(self, nombre):
        self.nombre = nombre
        
    def trabajar(self):
        print(f"{self.nombre} está trabajando.")

class Programador(Empleado):
    def __init__(self, nombre):
        super().__init__(nombre)
        

class Diseñador(Empleado):
    def __init__(self, nombre):
        super().__init__(nombre)
        
    def trabajar(self):
        print(f"{self.nombre} está diseñando.")   

programador1 = Programador("Juan")
diseñador1 = Diseñador("Ana")

programador1.trabajar()
diseñador1.trabajar()


class rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    @property
    def area(self):
        return self.base * self.altura
    def perimetro(self):
        return 2 * (self.base + self.altura)

a=rectangulo(5, 10)
print(a.area)
print(a.perimetro())

class Motor:
    def __init__(self, tipo):
        self.tipo = tipo
        self.encendido = False

    def arrancar(self):
        if not self.encendido:
            self.encendido = True
            print("El motor está encendido.")
        else:
            print("El motor ya está encendido.")

    def apagar(self):
        if self.encendido:
            self.encendido = False
            print("El motor está apagado.")
        else:
            print("El motor ya está apagado.")        

class Auto:
    def __init__(self, marca, modelo, Motor):
        self.marca = marca
        self.modelo = modelo
        self.Motor = Motor

    def arrancar(self):
        self.Motor.arrancar()

    def apagar(self):
        self.Motor.apagar()

Auto1 = Auto("Toyota", "Corolla", Motor("Nafta"))
Auto1.arrancar()
