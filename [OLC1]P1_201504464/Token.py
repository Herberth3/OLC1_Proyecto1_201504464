from enum import Enum

class Tipo(Enum):
    RESERVADA_VAR = 1
    RESERVADA_INT = 2
    RESERVADA_STRING = 3
    RESERVADA_CHAR = 4
    RESERVADA_BOOLEAN = 5
    RESERVADA_IF = 6
    RESERVADA_ELSE = 7
    RESERVADA_FOR = 8
    RESERVADA_WHILE = 9
    RESERVADA_DO = 10
    RESERVADA_CONTINUE = 11
    RESERVADA_BREAK = 12
    RESERVADA_RETURN = 13
    RESERVADA_CONTRUCTOR = 14
    RESERVADA_FUNCTION = 15
    RESERVADA_CLASS = 16
    RESERVADA_MATH = 17
    RESERVADA_POW = 18
    RESERVADA_TRUE = 19
    RESERVADA_FALSE = 20
    VARIABLE = 21
    NUMERO_ENTERO = 22
    NUMERO_DECIMAL = 23
    COMENTARIO_LINEA = 24
    COMENTARIO_BLOQUE = 25
    CADENA_STRING = 26
    SIGNO_AND = 27
    SIGNO_OR = 28
    SIGNO_POS_INCREMENTO = 29
    SIGNO_POS_DECREMENTO = 30
    SIGNO_SUMA_CONCATENADA = 31
    SIGNO_RESTA_CONCATENADA = 32
    SIGNO_LAMBDA = 33
    SIGNO_IGUAL = 34
    SIGNO_DOBLE_IGUAL = 35
    SIGNO_MENOR_QUE = 36
    SIGNO_MAYOR_QUE = 37
    SIGNO_MENOR_IGUAL_QUE = 38
    SIGNO_MAYOR_IGUAL_QUE = 39
    SIGNO_DIFERENTE_DE = 40
    SIGNO_NEGACION = 41
    SIGNO_ASIGNACION = 42
    SIGNO_MAS = 43
    SIGNO_MENOS = 44
    SIGNO_POR = 45
    SIGNO_DIVISION = 46
    LLAVE_IZQ = 47
    LLAVE_DER = 48
    PARENTESIS_IZQ = 49
    PARENTESIS_DER = 50
    COMA = 51
    PUNTO_Y_COMA = 52
    DOS_PUNTOS = 53
    PUNTO = 54
    DESCONOCIDO = 55


