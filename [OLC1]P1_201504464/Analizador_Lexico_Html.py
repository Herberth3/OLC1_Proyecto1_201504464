from Token_Html import Token_Html
from Token_Html import Tipo
from Token_Error import Token_Error
from Token_Error import TipoError
from tkinter import messagebox

class Analizador_Lexico_Html:
    estado = int
    auxLexema = str
    textoDocumento = str
    lista_Tokens = list
    lista_Errores = list

    def analizador_Html(self, textoDocumento):
        self.estado = 0
        self.auxLexema = ""
        self.textoDocumento = textoDocumento + "#"
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

        i = 0
        while i < len(self.textoDocumento):
            self.c = self.textoDocumento[i]
            self.columnaToken += 1

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
                    self.estado = 5
                    self.auxLexema += self.c
                elif self.c == "\"":
                    self.estado = 6
                    self.auxLexema += self.c
                elif self.c == "\'":
                    self.estado = 7
                    self.auxLexema += self.c
                elif self.c == "<":
                    self.estado = 9
                    self.auxLexema += self.c
                elif self.c == " " or self.c == "\t" or self.c == "\r" or self.c == "\n":
                    i += 1
                    self.estado = 0
                    if self.c == "\n":
                        self.columnaToken = 0
                        self.filaToken += 1
                    continue
                else:
                    if self.c == "#" and i == len(self.textoDocumento) - 1:
                        if len(self.lista_Errores) > 0:
                            messagebox.showerror("Alerta", "Se han encontrado errores léxicos")
                            self.imprimirLista()
                        messagebox.showinfo("Aviso", "Análisis léxico satisfactorio")
                    else:
                        self.addTokenError(self.c, self.filaToken, self.columnaToken)
            #ESTADO S1
            elif self.estado == 1:
                if self.c.isalpha() or self.c.isdigit() or self.c == "-":
                    self.estado = 1
                    self.auxLexema += self.c
                else:
                    if self.auxLexema == "html":
                        self.addToken(Tipo.RESERVADA_HTML, self.filaToken, self.columnaToken - len(self.auxLexema))
                    elif self.auxLexema == "head":
                        self.addToken(Tipo.RESERVADA_HEAD, self.filaToken, self.columnaToken - len(self.auxLexema))
                    elif self.auxLexema == "title":
                        self.addToken(Tipo.RESERVADA_TITLE, self.filaToken, self.columnaToken - len(self.auxLexema))
                    elif self.auxLexema == "body":
                        self.addToken(Tipo.RESERVADA_BODY, self.filaToken, self.columnaToken - len(self.auxLexema))
                    elif self.auxLexema == "h1":
                        self.addToken(Tipo.RESERVADA_H1, self.filaToken, self.columnaToken - len(self.auxLexema))
                    elif self.auxLexema == "h2":
                        self.addToken(Tipo.RESERVADA_H2, self.filaToken, self.columnaToken - len(self.auxLexema))
                    elif self.auxLexema == "h3":
                        self.addToken(Tipo.RESERVADA_H3, self.filaToken, self.columnaToken - len(self.auxLexema))
                    elif self.auxLexema == "h4":
                        self.addToken(Tipo.RESERVADA_H4, self.filaToken, self.columnaToken - len(self.auxLexema))
                    elif self.auxLexema == "h5":
                        self.addToken(Tipo.RESERVADA_H5, self.filaToken, self.columnaToken - len(self.auxLexema))
                    elif self.auxLexema == "h6":
                        self.addToken(Tipo.RESERVADA_H6, self.filaToken, self.columnaToken - len(self.auxLexema))
                    elif self.auxLexema == "p":
                        self.addToken(Tipo.RESERVADA_P, self.filaToken, self.columnaToken - len(self.auxLexema))
                    elif self.auxLexema == "br":
                        self.addToken(Tipo.RESERVADA_BR, self.filaToken, self.columnaToken - len(self.auxLexema))
                    elif self.auxLexema == "img":
                        self.addToken(Tipo.RESERVADA_IMG, self.filaToken, self.columnaToken - len(self.auxLexema))
                    elif self.auxLexema == "src":
                        self.addToken(Tipo.RESERVADA_SRC, self.filaToken, self.columnaToken - len(self.auxLexema))
                    elif self.auxLexema == "alt":
                        self.addToken(Tipo.RESERVADA_ALT, self.filaToken, self.columnaToken - len(self.auxLexema))
                    elif self.auxLexema == "a":
                        self.addToken(Tipo.RESERVADA_A, self.filaToken, self.columnaToken - len(self.auxLexema))
                    elif self.auxLexema == "href":
                        self.addToken(Tipo.RESERVADA_HREF, self.filaToken, self.columnaToken - len(self.auxLexema))
                    elif self.auxLexema == "ol":
                        self.addToken(Tipo.RESERVADA_OL, self.filaToken, self.columnaToken - len(self.auxLexema))
                    elif self.auxLexema == "ul":
                        self.addToken(Tipo.RESERVADA_UL, self.filaToken, self.columnaToken - len(self.auxLexema))
                    elif self.auxLexema == "li":
                        self.addToken(Tipo.RESERVADA_LI, self.filaToken, self.columnaToken - len(self.auxLexema))
                    elif self.auxLexema == "style":
                        self.addToken(Tipo.RESERVADA_STYLE, self.filaToken, self.columnaToken - len(self.auxLexema))
                    elif self.auxLexema == "table":
                        self.addToken(Tipo.RESERVADA_TABLE, self.filaToken, self.columnaToken - len(self.auxLexema))
                    elif self.auxLexema == "th":
                        self.addToken(Tipo.RESERVADA_TH, self.filaToken, self.columnaToken - len(self.auxLexema))
                    elif self.auxLexema == "tr":
                        self.addToken(Tipo.RESERVADA_TR, self.filaToken, self.columnaToken - len(self.auxLexema))
                    elif self.auxLexema == "td":
                        self.addToken(Tipo.RESERVADA_TD, self.filaToken, self.columnaToken - len(self.auxLexema))
                    elif self.auxLexema == "caption":
                        self.addToken(Tipo.RESERVADA_CAPTION, self.filaToken, self.columnaToken - len(self.auxLexema))
                    elif self.auxLexema == "colgroup":
                        self.addToken(Tipo.RESERVADA_COLGROUP, self.filaToken, self.columnaToken - len(self.auxLexema))
                    elif self.auxLexema == "col":
                        self.addToken(Tipo.RESERVADA_COL, self.filaToken, self.columnaToken - len(self.auxLexema))
                    elif self.auxLexema == "thead":
                        self.addToken(Tipo.RESERVADA_THEAD, self.filaToken, self.columnaToken - len(self.auxLexema))
                    elif self.auxLexema == "tbody":
                        self.addToken(Tipo.RESERVADA_TBODY, self.filaToken, self.columnaToken - len(self.auxLexema))
                    elif self.auxLexema == "tfoot":
                        self.addToken(Tipo.RESERVADA_TFOOT, self.filaToken, self.columnaToken - len(self.auxLexema))
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
                    self.estado = 3
                    self.auxLexema += self.c
                else:
                    self.addToken(Tipo.NUMERO_ENTERO, self.filaToken, self.columnaToken - len(self.auxLexema))
                    i -= 1
                    self.columnaToken -= 1
            #ESTADO S3
            elif self.estado == 3:
                if self.c.isdigit():
                    self.estado = 4
                    self.auxLexema += self.c
                else:
                    self.addTokenError(self.auxLexema, self.filaToken, self.columnaToken - len(self.auxLexema))
                    i -= 1
                    self.columnaToken -= 1
            #ESTADO S4
            elif self.estado == 4:
                if self.c.isdigit():
                    self.estado = 4
                    self.auxLexema += self.c
                else:
                    self.addToken(Tipo.NUMERO_DECIMAL, self.filaToken, self.columnaToken - len(self.auxLexema))
                    i -= 1
                    self.columnaToken -= 1
            #ESTADO S5
            elif self.estado == 5:
                if self.auxLexema == '>':
                    self.addToken(Tipo.SIGNO_MAYOR_QUE, self.filaToken, self.columnaToken - len(self.auxLexema))
                elif self.auxLexema == '/':
                    self.addToken(Tipo.SIGNO_DIVISION, self.filaToken, self.columnaToken - len(self.auxLexema))
                elif self.auxLexema == '=':
                    self.addToken(Tipo.SIGNO_IGUAL, self.filaToken, self.columnaToken - len(self.auxLexema))
                elif self.auxLexema == '.':
                    self.addToken(Tipo.PUNTO, self.filaToken, self.columnaToken - len(self.auxLexema))
                elif self.auxLexema == '(':
                    self.addToken(Tipo.PARENTESIS_IZQ, self.filaToken, self.columnaToken - len(self.auxLexema))
                elif self.auxLexema == ')':
                    self.addToken(Tipo.PARENTESIS_DER, self.filaToken, self.columnaToken - len(self.auxLexema))
                i -= 1
                self.columnaToken -= 1
            #ESTADO S6
            elif self.estado == 6:
                if self.c == "\"":
                    self.estado = 8
                    self.auxLexema += self.c
                else:
                    self.estado = 6
                    self.auxLexema += self.c
            #ESTADO S7
            elif self.estado == 7:
                if self.c == "\'":
                    self.estado = 8
                    self.auxLexema += self.c
                else:
                    self.estado = 7
                    self.auxLexema += self.c
            #ESTADO S8
            elif self.estado == 8:
                self.addToken(Tipo.CADENA_STRING, self.filaToken, self.columnaToken  - len(self.auxLexema))
                i -= 1
                self.columnaToken -= 1
            #ESTADO S9
            elif self.estado == 9:
                if self.c == "!":
                    self.estado = 10
                    self.auxLexema += self.c
                else:
                    self.addToken(Tipo.SIGNO_MENOR_QUE, self.filaToken, self.columnaToken - len(self.auxLexema))
                    i -= 1
                    self.columnaToken -= 1
            #ESTADO S10
            elif self.estado == 10:
                if self.c == "-":
                    self.estado = 11
                    self.auxLexema += self.c
                else:
                    self.addTokenError(self.auxLexema, self.filaToken, self.columnaToken - len(self.auxLexema))
                    i -= 1
                    self.columnaToken -= 1
            #ESTADO S11
            elif self.estado == 11:
                if self.c == "-":
                    self.estado = 12
                    self.auxLexema += self.c
                else:
                    self.addTokenError(self.auxLexema, self.filaToken, self.columnaToken - len(self.auxLexema))
                    i -= 1
                    self.columnaToken -= 1
            #ESTADO S12
            elif self.estado == 12:
                if self.c == "-":
                    self.estado = 13
                    self.auxLexema += self.c
                else:
                    #---Validaciones para COMENTARIO_BLOQUE-----
                    if self.c == "#" and i == len(self.textoDocumento) - 1:   #validacion si el COMENTARIO_BLOQUE esta en la ultima linea
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
                    self.estado = 12
                    self.auxLexema += self.c
            #ESTADO S13
            elif self.estado == 13:
                if self.c == "-" and self.textoDocumento[i + 1] == "#":
                    self.estado = 12
                    self.auxLexema += self.c
                elif self.c == "-" and self.textoDocumento[i + 1] == ">":
                    self.estado = 14
                    self.auxLexema += self.c
                elif self.c == "-":
                    self.estado = 13
                    self.auxLexema += self.c
                else:
                    if self.c == "\n":          #Incrementa la filaToken para no perder la posición durante un comentario bloque
                        if self.inicioComentarioBloque == False:        #Indica cuando comienza el comentario bloque para obtener la posición columna y fila
                            self.columnaComentarioBloque = self.columnaToken - len(self.auxLexema)
                            self.filaComentarioBloque = self.filaToken
                            self.inicioComentarioBloque = True
                        self.filaToken += 1
                        self.columnaToken = 0
                    #---Validaciones para COMENTARIO_BLOQUE-----
                    self.estado = 12
                    self.auxLexema += self.c
            #ESTADO S14
            elif self.estado == 14:
                if self.c == ">":
                    self.estado = 15
                    self.auxLexema += self.c
            #ESTADO S15
            elif self.estado == 15:
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
        nuevoToken = Token_Html(tipo, self.auxLexema, fila, columna)
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
    
    def imprimirLista(self):
        self.tokenError = Token_Error
        for self.tokenError in self.lista_Errores:
            print(self.tokenError.getCaracterError() + " Tipo Error: " + self.tokenError.getTipoErrorEnString() + " " + self.tokenError.getDescripcionError() + " Fila: " + str(self.tokenError.getFilaError()) + " Columna: " + str(self.tokenError.getColumnaError()))