from Token_Css import Token_Css
from Token_Css import Tipo
from Token_Error import Token_Error
from Token_Error import TipoError
from tkinter import messagebox

class Analizador_Lexico_Css:
    estado = int
    auxLexema = str
    textoDocumento = str
    lista_Tokens = list
    lista_Errores = list
    appendND = str

    def analizador_Css(self, textoDocumento):
        self.estado = 0
        self.auxLexema = ""
        self.textoDocumento = textoDocumento + "$"
        self.lista_Tokens = list()
        self.lista_Errores = list()
        self.c = ''
        self.columnaToken = 0
        self.filaToken = 1
        #---Validaciones para COMENTARIO_BLOQUE-----
        self.filaComentarioBloque = 0
        self.columnaComentarioBloque = 0
        self.inicioComentarioBloque = False
        #---Validaciones para COMENTARIO_BLOQUE-----
        self.appendND = ""  #Recolecta todos los caracteres omitiendo los errores

        i = 0
        while i < len(self.textoDocumento):
            self.c = self.textoDocumento[i]
            self.columnaToken += 1

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
                    self.estado = 3
                    self.auxLexema += self.c
                elif self.c == "\"":
                    self.estado = 4
                    self.auxLexema += self.c
                elif self.c == "/":
                    self.estado = 5
                    self.auxLexema += self.c
                elif self.c == " " or self.c == "\t" or self.c == "\r" or self.c == "\n":
                    i += 1
                    self.estado = 0
                    if self.c == "\n":
                        self.columnaToken = 0
                        self.filaToken += 1
                    self.appendND += self.c #Recolector de caracteres
                    continue
                else:
                    if self.c == "$" and i == len(self.textoDocumento) - 1:
                        if len(self.lista_Errores) > 0:
                            messagebox.showerror("Alerta", "Se han encontrado errores léxicos")
                            #self.imprimirListaErrores()
                        messagebox.showinfo("Aviso", "Análisis léxico satisfactorio")
                    else:
                        self.addTokenError(self.c, self.filaToken, self.columnaToken)
            #ESTADO S1
            elif self.estado == 1:
                if self.c.isalpha() or self.c.isdigit() or self.c == "-":
                    self.estado = 1
                    self.auxLexema += self.c
                else:
                    if self.auxLexema == "color":
                        self.addToken(Tipo.PROPIEDAD_COLOR, self.filaToken, self.columnaToken - len(self.auxLexema))
                    elif self.auxLexema == "background-color":
                        self.addToken(Tipo.PROPIEDAD_BACKGROUND_COLOR, self.filaToken, self.columnaToken - len(self.auxLexema))
                    elif self.auxLexema == "background-image":
                        self.addToken(Tipo.PROPIEDAD_BACKGROUND_IMAGE, self.filaToken, self.columnaToken - len(self.auxLexema))
                    elif self.auxLexema == "border":
                        self.addToken(Tipo.PROPIEDAD_BORDER, self.filaToken, self.columnaToken - len(self.auxLexema))
                    elif self.auxLexema == "opacity":
                        self.addToken(Tipo.PROPIEDAD_OPACITY, self.filaToken, self.columnaToken - len(self.auxLexema))
                    elif self.auxLexema == "background":
                        self.addToken(Tipo.PROPIEDAD_BACKGROUND, self.filaToken, self.columnaToken - len(self.auxLexema))
                    elif self.auxLexema == "text-align":
                        self.addToken(Tipo.PROPIEDAD_TEXT_ALIGN, self.filaToken, self.columnaToken - len(self.auxLexema))
                    elif self.auxLexema == "font-family":
                        self.addToken(Tipo.PROPIEDAD_FONT_FAMILY, self.filaToken, self.columnaToken - len(self.auxLexema))
                    elif self.auxLexema == "font-style":
                        self.addToken(Tipo.PROPIEDAD_FONT_STYLE, self.filaToken, self.columnaToken - len(self.auxLexema))
                    elif self.auxLexema == "font-weight":
                        self.addToken(Tipo.PROPIEDAD_FONT_WEIGHT, self.filaToken, self.columnaToken - len(self.auxLexema))
                    elif self.auxLexema == "font-size":
                        self.addToken(Tipo.PROPIEDAD_FONT_SIZE, self.filaToken, self.columnaToken - len(self.auxLexema))
                    elif self.auxLexema == "font":
                        self.addToken(Tipo.PROPIEDAD_FONT, self.filaToken, self.columnaToken - len(self.auxLexema))
                    elif self.auxLexema == "padding-left":
                        self.addToken(Tipo.PROPIEDAD_PADDING_LEFT, self.filaToken, self.columnaToken - len(self.auxLexema))
                    elif self.auxLexema == "padding-right":
                        self.addToken(Tipo.PROPIEDAD_PADDING_RIGHT, self.filaToken, self.columnaToken - len(self.auxLexema))
                    elif self.auxLexema == "padding-bottom":
                        self.addToken(Tipo.PROPIEDAD_PADDING_BOTTOM, self.filaToken, self.columnaToken - len(self.auxLexema))
                    elif self.auxLexema == "padding-top":
                        self.addToken(Tipo.PROPIEDAD_PADDING_TOP, self.filaToken, self.columnaToken - len(self.auxLexema))
                    elif self.auxLexema == "padding":
                        self.addToken(Tipo.PROPIEDAD_PADDING, self.filaToken, self.columnaToken - len(self.auxLexema))
                    elif self.auxLexema == "display":
                        self.addToken(Tipo.PROPIEDAD_DISPLAY, self.filaToken, self.columnaToken - len(self.auxLexema))
                    elif self.auxLexema == "line-height":
                        self.addToken(Tipo.PROPIEDAD_LINE_HEIGHT, self.filaToken, self.columnaToken - len(self.auxLexema))
                    elif self.auxLexema == "width":
                        self.addToken(Tipo.PROPIEDAD_WIDTH, self.filaToken, self.columnaToken - len(self.auxLexema))
                    elif self.auxLexema == "height":
                        self.addToken(Tipo.PROPIEDAD_HEIGHT, self.filaToken, self.columnaToken - len(self.auxLexema))
                    elif self.auxLexema == "margin-top":
                        self.addToken(Tipo.PROPIEDAD_MARGIN_TOP, self.filaToken, self.columnaToken - len(self.auxLexema))
                    elif self.auxLexema == "margin-right":
                        self.addToken(Tipo.PROPIEDAD_MARGIN_RIGHT, self.filaToken, self.columnaToken - len(self.auxLexema))
                    elif self.auxLexema == "margin-bottom":
                        self.addToken(Tipo.PROPIEDAD_MARGIN_BOTTOM, self.filaToken, self.columnaToken - len(self.auxLexema))
                    elif self.auxLexema == "margin-left":
                        self.addToken(Tipo.PROPIEDAD_MARGIN_LEFT, self.filaToken, self.columnaToken - len(self.auxLexema))
                    elif self.auxLexema == "margin":
                        self.addToken(Tipo.PROPIEDAD_MARGIN, self.filaToken, self.columnaToken - len(self.auxLexema))
                    elif self.auxLexema == "border-style":
                        self.addToken(Tipo.PROPIEDAD_BORDER_STYLE, self.filaToken, self.columnaToken - len(self.auxLexema))
                    elif self.auxLexema == "position":
                        self.addToken(Tipo.PROPIEDAD_POSITION, self.filaToken, self.columnaToken - len(self.auxLexema))
                    elif self.auxLexema == "bottom":
                        self.addToken(Tipo.PROPIEDAD_BOTTOM, self.filaToken, self.columnaToken - len(self.auxLexema))
                    elif self.auxLexema == "top":
                        self.addToken(Tipo.PROPIEDAD_TOP, self.filaToken, self.columnaToken - len(self.auxLexema))
                    elif self.auxLexema == "right":
                        self.addToken(Tipo.PROPIEDAD_RIGHT, self.filaToken, self.columnaToken - len(self.auxLexema))
                    elif self.auxLexema == "left":
                        self.addToken(Tipo.PROPIEDAD_LEFT, self.filaToken, self.columnaToken - len(self.auxLexema))
                    elif self.auxLexema == "float":
                        self.addToken(Tipo.PROPIEDAD_FLOAT, self.filaToken, self.columnaToken - len(self.auxLexema))
                    elif self.auxLexema == "clear":
                        self.addToken(Tipo.PROPIEDAD_CLEAR, self.filaToken, self.columnaToken - len(self.auxLexema))
                    elif self.auxLexema == "max-width":
                        self.addToken(Tipo.PROPIEDAD_MAX_WIDTH, self.filaToken, self.columnaToken - len(self.auxLexema))
                    elif self.auxLexema == "min-width":
                        self.addToken(Tipo.PROPIEDAD_MIN_WIDTH, self.filaToken, self.columnaToken - len(self.auxLexema))
                    elif self.auxLexema == "max-height":
                        self.addToken(Tipo.PROPIEDAD_MAX_HEIGHT, self.filaToken, self.columnaToken - len(self.auxLexema))
                    elif self.auxLexema == "min-height":
                        self.addToken(Tipo.PROPIEDAD_MIN_HEIGHT, self.filaToken, self.columnaToken - len(self.auxLexema))
                    elif self.auxLexema == "content":
                        self.addToken(Tipo.PROPIEDAD_CONTENT, self.filaToken, self.columnaToken - len(self.auxLexema))
                    elif self.auxLexema == "border-top":
                        self.addToken(Tipo.PROPIEDAD_BORDER_TOP, self.filaToken, self.columnaToken - len(self.auxLexema))
                    elif self.auxLexema == "px":
                        self.addToken(Tipo.RESERVADA_PX, self.filaToken, self.columnaToken - len(self.auxLexema))
                    elif self.auxLexema == "em":
                        self.addToken(Tipo.RESERVADA_EM, self.filaToken, self.columnaToken - len(self.auxLexema))
                    elif self.auxLexema == "rem":
                        self.addToken(Tipo.RESERVADA_REM, self.filaToken, self.columnaToken - len(self.auxLexema))
                    elif self.auxLexema == "vh":
                        self.addToken(Tipo.RESERVADA_VH, self.filaToken, self.columnaToken - len(self.auxLexema))
                    elif self.auxLexema == "vw":
                        self.addToken(Tipo.RESERVADA_VW, self.filaToken, self.columnaToken - len(self.auxLexema))
                    elif self.auxLexema == "in":
                        self.addToken(Tipo.RESERVADA_IN, self.filaToken, self.columnaToken - len(self.auxLexema))
                    elif self.auxLexema == "cm":
                        self.addToken(Tipo.RESERVADA_CM, self.filaToken, self.columnaToken - len(self.auxLexema))
                    elif self.auxLexema == "mm":
                        self.addToken(Tipo.RESERVADA_MM, self.filaToken, self.columnaToken - len(self.auxLexema))
                    elif self.auxLexema == "pt":
                        self.addToken(Tipo.RESERVADA_PT, self.filaToken, self.columnaToken - len(self.auxLexema))
                    elif self.auxLexema == "pc":
                        self.addToken(Tipo.RESERVADA_PC, self.filaToken, self.columnaToken - len(self.auxLexema))
                    elif self.auxLexema == "relative":
                        self.addToken(Tipo.RESERVADA_RELATIVE, self.filaToken, self.columnaToken - len(self.auxLexema))
                    elif self.auxLexema == "inline-block":
                        self.addToken(Tipo.RESERVADA_INLINE_BLOCK, self.filaToken, self.columnaToken - len(self.auxLexema))
                    elif self.auxLexema == "red":
                        self.addToken(Tipo.RESERVADA_RED, self.filaToken, self.columnaToken - len(self.auxLexema))
                    elif self.auxLexema == "rgba":
                        self.addToken(Tipo.RESERVADA_RGBA, self.filaToken, self.columnaToken - len(self.auxLexema))
                    elif self.auxLexema == "url":
                        self.addToken(Tipo.RESERVADA_URL, self.filaToken, self.columnaToken - len(self.auxLexema))
                    elif self.auxLexema == "content":
                        self.addToken(Tipo.RESERVADA_CONTENT, self.filaToken, self.columnaToken - len(self.auxLexema))
                    elif self.auxLexema == "inherit":
                        self.addToken(Tipo.RESERVADA_INHERIT, self.filaToken, self.columnaToken - len(self.auxLexema))
                    elif self.auxLexema == "solid":
                        self.addToken(Tipo.RESERVADA_SOLID, self.filaToken, self.columnaToken - len(self.auxLexema))
                    elif self.auxLexema == "absolute":
                        self.addToken(Tipo.RESERVADA_ABSOLUTE, self.filaToken, self.columnaToken - len(self.auxLexema))
                    elif self.auxLexema == "arial":
                        self.addToken(Tipo.RESERVADA_ARIAL, self.filaToken, self.columnaToken - len(self.auxLexema))
                    elif self.auxLexema == "sans-serif":
                        self.addToken(Tipo.RESERVADA_SANS_SERIF, self.filaToken, self.columnaToken - len(self.auxLexema))
                    elif self.auxLexema == "block":
                        self.addToken(Tipo.RESERVADA_BLOCK, self.filaToken, self.columnaToken - len(self.auxLexema))
                    else:
                        self.addToken(Tipo.IDENTIFICADOR, self.filaToken, self.columnaToken - len(self.auxLexema))
                    i -= 1
                    self.columnaToken -= 1
            #ESTADO S2
            elif self.estado == 2:
                if self.c.isdigit():
                    self.estado = 2
                    self.auxLexema += self.c
                elif self.c == ".":
                    self.estado = 6
                    self.auxLexema += self.c
                else:
                    self.addToken(Tipo.NUMERO_ENTERO, self.filaToken, self.columnaToken - len(self.auxLexema))
                    i -= 1
                    self.columnaToken -= 1
            #ESTADO S3
            elif self.estado == 3:
                if self.auxLexema == '{':
                    self.addToken(Tipo.LLAVE_IZQ, self.filaToken, self.columnaToken - len(self.auxLexema))
                elif self.auxLexema == '}':
                    self.addToken(Tipo.LLAVE_DER, self.filaToken, self.columnaToken - len(self.auxLexema))
                elif self.auxLexema == '(':
                    self.addToken(Tipo.PARENTESIS_IZQ, self.filaToken, self.columnaToken - len(self.auxLexema))
                elif self.auxLexema == ')':
                    self.addToken(Tipo.PARENTESIS_DER, self.filaToken, self.columnaToken - len(self.auxLexema))
                elif self.auxLexema == ';':
                    self.addToken(Tipo.PUNTO_Y_COMA, self.filaToken, self.columnaToken - len(self.auxLexema))
                elif self.auxLexema == ':':
                    self.addToken(Tipo.DOS_PUNTOS, self.filaToken, self.columnaToken - len(self.auxLexema))
                elif self.auxLexema == '.':
                    self.addToken(Tipo.PUNTO, self.filaToken, self.columnaToken - len(self.auxLexema))
                elif self.auxLexema == ',':
                    self.addToken(Tipo.COMA, self.filaToken, self.columnaToken - len(self.auxLexema))
                elif self.auxLexema == '-':
                    self.addToken(Tipo.SIGNO_MENOS, self.filaToken, self.columnaToken - len(self.auxLexema))
                elif self.auxLexema == '*':
                    self.addToken(Tipo.SIGNO_POR, self.filaToken, self.columnaToken - len(self.auxLexema))
                elif self.auxLexema == '%':
                    self.addToken(Tipo.SIGNO_PORCENTAJE, self.filaToken, self.columnaToken - len(self.auxLexema))
                elif self.auxLexema == '#':
                    self.addToken(Tipo.SIGNO_NUMERAL, self.filaToken, self.columnaToken - len(self.auxLexema))
                i -= 1
                self.columnaToken -= 1
            #ESTADO S4
            elif self.estado == 4:
                if self.c == "\"":
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
                else:
                    self.addTokenError(self.auxLexema, self.filaToken, self.columnaToken - len(self.auxLexema))
                    i -= 1
                    self.columnaToken -= 1
            #ESTADO S6
            elif self.estado == 6:
                if self.c.isdigit():
                    self.estado = 9
                    self.auxLexema += self.c
                else:
                    self.addTokenError(self.auxLexema, self.filaToken, self.columnaToken - len(self.auxLexema))
                    i -= 1
                    self.columnaToken -= 1
            #ESTADO S7
            elif self.estado == 7:
                self.addToken(Tipo.CADENA_STRING, self.filaToken, self.columnaToken  - len(self.auxLexema))
                i -= 1
                self.columnaToken -= 1
            #ESTADO S8
            elif self.estado == 8:
                if self.c == "*":
                    self.estado = 10
                    self.auxLexema += self.c
                else:
                    #---Validaciones para COMENTARIO_BLOQUE-----
                    if self.c == "$" and i == len(self.textoDocumento) - 1:   #validacion si el COMENTARIO_BLOQUE esta en la ultima linea
                        if self.inicioComentarioBloque:
                            self.addTokenError(self.auxLexema, self.filaComentarioBloque, self.columnaComentarioBloque)
                        else:
                            self.addTokenError(self.auxLexema, self.filaToken, self.columnaToken - len(self.auxLexema))
                        #i -= 1
                        self.columnaToken -= 1      #Se reduce en 1 columnaToken para no alterar la posición de #
                        continue
                    elif self.c == "\n":          #Incrementa la filaToken para no perder la posición durante un comentario bloque
                        if self.inicioComentarioBloque == False:        #Indica cuando comienza el comentario bloque para obtener la posición columna y fila
                            self.columnaComentarioBloque = self.columnaToken - len(self.auxLexema)
                            self.filaComentarioBloque = self.filaToken
                            self.inicioComentarioBloque = True
                        self.filaToken += 1
                        self.columnaToken = 0
                    #---Validaciones para COMENTARIO_BLOQUE-----
                    self.estado = 8
                    self.auxLexema += self.c
            #ESTADO S9
            elif self.estado == 9:
                if self.c.isdigit():
                    self.estado = 9
                    self.auxLexema += self.c
                else:
                    self.addToken(Tipo.NUMERO_DECIMAL, self.filaToken, self.columnaToken - len(self.auxLexema))
                    i -= 1
                    self.columnaToken -= 1
            #ESTADO S10
            elif self.estado == 10:
                if self.c == "/":
                    self.estado = 11
                    self.auxLexema += self.c
                elif self.c == "*":
                    self.estado = 8
                    i -= 1
                    self.columnaToken -= 1
                else:
                    #---Validaciones para COMENTARIO_BLOQUE-----
                    if self.c == "$" and i == len(self.textoDocumento) - 1:   #validacion si el COMENTARIO_BLOQUE esta en la ultima linea
                        if self.inicioComentarioBloque:
                            self.addTokenError(self.auxLexema, self.filaComentarioBloque, self.columnaComentarioBloque)
                        else:
                            self.addTokenError(self.auxLexema, self.filaToken, self.columnaToken - len(self.auxLexema))
                        self.columnaToken -= 1      #Se reduce en 1 columnaToken para no alterar la posición de #
                        continue
                    elif self.c == "\n":          #Incrementa la filaToken para no perder la posición durante un comentario bloque
                        if self.inicioComentarioBloque == False:        #Indica cuando comienza el comentario bloque para obtener la posición columna y fila
                            self.columnaComentarioBloque = self.columnaToken - len(self.auxLexema)
                            self.filaComentarioBloque = self.filaToken
                            self.inicioComentarioBloque = True
                        self.filaToken += 1
                        self.columnaToken = 0
                    #---Validaciones para COMENTARIO_BLOQUE-----
                    self.estado = 8
                    self.auxLexema += self.c
            #ESTADO S11
            elif self.estado == 11:
                if self.inicioComentarioBloque:
                    self.addToken(Tipo.COMENTARIO, self.filaComentarioBloque, self.columnaComentarioBloque)
                    #---Validaciones para COMENTARIO_BLOQUE-----
                    self.columnaComentarioBloque = 0
                    self.filaComentarioBloque = 0
                    self.inicioComentarioBloque = False
                    #---Validaciones para COMENTARIO_BLOQUE-----
                else:
                    self.addToken(Tipo.COMENTARIO, self.filaToken, self.columnaToken - len(self.auxLexema))
                i -= 1
                self.columnaToken -= 1
            i += 1
        
        return self.lista_Tokens

    def analizador_Error(self):
        return self.lista_Errores
    
    def addToken(self, tipo, fila, columna):
        nuevoToken = Token_Css(tipo, self.auxLexema, fila, columna)
        self.appendND += self.auxLexema # Recolector de caracteres
        self.lista_Tokens.append(nuevoToken)
        self.auxLexema = ""
        self.estado = 0

    def addTokenError(self, caracter, fila, columna):
        if self.auxLexema == "":
            nuevoError = Token_Error(caracter, TipoError.LEXICO, "El simbolo no pertenece al lenguaje", fila, columna)
        else:
            nuevoError = Token_Error(caracter, TipoError.LEXICO, "Lexema no definido en el lenguaje", fila, columna)
        
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

    def getRecolectorND(self):
        return self.appendND