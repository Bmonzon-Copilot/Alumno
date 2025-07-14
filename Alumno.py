class Estudiante:  #Clase Estudiante
    def __init__(self, nombre, carnet, carrera): #Costructor
        self.__nombre = nombre
        self.__carnet = carnet
        self.__carrera = carrera
        self.__notas = []
        self.__nota_final = None

    def __str__(self):
        resultado = (
            f"Nombre: {self.__nombre}, Carné: {self.__carnet}, Carrera: {self.__carrera}, "
        )

        if self.__notas:
            resultado += f", Notas: {self.__notas}, Nota Final (Promedio): {self.__nota_final:.2f}"
        else:
            resultado += ",Notas: ---"
        return resultado

def ingresar_notas():
    notas = []
    for i in range(1, 4):
        try:
            nota = float(input(f"Ingrese la nota #{i}: "))
            if nota >= 60 or nota <= 100:
                print("La nota debe estar entre 60 y 100.")
                return None
            notas.append(nota)
        except ValueError:
            print("La nota debe ser un número.")
            return None
    return notas

class SistemaEstudiante:
    def __init__(self):
        self.estudiantes=[]

    def existe_carnet(self,carnet):
        return any(est.carnet == carnet for est in self.estudiantes)

    def encuentra_estudiante(self, carnet):
        for est in self.estudiantes:
            if est.carnet == carnet:
                return  est
        return  None


    def registrar_estudiante(self):
        nombre = input("Ingrese Nombre: ")
        carnet = input("Ingrese carnet: ")

        if self.existe_carnet(carnet):
            print("El carnet ya existe...")
            return

        carrera = input("Ingrese carrera: ")

        estudiante = Estudiante(nombre,carnet,carrera)
        self.estudiantes.append(estudiante)
        print("Estudiante Registrado...")

    def ingreso_notas(self):
        carnet= input("Ingrese Carnet: ")
        estudiante= self.encuentra_estudiante(carnet)

        if estudiante is None:
            print("Estudiante no encontrado...")
            return

        notas= ingresar_notas()
        if notas is None:
            print("Notas no ingresadas correctamente...")
            return

        estudiante.notas=notas
        estudiante.nota_final = sum(notas) / len(notas)
        print("Notas ingresadas correctamente...")


    def mostrar_estudiante(self):
        if not self.estudiantes:
            print("No hay estudiantes ingresados...")
            return
        print("LISTADO: ")
        for estudiante in self.estudiantes:
            print(estudiante)
        print()

    def buscar_estudiante(self):
        carnet = input("Buscar estudiante (Ingrese Carnet): ")
        estudiante= self.encuentra_estudiante(carnet)
        if estudiante:
            print("Estudiante encontrado:")
            print(estudiante)
            return
        else:
            print("Estudiante no registrado\n")

def menu():
        sistema= SistemaEstudiante()

        while True:
            print("===== Sistema de Estudiantes =====")
            print("1. Registrar nuevo estudiante")
            print("2. Ingresar notas y calcular promedio")
            print("3. Mostrar todos los estudiantes")
            print("4. Buscar estudiante por carné")
            print("5. Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                sistema.registrar_estudiante()
            elif opcion == "2":
                sistema.ingresar_notas_a_estudiante()
            elif opcion == "3":
                sistema.mostrar_estudiantes()
            elif opcion == "4":
                sistema.buscar_estudiante_por_carne()
            elif opcion == "5":
                print("¡Hasta luego!")
                break
            else:
                print("Opción inválida. Intente de nuevo.\n")
menu()



