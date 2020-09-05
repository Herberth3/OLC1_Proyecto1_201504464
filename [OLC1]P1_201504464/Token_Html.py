from enum import Enum

class Tipo(Enum):
    RESERVADA_HTML = 1
    RESERVADA_HEAD = 2
    RESERVADA_TITLE = 3
    RESERVADA_BODY = 4
    RESERVADA_H1 = 5
    RESERVADA_H2 = 6
    RESERVADA_H3 = 7
    RESERVADA_H4 = 8
    RESERVADA_H5 = 9
    RESERVADA_H6 = 10
    RESERVADA_P = 11
    RESERVADA_BR = 12
    RESERVADA_IMG = 13
    RESERVADA_SRC = 14
    RESERVADA_ALT = 15
    RESERVADA_A = 16
    RESERVADA_HREF = 17
    RESERVADA_OL = 18
    RESERVADA_UL = 19
    RESERVADA_LI = 20
    RESERVADA_STYLE = 21
    RESERVADA_TABLE = 22
    RESERVADA_TH = 23
    RESERVADA_TR = 24
    RESERVADA_TD = 25
    RESERVADA_CAPTION = 26
    RESERVADA_COLGROUP = 27
    RESERVADA_COL = 28
    RESERVADA_THEAD = 29
    RESERVADA_TBODY = 30
    RESERVADA_TFOOT = 31
    IDENTIFICADOR = 32
    NUMERO_ENTERO = 33
    NUMERO_DECIMAL = 34
    COMENTARIO = 35
    CADENA_STRING = 36
    SIGNO_IGUAL = 37
    SIGNO_MENOR_QUE = 38
    SIGNO_MAYOR_QUE = 39
    SIGNO_DIVISION = 40
    PARENTESIS_IZQ = 41
    PARENTESIS_DER = 42
    PUNTO = 43
    DESCONOCIDO = 44


