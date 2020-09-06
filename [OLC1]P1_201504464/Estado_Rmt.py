from enum import Enum

class Estado(Enum):
    CORRECTO = 1
    INCORRECTO = 2


class Estado_Rmt:
    __estadoOperacion = Estado
    __operacion = str

    def __init__(self, estado, operar):
        self.__estadoOperacion = estado
        self.__operacion = operar
    
    def getEstado(self):
        return self.__estadoOperacion

    def getOperacion(self):
        return self.__operacion

    def getEstadoEnString(self):
        self.nombreEstado = ""

        if self.__estadoOperacion == Estado.CORRECTO:
            self.nombreEstado = "CORRECTO"
        elif self.__estadoOperacion == Estado.INCORRECTO:
            self.nombreEstado = "INCORRECTO"
        else:
            self.nombreEstado = "Desconocido"

        return self.nombreEstado
