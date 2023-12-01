from Model.Paciente import Paciente
from View.ViewPaciente import ViewPaciente
class ControllerPaciente:
    def __init__(self,view =ViewPaciente(),model =Paciente(), list =[],paciente = Paciente):

        self._view = view
        self._model = model
        self._list = list
        self._paciente = paciente
    def menu(self):
        option = self._view.menu()
        return option
    def listar_pacientes(self):
        try:
            with open("pacientes.txt","r") as file:
                for linea in file.readlines():
                    line = linea.split(";")
                    obj= self._paciente(line[0], line[1], line[2], line[3],line[4],line[5],line[6],line[7])
                    self._list.append(obj)
                return self._list
        except FileNotFoundError:
            self._view.fileNotFound()
    def mostrar_mayores(self):
        for paciente in self._list:
            if paciente.mayor_edad() == True:
                self._view.mayores(paciente)
    def seleccionar_paciente(self): #ESTE MÉTODO SE EJECUTA SIEMPRE QUE HAY QUE TRABAJAR CON UN PACIENTE PARTICULAR
        try:
            loop = True
            while loop == True :
                paciente = self._view.input_paciente()
                if paciente <= len(self._list) -1:
                    self._model = self._list[paciente]
                    loop = False
        except ValueError:
            self._view.valueError()
    def cambiar_peso(self):

        try:
            peso_actual= self._view.input_peso()
            self._model.set_peso_pasado(self._model._peso)
            self._model.set_peso(peso_actual)
            self._view.peso_nuevo(self._model)
        except ValueError:
            self._view.valueError()
    def peso_sano(self):
        calculo = self._model.peso_sano()
        if calculo == "ideal":
            self._view.peso_ideal()
        elif calculo == "bajopeso":
            self._view.bajopeso()
        elif calculo =="sobrepeso":
            self._view.sobrepeso()
    def diferencia_peso(self):
        if int(self._model._peso_pasado) == 0:
            self._view.actualizar()
        elif int(self._model._peso_pasado) > 0:
            diferencia = int(self._model._peso) - int(self._model._peso_pasado)
            self._view.diferencia(diferencia)
        estado = self._model.diferencia()
        if estado == "menor":
            self._view.disminuyo()
        elif estado == "mayor":
            self._view.subio()
        elif estado == "igual":
            self._view.igual()

