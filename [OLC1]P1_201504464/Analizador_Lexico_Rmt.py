from Token_Rmt import Token_Rmt
from Token_Rmt import Tipo
from Token_Error import Token_Error
from Token_Error import TipoError
from tkinter import messagebox

class Analizador_Lexico_Rmt:
    estado = int
    auxLexema = str
    textoDocumento = str
    lista_Tokens = list
    lista_Errores = list

    def analizador_Rmt(self, textoDocumento):
        self.estado = 0
        self.auxLexema = ""
        self.textoDocumento = textoDocumento + "$"
        self.lista_Tokens = list()
        self.lista_Errores = list()
        self.c = ''

        i = 0
        while i < len(self.textoDocumento):
            self.c = self.textoDocumento[i]

            #ESTADO 0
            if self.estado == 0:
                if self.c.isalpha():
                    self.estado = 1
                    self.auxLexema += self.c
                elif self.c.isdigit():
                    self.estado = 2
                    self.auxLexema += self.c
                elif self.c == '+':
                    self.auxLexema += self.c
                    self.addToken(Tipo.SIGNO_MAS)
                elif self.c == "-":
                    self.auxLexema += self.c
                    self.addToken(Tipo.SIGNO_MENOS)
                elif self.c == "*":
                    self.auxLexema += self.c
                    self.addToken(Tipo.SIGNO_POR)
                elif self.c == '/':
                    self.auxLexema += self.c
                    self.addToken(Tipo.SIGNO_DIVISION)
                elif self.c == "(":
                    self.auxLexema += self.c
                    self.addToken(Tipo.PARENTESIS_IZQ)
                elif self.c == ")":
                    self.auxLexema += self.c
                    self.addToken(Tipo.PARENTESIS_DER)
                elif self.c == " " or self.c == "\t" or self.c == "\r" or self.c == "\n":
                    i += 1
                    self.estado = 0
                    continue
                else:
                    if self.c == "$" and i == len(self.textoDocumento) - 1:
                        if len(self.lista_Errores) > 0:
                            messagebox.showerror("Alerta", "Se han encontrado errores léxicos")
                            #self.imprimirListaErrores()
                        #messagebox.showinfo("Aviso", "Análisis léxico satisfactorio")
                    else:
                        self.addTokenError(self.c)
            #ESTADO S1
            elif self.estado == 1:
                if self.c.isalpha() or self.c.isdigit() or self.c == "_":
                    self.estado = 1
                    self.auxLexema += self.c
                else:
                    self.addToken(Tipo.IDENTIFICADOR)
                    i -= 1
            #ESTADO S2
            elif self.estado == 2:
                if self.c.isdigit():
                    self.estado = 2
                    self.auxLexema += self.c
                elif self.c == ".":
                    self.estado = 3
                    self.auxLexema += self.c
                else:
                    self.addToken(Tipo.NUMERO)
                    i -= 1
            #ESTADO S3
            elif self.estado == 3:
                if self.c.isdigit():
                    self.estado = 4
                    self.auxLexema += self.c
                else:
                    self.addTokenError(self.auxLexema)
                    i -= 1
            #ESTADO S4
            elif self.estado == 4:
                if self.c.isdigit():
                    self.estado = 4
                    self.auxLexema += self.c
                else:
                    self.addToken(Tipo.NUMERO)
                    i -= 1
            i += 1
        
        return self.lista_Tokens

    def analizador_Error(self):
        return self.lista_Errores
    
    def addToken(self, tipo):
        nuevoToken = Token_Rmt(tipo, self.auxLexema)
        self.lista_Tokens.append(nuevoToken)
        self.auxLexema = ""
        self.estado = 0

    def addTokenError(self, caracter):
        if self.auxLexema == "":
            nuevoError = Token_Error(caracter, TipoError.LEXICO, "El simbolo no pertenece al lenguaje", 1, 1)
        else:
            nuevoError = Token_Error(caracter, TipoError.LEXICO, "Lexema no definido en el lenguaje", 1, 1)
        
        self.lista_Errores.append(nuevoError)
        self.auxLexema = ""
        self.estado = 0
    
    def imprimirListaErrores(self):
        self.tokenError = Token_Error
        impresion = ""
        for self.tokenError in self.lista_Errores:
            #print(self.tokenError.getCaracterError() + " Tipo Error: " + self.tokenError.getTipoErrorEnString() + " " + self.tokenError.getDescripcionError() + " Fila: " + str(self.tokenError.getFilaError()) + " Columna: " + str(self.tokenError.getColumnaError()))
            impresion += "Caracter: " + self.tokenError.getCaracterError() + " <--------> Tipo Error: " + self.tokenError.getTipoErrorEnString() + " <--------> " + self.tokenError.getDescripcionError() + " <-----> Fila: " + str(self.tokenError.getFilaError()) + " <-----> Columna: " + str(self.tokenError.getColumnaError()) + "\n"

        return impresion