from Token_Color import Token_Color
from Token_Color import Tipo

class Analizador_Color_Html:
    estado = int
    auxLexema = str
    textoDocumento = str
    lista_T = list

    def analizador_H(self, textoDocumento):
        self.estado = 0
        self.auxLexema = ""
        self.textoDocumento = textoDocumento + "#"
        self.lista_T = list()
        self.c = ''
        #---Validaciones para COMENTARIO_BLOQUE-----
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
                elif (self.c == '>' or self.c == '/' or self.c == '='
                    or self.c == '.' or self.c == '(' or self.c == ')'):
                    self.auxLexema += self.c
                    if self.c == '.':
                        self.addToken(Tipo.DESCONOCIDO)
                    else:
                        self.addToken(Tipo.OPERADOR)
                elif self.c == "\"":
                    self.estado = 3
                    self.auxLexema += self.c
                elif self.c == "\'":
                    self.estado = 4
                    self.auxLexema += self.c
                elif self.c == "<":
                    self.estado = 6
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
                if self.c.isalpha() or self.c.isdigit() or self.c == "-":
                    self.estado = 1
                    self.auxLexema += self.c
                else:
                    if (self.auxLexema == "html" or self.auxLexema == "head" or self.auxLexema == "title" or self.auxLexema == "body"
                        or self.auxLexema == "h1" or self.auxLexema == "h2" or self.auxLexema == "h3" or self.auxLexema == "h4"
                        or self.auxLexema == "h5" or self.auxLexema == "h6" or self.auxLexema == "p" or self.auxLexema == "br"
                        or self.auxLexema == "img" or self.auxLexema == "src" or self.auxLexema == "alt" or self.auxLexema == "a"
                        or self.auxLexema == "href" or self.auxLexema == "ol" or self.auxLexema == "ul" or self.auxLexema == "li" or self.auxLexema == "style"
                        or self.auxLexema == "table" or self.auxLexema == "th" or self.auxLexema == "tr" or self.auxLexema == "td"
                        or self.auxLexema == "caption" or self.auxLexema == "colgroup" or self.auxLexema == "col" or self.auxLexema == "thead"
                        or self.auxLexema == "tbody" or self.auxLexema == "tfoot"):
                        self.addToken(Tipo.RESERVADA)
                    else:
                        self.addToken(Tipo.DESCONOCIDO)
                    i -= 1
            #ESTADO S2
            elif self.estado == 2:
                if self.c.isdigit():
                    self.estado = 2
                    self.auxLexema += self.c
                else:
                    self.addToken(Tipo.DESCONOCIDO)
                    i -= 1
            #ESTADO S3
            elif self.estado == 3:
                if self.c == "\"":
                    self.estado = 5
                    self.auxLexema += self.c
                else:
                    self.estado = 3
                    self.auxLexema += self.c
            #ESTADO S4
            elif self.estado == 4:
                if self.c == "\'":
                    self.estado = 5
                    self.auxLexema += self.c
                else:
                    self.estado = 4
                    self.auxLexema += self.c
            #ESTADO S5
            elif self.estado == 5:
                self.addToken(Tipo.CADENA)
                i -= 1
            #ESTADO S6
            elif self.estado == 6:
                if self.c == "!":
                    self.estado = 7
                    self.auxLexema += self.c
                else:
                    self.addToken(Tipo.OPERADOR)
                    i -= 1
            #ESTADO S7
            elif self.estado == 7:
                if self.c == "-":
                    self.estado = 8
                    self.auxLexema += self.c
                else:
                    self.addToken(Tipo.DESCONOCIDO)
                    i -= 1
            #ESTADO S8
            elif self.estado == 8:
                if self.c == "-":
                    self.estado = 9
                    self.auxLexema += self.c
                else:
                    self.addToken(Tipo.DESCONOCIDO)
                    i -= 1
            #ESTADO S9
            elif self.estado == 9:
                if self.c == "-":
                    self.estado = 10
                    self.auxLexema += self.c
                else:
                    #---Validaciones para COMENTARIO_BLOQUE-----
                    if self.c == "#" and i == len(self.textoDocumento) - 1:   #validacion si el COMENTARIO_BLOQUE esta en la ultima linea
                        if self.inicioComentarioBloque:
                            self.addToken(Tipo.DESCONOCIDO)
                        continue
                    elif self.c == "\n":          #Comienza un comentario bloque
                        if self.inicioComentarioBloque == False:        #Indica cuando comienza el comentario bloque
                            self.inicioComentarioBloque = True
                    #---Validaciones para COMENTARIO_BLOQUE-----
                    self.estado = 9
                    self.auxLexema += self.c
            #ESTADO S10
            elif self.estado == 10:
                if self.c == "-" and self.textoDocumento[i + 1] == "#":
                    self.estado = 9
                    self.auxLexema += self.c
                elif self.c == "-" and self.textoDocumento[i + 1] == ">":
                    self.estado = 11
                    self.auxLexema += self.c
                elif self.c == "-":
                    self.estado = 10
                    self.auxLexema += self.c
                else:
                    if self.c == "\n":          #Comienza un comentario bloque
                        if self.inicioComentarioBloque == False:        #Indica cuando comienza el comentario bloque
                            self.inicioComentarioBloque = True
                    #---Validaciones para COMENTARIO_BLOQUE-----
                    self.estado = 9
                    self.auxLexema += self.c
            #ESTADO S11
            elif self.estado == 11:
                if self.c == ">":
                    self.estado = 12
                    self.auxLexema += self.c
            #ESTADO S12
            elif self.estado == 12:
                if self.inicioComentarioBloque:
                    self.addToken(Tipo.COMENTARIO)
                    #---Validaciones para COMENTARIO_BLOQUE-----
                    self.inicioComentarioBloque = False
                    #---Validaciones para COMENTARIO_BLOQUE-----
                else:
                    self.addToken(Tipo.COMENTARIO)
                i -= 1

            i += 1
    
        return self.lista_T
    
    def addToken(self, tipo):
        nuevoToken = Token_Color(tipo, self.auxLexema)
        self.lista_T.append(nuevoToken)
        self.auxLexema = ""
        self.estado = 0