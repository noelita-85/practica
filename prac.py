class persona:
    def __init__(self, nombre, edad, dni, email, domicilio):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni
        self.email = email
        self.domicilio = domicilio

    def mostrar_informacion(self):
        return f"Nombre: {self.nombre}\nEdad: {self.edad}\nDNI: {self.dni}\nEmail: {self.email}\nDomicilio: {self.domicilio}"


class Estudiante(persona):
    def __init__(self, nombre, edad, dni, email, domicilio, carrera):
        super().__init__(nombre, edad, dni, email, domicilio)
        self.id_estudiante = None
        self.carrera = carrera  

    def regularidad(self):
        if len(self.carrera.materias) > 0:
            print(f" El estudiante {self.nombre} está regular en la carrera {self.carrera.nombre}.")
        else:
            print(f" El estudiante {self.nombre} no está regular en ninguna carrera.")

    def mostrar_informacion(self):
        
        print(super().mostrar_informacion())
        print(f"Carrera elegida: {self.carrera.nombre}") 
        if self.edad >= 18:
            print("El estudiante es mayor de edad.")


class Carrera:
    def __init__(self, nombre, duracion):
        self.nombre = nombre
        self.duracion = duration = duracion
        self.materias = []  
        self.estudiantes = []
        self.titulos = []

    def mostrar_informacion(self):
        print(f"\n--- INFORMACIÓN DE LA CARRERA: {self.nombre} ---")
        print(f"Duración: {self.duracion} años")
        print("Materias asociadas:")
        for m in self.materias:
            print(f"  - {m.nombre} (Código: {m.codigo})")
        print("Estudiantes inscriptos:")
        for e in self.estudiantes:
            print(f"  - {e.nombre}")


class Materia:
    def __init__(self, nombre, codigo, horario):  
        self.nombre = nombre
        self.codigo = codigo
        self.horario = horario
        self.estudiantes = [] 
        self.profesor = []
        self.carrera = []

    def asignar_profesor(self, profesor):
        self.profesor.append(profesor)
        profesor.materias.append(self)

    def inscribir_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)
        if self not in estudiante.carrera.materias:
            estudiante.carrera.materias.append(self)


class Profesor(persona):
    def __init__(self, nombre, carrera):
        super().__init__(nombre, None, None, None, None)
        self.carrera = carrera  
        self.materias = []  

    def mostrar_profesor(self):
        print(f"\nProfesor: {self.nombre} | Especialidad: {self.carrera}")
        print("Materias que dicta:")
        for materia in self.materias:
            print(f"  - {materia.nombre} (Horario: {materia.horario}hs)")


class TiendaUniversitaria:
    def __init__(self):
        
        self.inventario = {
            "Guia de Programacion I": [10, 2500],
            "Apunte de Algebra": [5, 3000],
            "Cuaderno Universitario": [3, 3500]
        }

    def mostrar_inventario(self):
        print("\n--- INVENTARIO ACTUAL ---")
        for producto, datos in self.inventario.items():
            print(f"Producto: {producto} | Stock: {datos[0]} unidades | Precio: ${datos[1]}")

    def realizar_venta(self, estudiante, producto, cantidad):
        print(f"\n--- PROCESANDO VENTA A: {estudiante.nombre} ---")
        if producto in self.inventario:
            stock_actual = self.inventario[producto][0]
            precio = self.inventario[producto][1]
            
            if stock_actual >= cantidad:
                
                self.inventario[producto][0] -= cantidad
                total = precio * cantidad
                print(f" Venta exitosa: {cantidad}x '{producto}'. Total: ${total}")
                print(f" Stock restante de '{producto}': {self.inventario[producto][0]} unidades.")
            else:
                print(f" No se pudo vender. Stock insuficiente de '{producto}' (Disponible: {stock_actual}).")
        else:
            print(f" El producto '{producto}' no existe en la tienda.")

    def realizar_reposicion(self, producto, cantidad):
        print(f"\n--- PROCESANDO REPOSICIÓN ---")
        if producto in self.inventario:
            # Sumar al stock por la reposición
            self.inventario[producto][0] += cantidad
            print(f" Reposición exitosa: Se sumaron {cantidad} unidades a '{producto}'.")
            print(f" Nuevo stock de '{producto}': {self.inventario[producto][0]} unidades.")
        else:
            print(f" El producto '{producto}' no está registrado en el catálogo para reponer.")




print("=== Creando el Sistema Académico ===\n")

carrera_sistemas = Carrera("Ingeniería en Sistemas", 5)
materia1 = Materia("Programación I", "PROG101", 18)
materia2 = Materia("Álgebra", "ALGE202", 14)

carrera_sistemas.materias.append(materia1)
carrera_sistemas.materias.append(materia2)

estudiante1 = Estudiante("Martina", 22, "38444555", "martina@email.com", "Av. Corrientes 1234", carrera_sistemas)
carrera_sistemas.estudiantes.append(estudiante1)
materia1.inscribir_estudiante(estudiante1)

profe_carlos = Profesor("Carlos Gómez", "Sistemas")
materia1.asignar_profesor(profe_carlos)



print("\n--- INFO DEL ESTUDIANTE ---")
estudiante1.mostrar_informacion()

print("\n--- VERIFICACIÓN DE REGULARIDAD ---")
estudiante1.regularidad()



tienda = TiendaUniversitaria()


tienda.mostrar_inventario()


tienda.realizar_venta(estudiante1, "Guia de Programacion I", 3)


tienda.realizar_venta(estudiante1, "Cuaderno Universitario", 5)


tienda.realizar_reposicion("Cuaderno Universitario", 10)


tienda.realizar_venta(estudiante1, "Cuaderno Universitario", 5)


tienda.mostrar_inventario()










