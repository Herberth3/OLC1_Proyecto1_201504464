from enum import Enum

class Tipo(Enum):
    RESERVADA = 1
    VARIABLE = 2
    NUMERO = 3
    COMENTARIO = 4
    CADENA = 5
    BOOLEAN = 6
    OPERADOR = 7
    DESCONOCIDO = 57


class Token_Color:
    __tipoToken = Tipo
    __lexema = str

    def __init__(self, tipo, auxlex):
        self.__tipoToken = tipo
        self.__lexema = auxlex
    
    def getTipo(self):
        return self.__tipoToken

    def getLexema(self):
        return self.__lexema

    def getTipoEnString(self):
        self.nombreToken = ""

        if self.__tipoToken == Tipo.RESERVADA:
            self.nombreToken = "Reservada"
        elif self.__tipoToken == Tipo.VARIABLE:
            self.nombreToken = "Variable"
        elif self.__tipoToken == Tipo.NUMERO:
            self.nombreToken = "Numero"
        elif self.__tipoToken == Tipo.COMENTARIO:
            self.nombreToken = "Comentario"
        elif self.__tipoToken == Tipo.CADENA:
            self.nombreToken = "Cadena"
        elif self.__tipoToken == Tipo.BOOLEAN:
            self.nombreToken = "Boolean"
        elif self.__tipoToken == Tipo.OPERADOR:
            self.nombreToken = "Operador"
        else:
            self.nombreToken = "Desconocido"

        return self.nombreToken