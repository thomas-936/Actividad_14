print("Actividad 14")

class Competidor:
    def __init__(self, num_dorsal, nombre, edad, categoria):
        self.num_dorsal = num_dorsal
        self.nombre = nombre
        self.edad = edad
        self.categoria = categoria

    def __str__(self):
        return (f"Número de dorsal: {self.num_dorsal}|"
                f"Nombre del competidor: {self.nombre}|"
                f"Edad del competidor: {self.edad}|"
                f"Categoria del competidor: {self.categoria}")

class SistemaCarrera:
    def __init__(self):
        self.competidores= {}

    def agregar_competidor(self):
        cantidad = int(input("Ingrse la cantidad de competidores que desea registrar: "))
        for i in range(cantidad):
            print(f"Competirdor {i+1}")
            num_dorsal = int(input("Ingrese el número de dorsal del competodor: "))
            if num_dorsal in self.competidores:
                print("")




    def menu(self):
        opcion = 0
        while opcion!= 4:
            print("1. Agregar participante")
            print("2. Mostar participantes ordenados por nombre")
            print("3. Mostar participantes ordenados por edad")
            print("4. Salir")
            try:
                opcion = int(input("Ingrese la opción que desea: "))
            except ValueError:
                print("Ingrase un dato valido")