class Token_Html:
    __tipoToken = Tipo
    __lexema = str
    __filaToken = int
    __columnaToken = int

    def __init__(self, tipo, auxlex, fila, columna):
        self.__tipoToken = tipo
        self.__lexema = auxlex
        self.__filaToken = fila
        self.__columnaToken = columna
    
    def getTipo(self):
        return self.__tipoToken

    def getLexema(self):
        return self.__lexema
    
    def getFila(self):
        return self.__filaToken

    def getColumna(self):
        return self.__columnaToken

    def getTipoEnString(self):
        self.nombreToken = ""

        if self.__tipoToken == Tipo.RESERVADA_HTML:
            self.nombreToken = "Reservada_Html"
        elif self.__tipoToken == Tipo.RESERVADA_HEAD:
            self.nombreToken = "Reservada_Head"
        elif self.__tipoToken == Tipo.RESERVADA_TITLE:
            self.nombreToken = "Reservada_Title"
        elif self.__tipoToken == Tipo.RESERVADA_BODY:
            self.nombreToken = "Reservada_Body"
        elif self.__tipoToken == Tipo.RESERVADA_H1:
            self.nombreToken = "Reservada_h1"
        elif self.__tipoToken == Tipo.RESERVADA_H2:
            self.nombreToken = "Reservada_h2"
        elif self.__tipoToken == Tipo.RESERVADA_H3:
            self.nombreToken = "Reservada_h3"
        elif self.__tipoToken == Tipo.RESERVADA_H4:
            self.nombreToken = "Reservada_h4"
        elif self.__tipoToken == Tipo.RESERVADA_H5:
            self.nombreToken = "Reservada_h5"
        elif self.__tipoToken == Tipo.RESERVADA_H6:
            self.nombreToken = "Reservada_h6"
        elif self.__tipoToken == Tipo.RESERVADA_P:
            self.nombreToken = "Reservada_p"
        elif self.__tipoToken == Tipo.RESERVADA_BR:
            self.nombreToken = "Reservada_br"
        elif self.__tipoToken == Tipo.RESERVADA_IMG:
            self.nombreToken = "Reservada_Img"
        elif self.__tipoToken == Tipo.RESERVADA_SRC:
            self.nombreToken = "Reservada_Src"
        elif self.__tipoToken == Tipo.RESERVADA_ALT:
            self.nombreToken = "Reservada_Alt"
        elif self.__tipoToken == Tipo.RESERVADA_A:
            self.nombreToken = "Reservada_a"
        elif self.__tipoToken == Tipo.RESERVADA_HREF:
            self.nombreToken = "Reservada_Href"
        elif self.__tipoToken == Tipo.RESERVADA_OL:
            self.nombreToken = "Reservada_ol"
        elif self.__tipoToken == Tipo.RESERVADA_UL:
            self.nombreToken = "Reservada_ul"
        elif self.__tipoToken == Tipo.RESERVADA_LI:
            self.nombreToken = "Reservada_li"
        elif self.__tipoToken == Tipo.RESERVADA_STYLE:
            self.nombreToken = "Reservada_Style"
        elif self.__tipoToken == Tipo.RESERVADA_TABLE:
            self.nombreToken = "Reservada_Table"
        elif self.__tipoToken == Tipo.RESERVADA_TH:
            self.nombreToken = "Reservada_th"
        elif self.__tipoToken == Tipo.RESERVADA_TR:
            self.nombreToken = "Reservada_tr"
        elif self.__tipoToken == Tipo.RESERVADA_TD:
            self.nombreToken = "Reservada_td"
        elif self.__tipoToken == Tipo.RESERVADA_CAPTION:
            self.nombreToken = "Reservada_Caption"
        elif self.__tipoToken == Tipo.RESERVADA_COLGROUP:
            self.nombreToken = "Reservada_Colgroup"
        elif self.__tipoToken == Tipo.RESERVADA_COL:
            self.nombreToken = "Reservada_Col"
        elif self.__tipoToken == Tipo.RESERVADA_THEAD:
            self.nombreToken = "Reservada_Thead"
        elif self.__tipoToken == Tipo.RESERVADA_TBODY:
            self.nombreToken = "Reservada_Tbody"
        elif self.__tipoToken == Tipo.RESERVADA_TFOOT:
            self.nombreToken = "Reservada_Tfoot"
        elif self.__tipoToken == Tipo.IDENTIFICADOR:
            self.nombreToken = "Identificador"
        elif self.__tipoToken == Tipo.NUMERO_ENTERO:
            self.nombreToken = "NumeroEntero"
        elif self.__tipoToken == Tipo.NUMERO_DECIMAL:
            self.nombreToken = "NumeroDecimal"
        elif self.__tipoToken == Tipo.COMENTARIO:
            self.nombreToken = "Comentario"
        elif self.__tipoToken == Tipo.CADENA_STRING:
            self.nombreToken = "Cadena_String"
        elif self.__tipoToken == Tipo.SIGNO_IGUAL:
            self.nombreToken = "Signo_Igual"
        elif self.__tipoToken == Tipo.SIGNO_MENOR_QUE:
            self.nombreToken = "Signo_Menor_Que"
        elif self.__tipoToken == Tipo.SIGNO_MAYOR_QUE:
            self.nombreToken = "Signo_Mayor_Que"
        elif self.__tipoToken == Tipo.SIGNO_DIVISION:
            self.nombreToken = "Signo_Division"
        elif self.__tipoToken == Tipo.PARENTESIS_IZQ:
            self.nombreToken = "Parentesis_Izq"
        elif self.__tipoToken == Tipo.PARENTESIS_DER:
            self.nombreToken = "Parentesis_Der"
        elif self.__tipoToken == Tipo.PUNTO:
            self.nombreToken = "Punto"
        else:
            self.nombreToken = "Desconocido"

        return self.nombreToken