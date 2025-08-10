print("Actividad 14")

class Competidor:
    def __init__(self, num_dorsal, nombre, edad, categoria):
        self.num_dorsal = num_dorsal
        self.nombre = nombre
        self.edad = edad
        self.categoria = categoria

    def __str__(self):
        return (f"Número de dorsal: {self.num_dorsal}|  "
                f"Nombre del competidor: {self.nombre}|  "
                f"Edad del competidor: {self.edad}   |"
                f"Categoria del competidor: {self.categoria}")

class SistemaCarrera:
    def __init__(self):
        self.competidores= {}

    def pedir_entero(self, mensaje):
        while True:
            try:
                return int(input(mensaje))
            except ValueError:
                print("Ingrse un número válido.... ")


    def busqueda_secuencial(self, objetivo):
        lista = list(self.competidores.values())
        for i in range(len(lista)):
            if lista[i].objetivo.lower() == objetivo.lower():
                return i
            else:
                return -1




    def agregar_competidor(self):
        try:
            cantidad = self.pedir_entero("Ingrese la cantidad de competidores que desea registrar: ")

            for i in range(cantidad):
                print("\n----------------------------------------------------")
                print(f"Competirdor {i+1}")
                while True:
                    num_dorsal = self.pedir_entero("Ingrese le número de Dorsal del competidor: ")
                    if num_dorsal in self.competidores:
                        print("Este competidor ya ha sido registrado... :) ")
                    else:
                        break
                nombre = input("Ingrese el nombre del competidor: ")
                edad = self.pedir_entero("Ingrese la edad del competidor: ")
                categoria = input("Ingrese la categoria del competidor: ")
                self.competidores[num_dorsal] = Competidor(num_dorsal, nombre, edad, categoria)

        except ValueError:
            print("Ingrese un dato valido... :)")


    def sort_nombres(self, lista):
        if len(lista) <= 1:
            return lista

        pivote = lista[0]
        menores = [x for x in lista[1:] if x.nombre.lower() < pivote.nombre.lower()]
        iguales = [x for x  in lista if x.nombre.lower() == pivote.nombre.lower()]
        mayores = [x for x in lista[1:] if x.nombre.lower() > pivote.nombre.lower()]

        return self.sort_nombres(menores) + iguales + self.sort_nombres(mayores)

    def sort_edades(self, lista):
        if len(lista) <= 1:
            return lista

        pivote = lista[0]
        menores = [e for e in lista if e.edad < pivote.edad]
        iguales =  [e for e in lista if e.edad == pivote.edad]
        mayores = [e for e in lista if e.edad > pivote.edad]

        return self.sort_edades(menores) + iguales + self.sort_edades(mayores)

    def menu(self):
        opcion = 0
        while opcion!= 4:
            print("\n++MENU++")
            print("1. Agregar participante")
            print("2. Mostar participantes ordenados por nombre")
            print("3. Mostar participantes ordenados por edad")
            print("4. Salir")
            try:
                opcion = int(input("Ingrese la opción que desea: "))
            except ValueError:
                print("Ingrese un dato valido")
                continue

            match opcion:
                case 1:
                    self.agregar_competidor()
                case 2:
                    lista_ordenada = self.sort_nombres(list(self.competidores.values()))
                    for comperidor in lista_ordenada:
                        print(comperidor)
                case 3:
                    edades_ordenadas= self.sort_edades(list(self.competidores.values()))
                    for edad in edades_ordenadas:
                        print(edad)
                case 4:
                    print("Saliendo del programa... ")


SistemaCarrera().menu()