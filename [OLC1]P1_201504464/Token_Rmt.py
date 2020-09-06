from enum import Enum

class Tipo(Enum):
    NUMERO = 1
    IDENTIFICADOR = 2
    SIGNO_MAS = 3
    SIGNO_MENOS = 4
    SIGNO_POR = 5
    SIGNO_DIVISION = 6
    PARENTESIS_IZQ = 7
    PARENTESIS_DER = 8
    DESCONOCIDO = 9


class Token_Rmt:
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

        if self.__tipoToken == Tipo.NUMERO:
            self.nombreToken = "Numero"
        elif self.__tipoToken == Tipo.IDENTIFICADOR:
            self.nombreToken = "Identificador"
        elif self.__tipoToken == Tipo.SIGNO_MAS:
            self.nombreToken = "Signo_Mas"
        elif self.__tipoToken == Tipo.SIGNO_MENOS:
            self.nombreToken = "Signo_Menos"
        elif self.__tipoToken == Tipo.SIGNO_POR:
            self.nombreToken = "Signo_Por"
        elif self.__tipoToken == Tipo.SIGNO_DIVISION:
            self.nombreToken = "Signo_Division"
        elif self.__tipoToken == Tipo.PARENTESIS_IZQ:
            self.nombreToken = "Parentesis_Izq"
        elif self.__tipoToken == Tipo.PARENTESIS_DER:
            self.nombreToken = "Parentesis_Der"
        else:
            self.nombreToken = "Desconocido"

        return self.nombreToken