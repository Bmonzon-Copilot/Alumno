class Estudiante:  #Clase Cliente
    def __init__(self, nombre, carnet, carrera, notafinal): #Costructor
        self.__nombre = nombre
        self.__carnet = carnet
        self.__carrera = carrera
        self.__notaFinal = notafinal

class notas:
    def __init__(self, nota1, nota2, nota3):
        self.__nota1 = nota1
        self.__nota2 = nota2
        self.__nota3 = nota3


 def registrar_estudiante(self):
        nombre = input("Ingrese Nombre: ")
        carnet = input("Ingrese carnet: ")
        carrera = input("Ingrese carrera: ")
        nota_ = input("Correo: ")

 def menu(self):
            while True:
                print("\n--- estudiante ---")
                print("1. Ingrese nombre")
                print("2. Ingrese de notas")
                print("3. Ver Notas")


















        for propietario in self.propietarios:
            if propietario.get_dpi() == dpi:
                print("El cliente ya se encuentra ingresado.")
                return

        propietario = Cliente(dpi, nombre, telefono, correo)
        self.propietarios.append(propietario)
        print("Cliente Ingresado")
