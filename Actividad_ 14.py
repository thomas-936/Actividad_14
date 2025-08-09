print("Actividad 14")

class Competidor:
    def __init__(self, num_dorsal, nombre, edad, categoria):
        self.num_dorsal = num_dorsal
        self.nombre = nombre
        self.edad = edad
        self.categoria = categoria

class SistemaCarrera:
    def menu(self):
        opcion = 0
        while opcion!= 4:
            print("1. Agregar participante")
            print("2. Mostar participantes ordenados por nombre")
            print("3. Mostar participantes ordenados por edad")
            print("4. Salir")