class ViewPaciente:
    def menu(self):
        print("Menu")
        print("Ingrese 1 para consultar los pacientes que son mayores de edad")
        print("Ingrese  2 para seleccionar una paciente y registrar el peso actual")
        print("Ingrese  3 para calcular si la persona está en su peso ideal ")
        print("Ingrese 4 para conocer la diferencia del peso actual respecto al año pasado")
        return input()
    def fileNotFound(self):
        print("Error,no se pudo leer el archivo")
    def input_peso(self):
        return int(input("Ingrese el peso actual del paciente"))
    def input_paciente(self):
        return int(input("Seleccione un paciente según su ID"))
    def peso_nuevo(self,modelo):
        print("El nuevo peso del paciente es: ", modelo._peso)
    def mayores(self,paciente):
        print("Pacientes mayores de edad")
        print("ID ", paciente._id, " Nombre ",paciente._nombre," Edad",paciente._edad, " Peso ", paciente._peso)
    def peso_ideal(self):
        print("El paciente se encuentra en su peso ideal")
    def bajopeso(self):
        print("El paciente se encuentra debajo del peso ideal")
    def sobrepeso(self):
        print("El paciente se encuentra con sobrepeso")
    def actualizar(self):
        print("Primero debe actualizar el peso del paciente")
    def diferencia(self,diferencia):
        print( "La diferencia de peso respecto al año pasado es de : ",diferencia," kilogramos")
    def valueError(self):
        print("Debe ingresar carácteres numéricos")
    def disminuyo(self):
        print("El paciente disminuyó su peso")
    def subio(self):
        print("El paciente subio de peso")
    def igual(self):
        print("El paciente registra el mismo  peso respecto al año pasado")