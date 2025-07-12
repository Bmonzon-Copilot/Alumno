class Estudiante:  #Clase Cliente
    def __init__(self, nombre, carnet, carrera, nota_final): #Costructor
        self.__nombre = nombre
        self.__carnet = carnet
        self.__carrera = carrera
        self.__nota_final = nota_final

 def registrar_estudiante(self):
        nombre = input("Ingrese Nombre: ")
        carnet = input("Ingrese carnet: ")
        carrera = input("Ingrese carrera: ")
        nota_ = input("Correo: ")


















        for propietario in self.propietarios:
            if propietario.get_dpi() == dpi:
                print("El cliente ya se encuentra ingresado.")
                return

        propietario = Cliente(dpi, nombre, telefono, correo)
        self.propietarios.append(propietario)
        print("Cliente Ingresado")
