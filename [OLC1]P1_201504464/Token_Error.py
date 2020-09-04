from enum import Enum

class TipoError(Enum):
    LEXICO = 1
    SINTACTICO = 2

class Token_Error:
    __caracterError = str
    __tipoTokenError = TipoError
    __descripcionError = str
    __filaError = int
    __columnaError = int

    def __init__(self, caracter, tipoError, descripcion, fila, columna):
        self.__caracterError = caracter
        self.__tipoTokenError = tipoError
        self.__descripcionError = descripcion
        self.__filaError = fila
        self.__columnaError = columna
    
    def getCaracterError(self):
        return self.__caracterError
    
    def getTipoError(self):
        return self.__tipoTokenError
    
    def getDescripcionError(self):
        return self.__descripcionError
    
    def getFilaError(self):
        return self.__filaError
    
    def getColumnaError(self):
        return self.__columnaError

    def getTipoErrorEnString(self):
        self.nombreErrorToken = ""

        if self.__tipoTokenError == TipoError.LEXICO:
            self.nombreErrorToken = "Lexico"
        elif self.__tipoTokenError == TipoError.SINTACTICO:
            self.nombreErrorToken = "Sintactico"
        
        return self.nombreErrorToken
