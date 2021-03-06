from Token import Token
from Token import Tipo
from Token_Error import Token_Error
from Token_Error import TipoError
from tkinter import messagebox

class Analizador_Lexico_Javascript:
    estado = int
    auxLexema = str
    textoDocumento = str
    lista_Tokens = list
    lista_Errores = list
    appendND = str
    dotID = str
    dotD = str
    dotC = str

    def analizador_Javascript(self, textoDocumento):
        self.estado = 0
        self.auxLexema = ""
        self.textoDocumento = textoDocumento + "#"
        self.lista_Tokens = list()
        self.lista_Errores = list()
        self.c = ''
        self.columnaToken = 0
        self.filaToken = 1
        #---Validaciones para COMENTARIO_BLOQUE-----
        self.estadoComentario = 0  #Guarda el estado anterior del comentario para saber si es de linea o bloque
        self.filaComentarioBloque = 0
        self.columnaComentarioBloque = 0
        self.inicioComentarioBloque = False
        #---Validaciones para COMENTARIO_BLOQUE-----
        self.appendND = ""  #Recolecta todos los caracteres omitiendo los errores
        self.dotID = ""
        self.dotD = ""
        self.dotC = ""
        self.terminoDotID, self.terminoDotD, self.terminoDotC = False, False, False
        self.lexemaDot = ""
        self.estado1Activo = False  #Bandera para saber si el identificador tiene mas de 1 caracter
        self.estado2Activo, self.estado24Activo = False, False   #Bandera para saber si hubo otro número antes de . o aceptacion
        self.estado16Activo = False #Bandera para saber si el comentario fue recursivo

        i = 0
        while i < len(self.textoDocumento):
            self.c = self.textoDocumento[i]
            self.columnaToken += 1

            #ESTADO S0
            if self.estado == 0:
                if self.c.isalpha():
                    self.estado = 1
                    self.auxLexema += self.c
                    if self.terminoDotID == False:
                        self.dotID = "digraph G{\nnode[shape = circle]\n\nS0 -> S1[label = \""+ self.c +"\"]\n"
                elif self.c.isdigit():
                    self.estado = 2
                    self.auxLexema += self.c
                    if self.terminoDotD == False:
                        self.dotD = "digraph G{\nnode[shape = circle]\n\nS0 -> S2[label = \""+ self.c +"\"]\n"
                elif (self.c == '{' or self.c == '}' or self.c == '(' or self.c == ')'
                    or self.c == ';' or self.c == ':' or self.c == '.' or self.c == ','):
                    self.estado = 3
                    self.auxLexema += self.c
                elif self.c == "\"":
                    self.estado = 4
                    self.auxLexema += self.c
                elif self.c == "\'":
                    self.estado = 5
                    self.auxLexema += self.c
                elif self.c == "/":
                    self.estado = 6
                    self.auxLexema += self.c
                    if self.terminoDotC == False:
                        self.lexemaDot = self.c + " "
                elif self.c == "&":
                    self.estado = 7
                    self.auxLexema += self.c
                elif self.c == "|":
                    self.estado = 8
                    self.auxLexema += self.c
                elif self.c == "+":
                    self.estado = 9
                    self.auxLexema += self.c
                elif self.c == "-":
                    self.estado = 10
                    self.auxLexema += self.c
                elif self.c == "=":
                    self.estado = 11
                    self.auxLexema += self.c
                elif (self.c == '<' or self.c == '>' or self.c == '!' or self.c == '*'):
                    self.estado = 12
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
                    if self.c == "#" and i == len(self.textoDocumento) - 1:
                        if len(self.lista_Errores) > 0:
                            messagebox.showerror("Alerta", "Se han encontrado errores léxicos")
                            #self.imprimirListaErrores()
                        messagebox.showinfo("Aviso", "Análisis léxico satisfactorio")
                    else:
                        self.addTokenError(self.c, self.filaToken, self.columnaToken)
            #ESTADO S1
            elif self.estado == 1:
                if self.c.isalpha() or self.c.isdigit() or self.c == "_":
                    self.estado = 1
                    self.auxLexema += self.c
                    if self.terminoDotID == False:
                        self.lexemaDot += self.c + " "
                        self.estado1Activo = True
                else:
                    if self.terminoDotID == False:
                        if self.estado1Activo:
                            self.dotID += "S1 -> S1[label = \""+ self.lexemaDot +"\"]\n"
                        self.dotID += "S1[shape=doublecircle]\n}"
                        self.lexemaDot = ""

                    if self.auxLexema == "var":
                        self.addToken(Tipo.RESERVADA_VAR, self.filaToken, self.columnaToken - len(self.auxLexema))
                    elif self.auxLexema == "int":
                        self.addToken(Tipo.RESERVADA_INT, self.filaToken, self.columnaToken - len(self.auxLexema))
                    elif self.auxLexema == "string":
                        self.addToken(Tipo.RESERVADA_STRING, self.filaToken, self.columnaToken - len(self.auxLexema))
                    elif self.auxLexema == "char":
                        self.addToken(Tipo.RESERVADA_CHAR, self.filaToken, self.columnaToken - len(self.auxLexema))
                    elif self.auxLexema == "boolean":
                        self.addToken(Tipo.RESERVADA_BOOLEAN, self.filaToken, self.columnaToken - len(self.auxLexema))
                    elif self.auxLexema == "if":
                        self.addToken(Tipo.RESERVADA_IF, self.filaToken, self.columnaToken - len(self.auxLexema))
                    elif self.auxLexema == "else":
                        self.addToken(Tipo.RESERVADA_ELSE, self.filaToken, self.columnaToken - len(self.auxLexema))
                    elif self.auxLexema == "for":
                        self.addToken(Tipo.RESERVADA_FOR, self.filaToken, self.columnaToken - len(self.auxLexema))
                    elif self.auxLexema == "while":
                        self.addToken(Tipo.RESERVADA_WHILE, self.filaToken, self.columnaToken - len(self.auxLexema))
                    elif self.auxLexema == "do":
                        self.addToken(Tipo.RESERVADA_DO, self.filaToken, self.columnaToken - len(self.auxLexema))
                    elif self.auxLexema == "continue":
                        self.addToken(Tipo.RESERVADA_CONTINUE, self.filaToken, self.columnaToken - len(self.auxLexema))
                    elif self.auxLexema == "break":
                        self.addToken(Tipo.RESERVADA_BREAK, self.filaToken, self.columnaToken - len(self.auxLexema))
                    elif self.auxLexema == "return":
                        self.addToken(Tipo.RESERVADA_RETURN, self.filaToken, self.columnaToken - len(self.auxLexema))
                    elif self.auxLexema == "constructor":
                        self.addToken(Tipo.RESERVADA_CONTRUCTOR, self.filaToken, self.columnaToken - len(self.auxLexema))
                    elif self.auxLexema == "function":
                        self.addToken(Tipo.RESERVADA_FUNCTION, self.filaToken, self.columnaToken - len(self.auxLexema))
                    elif self.auxLexema == "class":
                        self.addToken(Tipo.RESERVADA_CLASS, self.filaToken, self.columnaToken - len(self.auxLexema))
                    elif self.auxLexema == "Math":
                        self.addToken(Tipo.RESERVADA_MATH, self.filaToken, self.columnaToken - len(self.auxLexema))
                    elif self.auxLexema == "pow":
                        self.addToken(Tipo.RESERVADA_POW, self.filaToken, self.columnaToken - len(self.auxLexema))
                    elif self.auxLexema == "true":
                        self.addToken(Tipo.RESERVADA_TRUE, self.filaToken, self.columnaToken - len(self.auxLexema))
                    elif self.auxLexema == "false":
                        self.addToken(Tipo.RESERVADA_FALSE, self.filaToken, self.columnaToken - len(self.auxLexema))
                    elif self.auxLexema == "this":
                        self.addToken(Tipo.RESERVADA_THIS, self.filaToken, self.columnaToken - len(self.auxLexema))
                    elif self.auxLexema == "console":
                        self.addToken(Tipo.RESERVADA_CONSOLE, self.filaToken, self.columnaToken - len(self.auxLexema))
                    else:
                        self.addToken(Tipo.VARIABLE, self.filaToken, self.columnaToken - len(self.auxLexema))
                    i -= 1
                    self.columnaToken -= 1
                    self.terminoDotID = True
            #ESTADO S2
            elif self.estado == 2:
                if self.c.isdigit():
                    self.estado = 2
                    self.auxLexema += self.c
                    if self.terminoDotD == False:
                        self.lexemaDot += self.c + " "
                        self.estado2Activo = True   #Bandera para saber si hubo otro número antes de . o aceptacion
                elif self.c == ".":
                    self.estado = 13
                    self.auxLexema += self.c
                    if self.terminoDotD == False:
                        if self.estado2Activo:
                            self.dotD += "S2 -> S2[label = \""+ self.lexemaDot +"\"]\n"
                        self.dotD += "S2 -> S13[label = \""+ self.c +"\"]\n"
                        self.lexemaDot = ""
                else:
                    if self.terminoDotD == False:
                        if self.estado2Activo:
                            self.dotD += "S2 -> S2[label = \""+ self.lexemaDot +"\"]\n"
                        self.dotD += "S2[shape=doublecircle]\n}"
                        self.lexemaDot = ""
                    self.addToken(Tipo.NUMERO_ENTERO, self.filaToken, self.columnaToken - len(self.auxLexema))
                    i -= 1
                    self.columnaToken -= 1
                    self.terminoDotD = True
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
                i -= 1
                self.columnaToken -= 1
            #ESTADO S4
            elif self.estado == 4:
                if self.c == "\"":
                    self.estado = 14
                    self.auxLexema += self.c
                else:
                    self.estado = 4
                    self.auxLexema += self.c
            #ESTADO S5
            elif self.estado == 5:
                if self.c == "\'":
                    self.estado = 15
                    self.auxLexema += self.c
                else:
                    self.estado = 5
                    self.auxLexema += self.c
            #ESTADO S6
            elif self.estado == 6:
                if self.c == "*":
                    self.estado = 16
                    self.auxLexema += self.c
                    if self.terminoDotC == False:
                        self.dotC = "digraph G{\nnode[shape = circle]\n\nS0 -> S6[label = \""+ self.lexemaDot +"\"]\n"
                        self.dotC += "S6 -> S16[label = \""+ self.c +"\"]\n"
                        self.lexemaDot = ""
                elif self.c == "/":
                    self.estado = 17
                    self.auxLexema += self.c
                    if self.terminoDotC == False:
                        self.lexemaDot = ""
                else:
                    self.addToken(Tipo.SIGNO_DIVISION, self.filaToken, self.columnaToken - len(self.auxLexema))
                    i -= 1
                    self.columnaToken -= 1
                    if self.terminoDotC == False:
                        self.lexemaDot = ""
            #ESTADO S7
            elif self.estado == 7:
                if self.c == "&":
                    self.estado = 18
                    self.auxLexema += self.c
                else:
                    self.addTokenError(self.auxLexema, self.filaToken, self.columnaToken - len(self.auxLexema))
                    i -= 1
                    self.columnaToken -= 1
            #ESTADO S8
            elif self.estado == 8:
                if self.c == "|":
                    self.estado = 19
                    self.auxLexema += self.c
                else:
                    self.addTokenError(self.auxLexema, self.filaToken, self.columnaToken - len(self.auxLexema))
                    i -= 1
                    self.columnaToken -= 1
            #ESTADO S9
            elif self.estado == 9:
                if self.c == "+" or self.c == "=":
                    self.estado = 20
                    self.auxLexema += self.c
                else:
                    self.addToken(Tipo.SIGNO_MAS, self.filaToken, self.columnaToken - len(self.auxLexema))
                    i -= 1
                    self.columnaToken -= 1
            #ESTADO S10
            elif self.estado == 10:
                if self.c == "-" or self.c == "=":
                    self.estado = 21
                    self.auxLexema += self.c
                else:
                    self.addToken(Tipo.SIGNO_MENOS, self.filaToken, self.columnaToken - len(self.auxLexema))
                    i -= 1
                    self.columnaToken -= 1
            #ESTADO S11
            elif self.estado == 11:
                if self.c == ">" or self.c == "=":
                    self.estado = 22
                    self.auxLexema += self.c
                else:
                    self.addToken(Tipo.SIGNO_IGUAL, self.filaToken, self.columnaToken - len(self.auxLexema))
                    i -= 1
                    self.columnaToken -= 1
            #ESTADO S12
            elif self.estado == 12:
                if self.c == "=":
                    self.estado = 23
                    self.auxLexema += self.c
                else:
                    if self.auxLexema == '<':
                        self.addToken(Tipo.SIGNO_MENOR_QUE, self.filaToken, self.columnaToken - len(self.auxLexema))
                    elif self.auxLexema == '>':
                        self.addToken(Tipo.SIGNO_MAYOR_QUE, self.filaToken, self.columnaToken - len(self.auxLexema))
                    elif self.auxLexema == '!':
                        self.addToken(Tipo.SIGNO_NEGACION, self.filaToken, self.columnaToken - len(self.auxLexema))
                    elif self.auxLexema == '*':
                        self.addToken(Tipo.SIGNO_POR, self.filaToken, self.columnaToken - len(self.auxLexema))
                    i -= 1
                    self.columnaToken -= 1
            #ESTADO S13
            elif self.estado == 13:
                if self.c.isdigit():
                    self.estado = 24
                    self.auxLexema += self.c
                    if self.terminoDotD == False:
                        self.dotD += "S13 -> S24[label = \""+ self.c +"\"]\n"
                        self.lexemaDot = ""
                else:
                    if self.terminoDotD == False:
                        self.dotD += "S13 -> S0[label = \"Error: "+ self.c +"\"]\n"
                        self.dotD += "S2[shape=doublecircle]\n}"
                        self.lexemaDot = ""
                    self.addTokenError(self.auxLexema, self.filaToken, self.columnaToken - len(self.auxLexema))
                    i -= 1
                    self.columnaToken -= 1
                    self.terminoDotD = True
            #ESTADO S14
            elif self.estado == 14:
                self.addToken(Tipo.CADENA_STRING, self.filaToken, self.columnaToken  - len(self.auxLexema))
                i -= 1
                self.columnaToken -= 1
            #ESTADO S15
            elif self.estado == 15:
                self.addToken(Tipo.CADENA_STRING, self.filaToken, self.columnaToken  - len(self.auxLexema))
                i -= 1
                self.columnaToken -= 1
            #ESTADO S16
            elif self.estado == 16:
                if self.c == "*":
                    self.estado = 25
                    self.auxLexema += self.c
                    if self.terminoDotC == False:
                        if not self.textoDocumento[i + 1] == "/":
                            self.lexemaDot += self.c + " "
                else:
                    #---Validaciones para COMENTARIO_BLOQUE-----
                    if self.c == "#" and i == len(self.textoDocumento) - 1:   #validacion si el COMENTARIO_BLOQUE esta en la ultima linea
                        if self.inicioComentarioBloque:
                            if self.terminoDotC == False:
                                self.dotC += "S16 -> S0[label = \"Error: "+ self.lexemaDot +"\"]\n"
                                self.dotC += "S6[shape=doublecircle]\n}"
                                self.lexemaDot = ""
                            self.addTokenError(self.auxLexema, self.filaComentarioBloque, self.columnaComentarioBloque)
                        else:
                            if self.terminoDotC == False:
                                self.dotC += "S16 -> S0[label = \"Error: "+ self.lexemaDot +"\"]\n"
                                self.dotC += "S6[shape=doublecircle]\n}"
                                self.lexemaDot = ""
                            self.addTokenError(self.auxLexema, self.filaToken, self.columnaToken - len(self.auxLexema))
                        #i -= 1
                        self.columnaToken -= 1      #Se reduce en 1 columnaToken para no alterar la posición de #
                        self.terminoDotC = True
                        continue
                    elif self.c == "\n":          #Incrementa la filaToken para no perder la posición durante un comentario bloque
                        if self.inicioComentarioBloque == False:        #Indica cuando comienza el comentario bloque para obtener la posición columna y fila
                            self.columnaComentarioBloque = self.columnaToken - len(self.auxLexema)
                            self.filaComentarioBloque = self.filaToken
                            self.inicioComentarioBloque = True
                        self.filaToken += 1
                        self.columnaToken = 0
                    #---Validaciones para COMENTARIO_BLOQUE-----
                    self.estado = 16
                    self.auxLexema += self.c
                    if self.terminoDotC == False:
                        if self.c == "\"":
                            self.lexemaDot += "\\" + self.c + " "
                        else:
                            self.lexemaDot += self.c + " "
                        self.estado16Activo = True
            #ESTADO S17
            elif self.estado == 17:
                if self.c == "\n":
                    self.estado = 26
                    #---Validaciones para COMENTARIO_LINEA-----
                    self.estadoComentario = 17
                    i -= 1                      #Se reduce en 1 el iterador i para analizar el \n ya que no se adjunta a la cadena
                    self.columnaToken -= 1
                    #---Validaciones para COMENTARIO_LINEA-----
                elif self.c == "#" and i == len(self.textoDocumento) - 1:   #validacion si el COMENTARIO_LINEA esta en la ultima linea
                    self.estado = 26
                    #---Validaciones para COMENTARIO_LINEA-----
                    self.estadoComentario = 17
                    i -= 1
                    self.columnaToken -= 1      #Se reduce en 1 columnaToken para analizar el \n ya que no se adjunta a la cadena
                    #---Validaciones para COMENTARIO_LINEA-----
                else:
                    self.estado = 17
                    self.auxLexema += self.c
            #ESTADO S18
            elif self.estado == 18:
                self.addToken(Tipo.SIGNO_AND, self.filaToken, self.columnaToken - len(self.auxLexema))
                i -= 1
                self.columnaToken -= 1
            #ESTADO S19
            elif self.estado == 19:
                self.addToken(Tipo.SIGNO_OR, self.filaToken, self.columnaToken - len(self.auxLexema))
                i -= 1
                self.columnaToken -= 1
            #ESTADO S20
            elif self.estado == 20:
                if self.auxLexema == "++":
                    self.addToken(Tipo.SIGNO_POS_INCREMENTO, self.filaToken, self.columnaToken - len(self.auxLexema))
                elif self.auxLexema == "+=":
                    self.addToken(Tipo.SIGNO_SUMA_CONCATENADA, self.filaToken, self.columnaToken - len(self.auxLexema))
                i -= 1
                self.columnaToken -= 1
            #ESTADO S21
            elif self.estado == 21:
                if self.auxLexema == "--":
                    self.addToken(Tipo.SIGNO_POS_DECREMENTO, self.filaToken, self.columnaToken - len(self.auxLexema))
                elif self.auxLexema == "-=":
                    self.addToken(Tipo.SIGNO_RESTA_CONCATENADA, self.filaToken, self.columnaToken - len(self.auxLexema))
                i -= 1
                self.columnaToken -= 1
            #ESTADO S22
            elif self.estado == 22:
                if self.auxLexema == "=>":
                    self.addToken(Tipo.SIGNO_LAMBDA, self.filaToken, self.columnaToken - len(self.auxLexema))
                elif self.auxLexema == "==":
                    self.addToken(Tipo.SIGNO_DOBLE_IGUAL, self.filaToken, self.columnaToken - len(self.auxLexema))
                i -= 1
                self.columnaToken -= 1
            #ESTADO S23
            elif self.estado == 23:
                if self.auxLexema == "<=":
                    self.addToken(Tipo.SIGNO_MENOR_IGUAL_QUE, self.filaToken, self.columnaToken - len(self.auxLexema))
                elif self.auxLexema == ">=":
                    self.addToken(Tipo.SIGNO_MAYOR_IGUAL_QUE, self.filaToken, self.columnaToken - len(self.auxLexema))
                elif self.auxLexema == "!=":
                    self.addToken(Tipo.SIGNO_DIFERENTE_DE, self.filaToken, self.columnaToken - len(self.auxLexema))
                elif self.auxLexema == "*=":
                    self.addToken(Tipo.SIGNO_ASIGNACION, self.filaToken, self.columnaToken - len(self.auxLexema))
                i -= 1
                self.columnaToken -= 1
            #ESTADO S24
            elif self.estado == 24:
                if self.c.isdigit():
                    self.estado = 24
                    self.auxLexema += self.c
                    if self.terminoDotD == False:
                        self.lexemaDot += self.c + " "
                        self.estado24Activo = True
                else:
                    if self.terminoDotD == False:
                        if self.estado24Activo:
                            self.dotD += "S24 -> S24[label = \""+ self.lexemaDot +"\"]\n"
                        self.dotD += "S2[shape=doublecircle]\n"
                        self.dotD += "S24[shape=doublecircle]\n}"
                        self.lexemaDot = ""
                    self.addToken(Tipo.NUMERO_DECIMAL, self.filaToken, self.columnaToken - len(self.auxLexema))
                    i -= 1
                    self.columnaToken -= 1
                    self.terminoDotD = True
            #ESTADO S25
            elif self.estado == 25:
                if self.c == "/":
                    self.estado = 26
                    self.auxLexema += self.c
                    #---Validaciones para COMENTARIO_BLOQUE-----
                    self.estadoComentario = 25
                    #---Validaciones para COMENTARIO_BLOQUE-----
                    if self.terminoDotC == False:
                        if self.estado16Activo:
                            self.dotC += "S16 -> S16[label = \""+ self.lexemaDot +"\"]\n"
                        self.dotC += "S16 -> S25[label = \"*\"]\n"
                        self.dotC += "S25 -> S26[label = \""+ self.c +"\"]\n"
                        self.lexemaDot = ""
                elif self.c == "*":
                    #Cofigo prueba----FUNCIONO EXCELENTE
                    self.estado = 16
                    i -= 1
                    self.columnaToken -= 1
                    #Cofigo prueba----FUNCIONO EXCELENTE
                    #Codigo original-------
                    #self.estado = 25
                    #self.auxLexema += self.c
                    #Codigo original-------
                else:
                    #---Validaciones para COMENTARIO_BLOQUE-----
                    if self.c == "#" and i == len(self.textoDocumento) - 1:   #validacion si el COMENTARIO_BLOQUE esta en la ultima linea
                        if self.inicioComentarioBloque:
                            if self.terminoDotC == False:
                                self.dotC += "S25 -> S0[label = \"Error: "+ self.lexemaDot +"\"]\n"
                                self.dotC += "S6[shape=doublecircle]\n}"
                                self.lexemaDot = ""
                            self.addTokenError(self.auxLexema, self.filaComentarioBloque, self.columnaComentarioBloque)
                        else:
                            if self.terminoDotC == False:
                                self.dotC += "S25 -> S0[label = \"Error: "+ self.lexemaDot +"\"]\n"
                                self.dotC += "S6[shape=doublecircle]\n}"
                                self.lexemaDot = ""
                            self.addTokenError(self.auxLexema, self.filaToken, self.columnaToken - len(self.auxLexema))
                        #i -= 1
                        self.columnaToken -= 1      #Se reduce en 1 columnaToken para no alterar la posición de #
                        self.terminoDotC = True
                        continue
                    elif self.c == "\n":          #Incrementa la filaToken para no perder la posición durante un comentario bloque
                        if self.inicioComentarioBloque == False:        #Indica cuando comienza el comentario bloque para obtener la posición columna y fila
                            self.columnaComentarioBloque = self.columnaToken - len(self.auxLexema)
                            self.filaComentarioBloque = self.filaToken
                            self.inicioComentarioBloque = True
                        self.filaToken += 1
                        self.columnaToken = 0
                    #---Validaciones para COMENTARIO_BLOQUE-----
                    self.estado = 16
                    self.auxLexema += self.c
                    if self.terminoDotC == False:
                        if self.c == "\"":
                            self.lexemaDot += "\\" + self.c + " "
                        else:
                            self.lexemaDot += self.c + " "
                        self.estado16Activo = True
            #ESTADO S26
            elif self.estado == 26:
                if self.estadoComentario == 17:
                    self.addToken(Tipo.COMENTARIO_LINEA, self.filaToken, self.columnaToken - len(self.auxLexema))
                else:
                    if self.terminoDotC == False:
                        self.dotC += "S6[shape=doublecircle]\n"
                        self.dotC += "S26[shape=doublecircle]\n}"
                        self.lexemaDot = ""
                    self.addToken(Tipo.COMENTARIO_BLOQUE, self.filaComentarioBloque, self.columnaComentarioBloque)
                    #---Validaciones para COMENTARIO_BLOQUE-----
                    self.columnaComentarioBloque = 0
                    self.filaComentarioBloque = 0
                    self.inicioComentarioBloque = False
                    #---Validaciones para COMENTARIO_BLOQUE-----
                    self.terminoDotC = True
                i -= 1
                self.columnaToken -= 1
            i += 1
        
        return self.lista_Tokens
    
    def analizador_Error(self):
        return self.lista_Errores
    
    def addToken(self, tipo, fila, columna):
        nuevoToken = Token(tipo, self.auxLexema, fila, columna)
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

    def getDotID(self):
        return self.dotID
    
    def getDotD(self):
        return self.dotD

    def getDotC(self):
        return self.dotC

        



        