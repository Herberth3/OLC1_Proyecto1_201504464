from Token_Color import Token_Color
from Token_Color import Tipo

class Analizador_Color_Css:
    estado = int
    auxLexema = str
    textoDocumento = str
    lista_T = list

    def analizador_C(self, textoDocumento):
        self.estado = 0
        self.auxLexema = ""
        self.textoDocumento = textoDocumento + "$"
        self.lista_T = list()
        self.c = ''
        #---Validaciones para COMENTARIO_BLOQUE-----
        self.inicioComentarioBloque = False
        #---Validaciones para COMENTARIO_BLOQUE-----

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
                elif (self.c == '{' or self.c == '}' or self.c == '(' or self.c == ')' or self.c == ';' or self.c == ':'
                    or self.c == '.' or self.c == ',' or self.c == '-' or self.c == '*' or self.c == '%' or self.c == '#'):
                    self.auxLexema += self.c
                    self.addToken(Tipo.OPERADOR)
                elif self.c == "\"":
                    self.estado = 3
                    self.auxLexema += self.c
                elif self.c == "/":
                    self.estado = 4
                    self.auxLexema += self.c
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
                if self.c.isalpha() or self.c.isdigit() or self.c == "-":
                    self.estado = 1
                    self.auxLexema += self.c
                else:
                    if (self.auxLexema == "color" or self.auxLexema == "background-color" or self.auxLexema == "background-image" or self.auxLexema == "border"
                        or self.auxLexema == "opacity" or self.auxLexema == "background" or self.auxLexema == "text-align" or self.auxLexema == "font-family"
                        or self.auxLexema == "font-style" or self.auxLexema == "font-weight" or self.auxLexema == "font-size" or self.auxLexema == "font"
                        or self.auxLexema == "padding-left" or self.auxLexema == "padding-right" or self.auxLexema == "padding-bottom" or self.auxLexema == "padding-top"
                        or self.auxLexema == "padding" or self.auxLexema == "display" or self.auxLexema == "line-height" or self.auxLexema == "width" or self.auxLexema == "height"
                        or self.auxLexema == "margin-top" or self.auxLexema == "margin-right" or self.auxLexema == "margin-bottom" or self.auxLexema == "margin-left"
                        or self.auxLexema == "margin" or self.auxLexema == "border-style" or self.auxLexema == "position" or self.auxLexema == "bottom"
                        or self.auxLexema == "top" or self.auxLexema == "right" or self.auxLexema == "left" or self.auxLexema == "float"
                        or self.auxLexema == "clear" or self.auxLexema == "max-width" or self.auxLexema == "min-width" or self.auxLexema == "max-height" or self.auxLexema == "min-height"
                        or self.auxLexema == "content" or self.auxLexema == "border-top" or self.auxLexema == "px" or self.auxLexema == "em"
                        or self.auxLexema == "rem" or self.auxLexema == "vh" or self.auxLexema == "vw" or self.auxLexema == "in"
                        or self.auxLexema == "cm" or self.auxLexema == "mm" or self.auxLexema == "pt" or self.auxLexema == "pc"
                        or self.auxLexema == "relative" or self.auxLexema == "inline-block" or self.auxLexema == "red" or self.auxLexema == "rgba" or self.auxLexema == "url"
                        or self.auxLexema == "content" or self.auxLexema == "inherit" or self.auxLexema == "solid" or self.auxLexema == "absolute"
                        or self.auxLexema == "arial" or self.auxLexema == "sans-serif" or self.auxLexema == "block"):
                        self.addToken(Tipo.RESERVADA)
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
                    self.estado = 5
                    self.auxLexema += self.c
                else:
                    self.estado = 3
                    self.auxLexema += self.c
            #ESTADO S4
            elif self.estado ==4:
                if self.c == "*":
                    self.estado = 6
                    self.auxLexema += self.c
                else:
                    self.addToken(Tipo.DESCONOCIDO)
                    i -= 1
            #ESTADO S5
            elif self.estado == 5:
                self.addToken(Tipo.CADENA)
                i -= 1
            #ESTADO S6
            elif self.estado == 6:
                if self.c == "*":
                    self.estado = 7
                    self.auxLexema += self.c
                else:
                    #---Validaciones para COMENTARIO_BLOQUE-----
                    if self.c == "$" and i == len(self.textoDocumento) - 1:   #validacion si el COMENTARIO_BLOQUE esta en la ultima linea
                        if self.inicioComentarioBloque:
                            self.addToken(Tipo.DESCONOCIDO)
                        continue
                    elif self.c == "\n":          #Comienza un comentario bloque
                        if self.inicioComentarioBloque == False:        #Indica cuando comienza el comentario bloque
                            self.inicioComentarioBloque = True
                    #---Validaciones para COMENTARIO_BLOQUE-----
                    self.estado = 6
                    self.auxLexema += self.c
            #ESTADO S7
            elif self.estado == 7:
                if self.c == "/":
                    self.estado = 8
                    self.auxLexema += self.c
                elif self.c == "*":
                    self.estado = 6
                    i -= 1
                else:
                    #---Validaciones para COMENTARIO_BLOQUE-----
                    if self.c == "$" and i == len(self.textoDocumento) - 1:   #validacion si el COMENTARIO_BLOQUE esta en la ultima linea
                        if self.inicioComentarioBloque:
                            self.addToken(Tipo.DESCONOCIDO)
                        continue
                    elif self.c == "\n":          #Comienza un comentario bloque
                        if self.inicioComentarioBloque == False:
                            self.inicioComentarioBloque = True
                    #---Validaciones para COMENTARIO_BLOQUE-----
                    self.estado = 6
                    self.auxLexema += self.c
            #ESTADO S8
            elif self.estado == 8:
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