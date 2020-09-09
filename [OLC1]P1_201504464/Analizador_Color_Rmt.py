from Token_Color import Token_Color
from Token_Color import Tipo

class Analizador_Color_Rmt:
    estado = int
    auxLexema = str
    textoDocumento = str
    lista_Tokens = list

    def analizador_R(self, textoDocumento):
        self.estado = 0
        self.auxLexema = ""
        self.textoDocumento = textoDocumento + "$"
        self.lista_Tokens = list()
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
                    self.addToken(Tipo.OPERADOR)
                elif self.c == "-":
                    self.auxLexema += self.c
                    self.addToken(Tipo.OPERADOR)
                elif self.c == "*":
                    self.auxLexema += self.c
                    self.addToken(Tipo.OPERADOR)
                elif self.c == '/':
                    self.auxLexema += self.c
                    self.addToken(Tipo.OPERADOR)
                elif self.c == "(":
                    self.auxLexema += self.c
                    self.addToken(Tipo.OPERADOR)
                elif self.c == ")":
                    self.auxLexema += self.c
                    self.addToken(Tipo.OPERADOR)
                elif self.c == ".":
                    self.auxLexema += self.c
                    self.addToken(Tipo.OPERADOR)
                elif self.c == " " or self.c == "\t" or self.c == "\r" or self.c == "\n":
                    self.auxLexema += self.c
                    self.addToken(Tipo.DESCONOCIDO)
                else:
                    if self.c == "$" and i == len(self.textoDocumento) - 1:
                        print("Termino analisis de tokens para colorear")
                    else:
                        self.auxLexema += self.c
                        self.addToken(Tipo.DESCONOCIDO)
            #ESTADO S1
            elif self.estado == 1:
                if self.c.isalpha() or self.c.isdigit() or self.c == "_":
                    self.estado = 1
                    self.auxLexema += self.c
                else:
                    self.addToken(Tipo.VARIABLE)
                    i -= 1
            #ESTADO S2
            elif self.estado == 2:
                if self.c.isdigit():
                    self.estado = 2
                    self.auxLexema += self.c
                else:
                    self.addToken(Tipo.NUMERO)
                    i -= 1
            i += 1
        
        return self.lista_Tokens

    def addToken(self, tipo):
        nuevoToken = Token_Color(tipo, self.auxLexema)
        self.lista_Tokens.append(nuevoToken)
        self.auxLexema = ""
        self.estado = 0