class Token:
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

        if self.__tipoToken == Tipo.RESERVADA_VAR:
            self.nombreToken = "Reservada_Var"
        elif self.__tipoToken == Tipo.RESERVADA_INT:
            self.nombreToken = "Reservada_Int"
        elif self.__tipoToken == Tipo.RESERVADA_STRING:
            self.nombreToken = "Reservada_String"
        elif self.__tipoToken == Tipo.RESERVADA_CHAR:
            self.nombreToken = "Reservada_Char"
        elif self.__tipoToken == Tipo.RESERVADA_BOOLEAN:
            self.nombreToken = "Reservada_Boolean"
        elif self.__tipoToken == Tipo.RESERVADA_IF:
            self.nombreToken = "Reservada_If"
        elif self.__tipoToken == Tipo.RESERVADA_ELSE:
            self.nombreToken = "Reservada_Else"
        elif self.__tipoToken == Tipo.RESERVADA_FOR:
            self.nombreToken = "Reservada_For"
        elif self.__tipoToken == Tipo.RESERVADA_WHILE:
            self.nombreToken = "Reservada_While"
        elif self.__tipoToken == Tipo.RESERVADA_DO:
            self.nombreToken = "Reservada_Do"
        elif self.__tipoToken == Tipo.RESERVADA_CONTINUE:
            self.nombreToken = "Reservada_Continue"
        elif self.__tipoToken == Tipo.RESERVADA_BREAK:
            self.nombreToken = "Reservada_Break"
        elif self.__tipoToken == Tipo.RESERVADA_RETURN:
            self.nombreToken = "Reservada_Return"
        elif self.__tipoToken == Tipo.RESERVADA_CONTRUCTOR:
            self.nombreToken = "Reservada_Constructor"
        elif self.__tipoToken == Tipo.RESERVADA_FUNCTION:
            self.nombreToken = "Reservada_Function"
        elif self.__tipoToken == Tipo.RESERVADA_CLASS:
            self.nombreToken = "Reservada_Class"
        elif self.__tipoToken == Tipo.RESERVADA_MATH:
            self.nombreToken = "Reservada_Math"
        elif self.__tipoToken == Tipo.RESERVADA_POW:
            self.nombreToken = "Reservada_Pow"
        elif self.__tipoToken == Tipo.RESERVADA_TRUE:
            self.nombreToken = "Reservada_True"
        elif self.__tipoToken == Tipo.RESERVADA_FALSE:
            self.nombreToken = "Reservada_False"
        elif self.__tipoToken == Tipo.VARIABLE:
            self.nombreToken = "Variable"
        elif self.__tipoToken == Tipo.NUMERO_ENTERO:
            self.nombreToken = "NumeroEntero"
        elif self.__tipoToken == Tipo.NUMERO_DECIMAL:
            self.nombreToken = "NumeroDecimal"
        elif self.__tipoToken == Tipo.COMENTARIO_LINEA:
            self.nombreToken = "Comentario_Linea"
        elif self.__tipoToken == Tipo.COMENTARIO_BLOQUE:
            self.nombreToken = "Comentario_Bloque"
        elif self.__tipoToken == Tipo.CADENA_STRING:
            self.nombreToken = "Cadena_String"
        elif self.__tipoToken == Tipo.SIGNO_AND:
            self.nombreToken = "Signo_AND"
        elif self.__tipoToken == Tipo.SIGNO_OR:
            self.nombreToken = "Signo_OR"
        elif self.__tipoToken == Tipo.SIGNO_POS_INCREMENTO:
            self.nombreToken = "Signo_Pos_Incremento"
        elif self.__tipoToken == Tipo.SIGNO_POS_DECREMENTO:
            self.nombreToken = "Signo_Pos_Decremento"
        elif self.__tipoToken == Tipo.SIGNO_SUMA_CONCATENADA:
            self.nombreToken = "Signo_Suma_Concatenada"
        elif self.__tipoToken == Tipo.SIGNO_RESTA_CONCATENADA:
            self.nombreToken = "Signo_Resta_Concatenada"
        elif self.__tipoToken == Tipo.SIGNO_LAMBDA:
            self.nombreToken = "Signo_Lambda"
        elif self.__tipoToken == Tipo.SIGNO_IGUAL:
            self.nombreToken = "Signo_Igual"
        elif self.__tipoToken == Tipo.SIGNO_DOBLE_IGUAL:
            self.nombreToken = "Signo_Doble_Igual"
        elif self.__tipoToken == Tipo.SIGNO_MENOR_QUE:
            self.nombreToken = "Signo_Menor_Que"
        elif self.__tipoToken == Tipo.SIGNO_MAYOR_QUE:
            self.nombreToken = "Signo_Mayor_Que"
        elif self.__tipoToken == Tipo.SIGNO_MENOR_IGUAL_QUE:
            self.nombreToken = "Signo_Menor_Igual_Que"
        elif self.__tipoToken == Tipo.SIGNO_MAYOR_IGUAL_QUE:
            self.nombreToken = "Signo_Mayor_Igual_Que"
        elif self.__tipoToken == Tipo.SIGNO_DIFERENTE_DE:
            self.nombreToken = "Signo_Diferente_De"
        elif self.__tipoToken == Tipo.SIGNO_NEGACION:
            self.nombreToken = "Signo_Negacion"
        elif self.__tipoToken == Tipo.SIGNO_ASIGNACION:
            self.nombreToken = "Signo_Asignacion"
        elif self.__tipoToken == Tipo.SIGNO_MAS:
            self.nombreToken = "Signo_Mas"
        elif self.__tipoToken == Tipo.SIGNO_MENOS:
            self.nombreToken = "Signo_Menos"
        elif self.__tipoToken == Tipo.SIGNO_POR:
            self.nombreToken = "Signo_Por"
        elif self.__tipoToken == Tipo.SIGNO_DIVISION:
            self.nombreToken = "Signo_Division"
        elif self.__tipoToken == Tipo.LLAVE_IZQ:
            self.nombreToken = "Llave_Izq"
        elif self.__tipoToken == Tipo.LLAVE_DER:
            self.nombreToken = "Llave_Der"
        elif self.__tipoToken == Tipo.PARENTESIS_IZQ:
            self.nombreToken = "Parentesis_Izq"
        elif self.__tipoToken == Tipo.PARENTESIS_DER:
            self.nombreToken = "Parentesis_Der"
        elif self.__tipoToken == Tipo.COMA:
            self.nombreToken = "Coma"
        elif self.__tipoToken == Tipo.PUNTO_Y_COMA:
            self.nombreToken = "Punto_Y_Coma"
        elif self.__tipoToken == Tipo.DOS_PUNTOS:
            self.nombreToken = "Dos_Puntos"
        elif self.__tipoToken == Tipo.PUNTO:
            self.nombreToken = "Punto"
        else:
            self.nombreToken = "Desconocido"

        return self.nombreToken