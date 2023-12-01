class Paciente:
    def __init__(self,id=int(0),nombre="",edad=int(0),dni =int(0),genero="",peso =int(0),altura=int(0),peso_pasado=int(0)):
        self._id = id
        self._nombre= nombre
        self._edad = edad
        self._dni = dni
        self._genero = genero
        self._peso = peso
        self._altura = altura
        self._peso_pasado = peso_pasado
    def get_nombre(self):
        return self._nombre
    def set_nombre(self,data):
        self._nombre = data
    def get_edad(self):
        return self._edad
    def set_edad(self,data):
        self._edad = data
    def get_dni(self):
        return self._dni
    def set_dni(self,data):
        self._edad = data
    def get_genero(self):
        return self._genero
    def set_genero(self,data):
        self._genero= data
    def get_peso(self):
        return self._peso
    def set_peso(self,data):
        self._peso= data
    def get_altura(self):
        return self._altura
    def set_altura(self,data):
        self._altura= data
    def get_peso_pasado(self):
        return self._peso_pasado
    def set_peso_pasado(self,data):
        self._peso_pasado = data

    def mayor_edad(self):
        if int(self._edad) > int(17):
            return True
        else:
            return False
    def peso_sano(self):
        if int(self._peso) / (int(self._altura)*int(self._altura)) <20:
            return "ideal"
        elif int(self._peso) / (int(self._altura)*int(self._altura)) >= 20 and int(self._peso) / (int(self._altura)*int(self._altura)) <=25:
            return "bajopeso"
        elif int(self._peso) / (int(self._altura)*int(self._altura)) > 25:
            return "sobrepeso"
    def diferencia(self):
        if int(self._peso) < int(self._peso_pasado):
            return "menor"
        elif int(self._peso) > int(self._peso_pasado):
            return "mayor"
        elif int(self._peso) == int(self._peso_pasado):
            return "igual"