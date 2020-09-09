from Token_Color import Token_Color
from Token_Color import Tipo

class Analizador_Color_Javascript:
    estado = int
    auxLexema = str
    textoDocumento = str
    lista_T = list

    def analizador_J(self, textoDocumento):
        self.estado = 0
        self.auxLexema = ""
        self.textoDocumento = textoDocumento + "#"
        self.lista_T = list()
        self.c = ''
        #---Validaciones para COMENTARIO_BLOQUE-----
        self.estadoComentario = 0  #Guarda el estado anterior del comentario para saber si es de linea o bloque
        self.inicioComentarioBloque = False
        #---Validaciones para COMENTARIO_BLOQUE-----

        i = 0
        while i < len(self.textoDocumento):
            self.c = self.textoDocumento[i]

            #ESTADO S0
            if self.estado == 0:
                if self.c.isalpha():
                    self.estado = 1
                    self.auxLexema += self.c
                elif self.c.isdigit():
                    self.estado = 2
                    self.auxLexema += self.c
                elif (self.c == '{' or self.c == '}' or self.c == '(' or self.c == ')' or self.c == ';' or self.c == ':' 
                    or self.c == '.' or self.c == ',' or self.c == '&' or self.c == '|' or self.c == '+' or self.c == '='
                    or self.c == '-' or self.c == '>' or self.c == '<' or self.c == '!' or self.c == '*'):
                    self.auxLexema += self.c
                    self.addToken(Tipo.OPERADOR)
                elif self.c == "\"":
                    self.estado = 3
                    self.auxLexema += self.c
                elif self.c == "\'":
                    self.estado = 4
                    self.auxLexema += self.c
                elif self.c == "/":
                    self.estado = 5
                    self.auxLexema += self.c
                elif self.c == " " or self.c == "\t" or self.c == "\r" or self.c == "\n":
                    self.auxLexema += self.c
                    self.addToken(Tipo.DESCONOCIDO)
                else:
                    if self.c == "#" and i == len(self.textoDocumento) - 1:
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
                    if (self.auxLexema == "var" or self.auxLexema == "int" or self.auxLexema == "string" or self.auxLexema == "char"
                        or self.auxLexema == "boolean" or self.auxLexema == "if" or self.auxLexema == "else" or self.auxLexema == "for"
                        or self.auxLexema == "while" or self.auxLexema == "do" or self.auxLexema == "continue" or self.auxLexema == "break"
                        or self.auxLexema == "return" or self.auxLexema == "constructor" or self.auxLexema == "function" or self.auxLexema == "class"
                        or self.auxLexema == "Math" or self.auxLexema == "pow" or self.auxLexema == "this" or self.auxLexema == "console"):
                        self.addToken(Tipo.RESERVADA)
                    elif self.auxLexema == "true":
                        self.addToken(Tipo.BOOLEAN)
                    elif self.auxLexema == "false":
                        self.addToken(Tipo.BOOLEAN)
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
            #ESTADO S3
            elif self.estado == 3:
                if self.c == "\"":
                    self.estado = 6
                    self.auxLexema += self.c
                else:
                    self.estado = 3
                    self.auxLexema += self.c
            #ESTADO S4
            elif self.estado == 4:
                if self.c == "\'":
                    self.estado = 7
                    self.auxLexema += self.c
                else:
                    self.estado = 4
                    self.auxLexema += self.c
            #ESTADO S5
            elif self.estado == 5:
                if self.c == "*":
                    self.estado = 8
                    self.auxLexema += self.c
                elif self.c == "/":
                    self.estado = 9
                    self.auxLexema += self.c
                else:
                    self.addToken(Tipo.OPERADOR)
                    i -= 1
            #ESTADO S6
            elif self.estado == 6:
                self.addToken(Tipo.CADENA)
                i -= 1
            #ESTADO S7
            elif self.estado == 7:
                self.addToken(Tipo.CADENA)
                i -= 1
            #ESTADO S8
            elif self.estado == 8:
                if self.c == "*":
                    self.estado = 10
                    self.auxLexema += self.c
                else:
                    #---Validaciones para COMENTARIO_BLOQUE-----
                    if self.c == "#" and i == len(self.textoDocumento) - 1:   #validacion si el COMENTARIO_BLOQUE esta en la ultima linea
                        if self.inicioComentarioBloque:
                            self.addToken(Tipo.DESCONOCIDO)
                        continue
                    elif self.c == "\n":          #Comienza un comentario bloque
                        if self.inicioComentarioBloque == False:
                            self.inicioComentarioBloque = True
                    #---Validaciones para COMENTARIO_BLOQUE-----
                    self.estado = 8
                    self.auxLexema += self.c
            #ESTADO S9
            elif self.estado == 9:
                if self.c == "\n":
                    self.estado = 11
                    #---Validaciones para COMENTARIO_LINEA-----
                    self.estadoComentario = 9
                    i -= 1                      #Se reduce en 1 el iterador i para analizar el \n ya que no se adjunta a la cadena
                    #---Validaciones para COMENTARIO_LINEA-----
                elif self.c == "#" and i == len(self.textoDocumento) - 1:   #validacion si el COMENTARIO_LINEA esta en la ultima linea
                    self.estado = 11
                    #---Validaciones para COMENTARIO_LINEA-----
                    self.estadoComentario = 9
                    i -= 1
                    #---Validaciones para COMENTARIO_LINEA-----
                else:
                    self.estado = 9
                    self.auxLexema += self.c
            #ESTADO S10
            elif self.estado == 10:
                if self.c == "/":
                    self.estado = 11
                    self.auxLexema += self.c
                    #---Validaciones para COMENTARIO_BLOQUE-----
                    self.estadoComentario = 10
                    #---Validaciones para COMENTARIO_BLOQUE-----
                elif self.c == "*":
                    self.estado = 8
                    i -= 1
                else:
                    #---Validaciones para COMENTARIO_BLOQUE-----
                    if self.c == "#" and i == len(self.textoDocumento) - 1:   #validacion si el COMENTARIO_BLOQUE esta en la ultima linea
                        if self.inicioComentarioBloque:
                            self.addToken(Tipo.DESCONOCIDO)
                        continue
                    elif self.c == "\n":          #Comienza un comentario bloque
                        if self.inicioComentarioBloque == False:
                            self.inicioComentarioBloque = True
                    #---Validaciones para COMENTARIO_BLOQUE-----
                    self.estado = 8
                    self.auxLexema += self.c
            #ESTADO S11
            elif self.estado == 11:
                if self.estadoComentario == 9:
                    self.addToken(Tipo.COMENTARIO)
                else:
                    self.addToken(Tipo.COMENTARIO)
                    #---Validaciones para COMENTARIO_BLOQUE-----
                    self.inicioComentarioBloque = False
                    #---Validaciones para COMENTARIO_BLOQUE-----
                i -= 1
            i += 1
        
        return self.lista_T
    
    def addToken(self, tipo):
        nuevoToken = Token_Color(tipo, self.auxLexema)
        self.lista_T.append(nuevoToken)
        self.auxLexema = ""
        self.estado = 0

        



        