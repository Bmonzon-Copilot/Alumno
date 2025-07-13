class Estudiante:  #Clase Estudiante
    def __init__(self, nombre, carnet, carrera, nota_final): #Costructor
        self.__nombre = nombre
        self.__carnet = carnet
        self.__carrera = carrera
        self.__nota_final = nota_final

    def __str__(self):
        return f"Nombre: {self.nombre}, Carné: {self.carnet}, Carrera: {self.carrera}, Nota Final: {self.nota_final}"


class Sistema:
    def __init__(self):
        self.estudiantes=[]

    def registrar_estudiante(self):
        nombre = input("Ingrese Nombre: ")
        carnet = input("Ingrese carnet: ")
        carrera = input("Ingrese carrera: ")

        try:
            nota_final = float(input("Ingrese la nota final: "))
            return
        except ValueError:
            print("Nota no valida ingrese un nota en numeros")

        estudiante = Estudiante(nombre, carnet,carrera, nota_final)
        self.estudiantes.append(estudiante)
        print("Estudiante Ingresado")

    def mostrar_estudiante(self):
        if not self.estudiantes:
            print("No hay estudiantes ingresados...")
            return
        print("LISTADO: ")
        for estudiante in self.estudiantes:
            print(estudiante)
        print()


 def registrar_estudiante(self):
        nombre = input("Ingrese Nombre: ")
        carnet = input("Ingrese carnet: ")
        carrera = input("Ingrese carrera: ")
        notafinal = input("Correo: ")

















        for propietario in self.propietarios:
            if propietario.get_dpi() == dpi:
                print("El cliente ya se encuentra ingresado.")
                return

        propietario = Cliente(dpi, nombre, telefono, correo)
        self.propietarios.append(propietario)
        print("Cliente Ingresado")
