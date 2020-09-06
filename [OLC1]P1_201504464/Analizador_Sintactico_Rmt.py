from Token_Rmt import Token_Rmt
from Token_Rmt import Tipo
from Estado_Rmt import Estado

class Analizador_Sintactico_Rmt:
    numPreanalisis = int
    listaTokens = list()
    estadoOperacion = Estado

    def parsear(self, listaT):
        self.listaTokens = listaT
        self.preanalisis = Token_Rmt
        self.preanalisis = self.listaTokens[0]
        self.numPreanalisis = 0
        self.esCorrecto = True
        self.Expresion()
    
    def Expresion(self):
        self.E()
        if self.preanalisis.getTipo() == Tipo.DESCONOCIDO and self.esCorrecto:
            self.estadoOperacion = Estado.CORRECTO
        else:
            self.estadoOperacion = Estado.INCORRECTO

    def E(self):
        self.T()
        self.EP()

    def EP(self):
        if self.preanalisis.getTipo() == Tipo.SIGNO_MAS:
            self.match(Tipo.SIGNO_MAS)
            self.T()
            self.EP()
        elif self.preanalisis.getTipo() == Tipo.SIGNO_MENOS:
            self.match(Tipo.SIGNO_MENOS)
            self.T()
            self.EP()

    def T(self):
        self.F()
        self.TP()

    def TP(self):
        if self.preanalisis.getTipo() == Tipo.SIGNO_POR:
            self.match(Tipo.SIGNO_POR)
            self.F()
            self.TP()
        elif self.preanalisis.getTipo() == Tipo.SIGNO_DIVISION:
            self.match(Tipo.SIGNO_DIVISION)
            self.F()
            self.TP()

    def F(self):
        if self.preanalisis.getTipo() == Tipo.PARENTESIS_IZQ:
            self.match(Tipo.PARENTESIS_IZQ)
            self.E()
            self.match(Tipo.PARENTESIS_DER)
        elif self.preanalisis.getTipo() == Tipo.NUMERO:
            self.match(Tipo.NUMERO)
        elif self.preanalisis.getTipo() == Tipo.IDENTIFICADOR:
            self.match(Tipo.IDENTIFICADOR)

    def match(self, tipo):
        if not tipo == self.preanalisis.getTipo():
            print("Se esperaba " + self.getTipoParaError(tipo))
            self.esCorrecto = False
        
        if not self.preanalisis.getTipo() == Tipo.DESCONOCIDO:
            self.numPreanalisis += 1
            self.preanalisis = self.listaTokens[self.numPreanalisis]

    def getTipoParaError(self, tipo):
        
        if tipo == Tipo.NUMERO:
            return "Numero"
        elif tipo == Tipo.IDENTIFICADOR:
            return "Identificador"
        elif tipo == Tipo.SIGNO_MAS:
            return "Signo Mas"
        elif tipo == Tipo.SIGNO_MENOS:
            return "Signo Menos"
        elif tipo == Tipo.SIGNO_POR:
            return "Signo Por"
        elif tipo == Tipo.SIGNO_DIVISION:
            return "Signo Division"
        elif tipo == Tipo.PARENTESIS_IZQ:
            return "Parentesis izquierdo"
        elif tipo == Tipo.PARENTESIS_DER:
            return "Parentesis derecho"
    
    def getEstadoOperacion(self):
        return self.estadoOperacion