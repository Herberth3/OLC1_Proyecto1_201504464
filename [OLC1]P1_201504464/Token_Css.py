from enum import Enum

class Tipo(Enum):
    PROPIEDAD_COLOR = 1
    PROPIEDAD_BACKGROUND_COLOR = 2
    PROPIEDAD_BACKGROUND_IMAGE = 3
    PROPIEDAD_BORDER = 4
    PROPIEDAD_OPACITY = 5
    PROPIEDAD_BACKGROUND = 6
    PROPIEDAD_TEXT_ALIGN = 7
    PROPIEDAD_FONT_FAMILY = 8
    PROPIEDAD_FONT_STYLE = 9
    PROPIEDAD_FONT_WEIGHT = 10
    PROPIEDAD_FONT_SIZE = 11
    PROPIEDAD_FONT = 12
    PROPIEDAD_PADDING_LEFT = 13
    PROPIEDAD_PADDING_RIGHT = 14
    PROPIEDAD_PADDING_BOTTOM = 15
    PROPIEDAD_PADDING_TOP = 16
    PROPIEDAD_PADDING = 17
    PROPIEDAD_DISPLAY = 18
    PROPIEDAD_LINE_HEIGHT = 19
    PROPIEDAD_WIDTH = 20
    PROPIEDAD_HEIGHT = 21
    PROPIEDAD_MARGIN_TOP = 22
    PROPIEDAD_MARGIN_RIGHT = 23
    PROPIEDAD_MARGIN_BOTTOM = 24
    PROPIEDAD_MARGIN_LEFT = 25
    PROPIEDAD_MARGIN = 26
    PROPIEDAD_BORDER_STYLE = 27
    PROPIEDAD_POSITION = 28
    PROPIEDAD_BOTTOM = 29
    PROPIEDAD_TOP = 30
    PROPIEDAD_RIGHT = 31
    PROPIEDAD_LEFT = 32
    PROPIEDAD_FLOAT = 33
    PROPIEDAD_CLEAR = 34
    PROPIEDAD_MAX_WIDTH = 35
    PROPIEDAD_MIN_WIDTH = 36
    PROPIEDAD_MAX_HEIGHT = 37
    PROPIEDAD_MIN_HEIGHT = 38
    PROPIEDAD_CONTENT = 39
    PROPIEDAD_BORDER_TOP = 40
    RESERVADA_PX = 41
    RESERVADA_EM = 42
    RESERVADA_REM = 43
    RESERVADA_VH = 44
    RESERVADA_VW= 45
    RESERVADA_IN = 46
    RESERVADA_CM = 47
    RESERVADA_MM = 48
    RESERVADA_PT = 49
    RESERVADA_PC = 50
    RESERVADA_RELATIVE = 51
    RESERVADA_INLINE_BLOCK = 52
    RESERVADA_RED = 53
    RESERVADA_RGBA = 54
    RESERVADA_URL = 55
    RESERVADA_CONTENT = 56
    RESERVADA_INHERIT = 57
    RESERVADA_SOLID = 58
    RESERVADA_ABSOLUTE = 59
    RESERVADA_ARIAL = 60
    RESERVADA_SANS_SERIF = 61
    RESERVADA_BLOCK = 62
    IDENTIFICADOR = 63
    NUMERO_ENTERO = 64
    NUMERO_DECIMAL = 65
    COMENTARIO = 66
    CADENA_STRING = 67
    SIGNO_PORCENTAJE = 68
    SIGNO_NUMERAL = 69
    SIGNO_MENOS = 70
    SIGNO_POR = 71
    LLAVE_IZQ = 72
    LLAVE_DER = 73
    PARENTESIS_IZQ = 74
    PARENTESIS_DER = 75
    COMA = 76
    PUNTO_Y_COMA = 77
    DOS_PUNTOS = 78
    PUNTO = 79
    DESCONOCIDO = 80


class Token_Css:
    __tipoToken = Tipo
    __lexema = str
    __filaToken = int
    __columnaToken = int

    def __init__(self, tipo, auxlex, fila, columna):
        self.__tipoToken = tipo
        self.__lexema = auxlex
        self.__filaToken = fila
        self.__columnaToken = columna
    
    def getTipo(self):
        return self.__tipoToken

    def getLexema(self):
        return self.__lexema
    
    def getFila(self):
        return self.__filaToken

    def getColumna(self):
        return self.__columnaToken

    def getTipoEnString(self):
        self.nombreToken = ""

        if self.__tipoToken == Tipo.PROPIEDAD_COLOR:
            self.nombreToken = "Propiedad_Color"
        elif self.__tipoToken == Tipo.PROPIEDAD_BACKGROUND_COLOR:
            self.nombreToken = "Propiedad_Background-Color"
        elif self.__tipoToken == Tipo.PROPIEDAD_BACKGROUND_IMAGE:
            self.nombreToken = "Propiedad_Background-Image"
        elif self.__tipoToken == Tipo.PROPIEDAD_BORDER:
            self.nombreToken = "Propiedad_Border"
        elif self.__tipoToken == Tipo.PROPIEDAD_OPACITY:
            self.nombreToken = "Propiedad_Opacity"
        elif self.__tipoToken == Tipo.PROPIEDAD_BACKGROUND:
            self.nombreToken = "Propiedad_Background"
        elif self.__tipoToken == Tipo.PROPIEDAD_TEXT_ALIGN:
            self.nombreToken = "Propiedad_Text_Align"
        elif self.__tipoToken == Tipo.PROPIEDAD_FONT_FAMILY:
            self.nombreToken = "Propiedad_Font_Family"
        elif self.__tipoToken == Tipo.PROPIEDAD_FONT_STYLE:
            self.nombreToken = "Propiedad_Font_Style"
        elif self.__tipoToken == Tipo.PROPIEDAD_FONT_WEIGHT:
            self.nombreToken = "Propiedad_Font_Weight"
        elif self.__tipoToken == Tipo.PROPIEDAD_FONT_SIZE:
            self.nombreToken = "Propiedad_Font_Size"
        elif self.__tipoToken == Tipo.PROPIEDAD_FONT:
            self.nombreToken = "Propiedad_Font"
        elif self.__tipoToken == Tipo.PROPIEDAD_PADDING_LEFT:
            self.nombreToken = "Propiedad_Padding_Left"
        elif self.__tipoToken == Tipo.PROPIEDAD_PADDING_RIGHT:
            self.nombreToken = "Propiedad_Padding_Right"
        elif self.__tipoToken == Tipo.PROPIEDAD_PADDING_BOTTOM:
            self.nombreToken = "Propiedad_Padding_Bottom"
        elif self.__tipoToken == Tipo.PROPIEDAD_PADDING_TOP:
            self.nombreToken = "Propiedad_Padding_Top"
        elif self.__tipoToken == Tipo.PROPIEDAD_PADDING:
            self.nombreToken = "Propiedad_Padding"
        elif self.__tipoToken == Tipo.PROPIEDAD_DISPLAY:
            self.nombreToken = "Propiedad_Display"
        elif self.__tipoToken == Tipo.PROPIEDAD_LINE_HEIGHT:
            self.nombreToken = "Propiedad_Line_Height"
        elif self.__tipoToken == Tipo.PROPIEDAD_WIDTH:
            self.nombreToken = "Propiedad_Width"
        elif self.__tipoToken == Tipo.PROPIEDAD_HEIGHT:
            self.nombreToken = "Propiedad_Height"
        elif self.__tipoToken == Tipo.PROPIEDAD_MARGIN_TOP:
            self.nombreToken = "Propiedad_Margin_Top"
        elif self.__tipoToken == Tipo.PROPIEDAD_MARGIN_RIGHT:
            self.nombreToken = "Propiedad_Margin_Right"
        elif self.__tipoToken == Tipo.PROPIEDAD_MARGIN_BOTTOM:
            self.nombreToken = "Propiedad_Margin_Bottom"
        elif self.__tipoToken == Tipo.PROPIEDAD_MARGIN_LEFT:
            self.nombreToken = "Propiedad_Margin_Left"
        elif self.__tipoToken == Tipo.PROPIEDAD_MARGIN:
            self.nombreToken = "Propiedad_Margin"
        elif self.__tipoToken == Tipo.PROPIEDAD_BORDER_STYLE:
            self.nombreToken = "Propiedad_Border_Style"
        elif self.__tipoToken == Tipo.PROPIEDAD_POSITION:
            self.nombreToken = "Propiedad_Position"
        elif self.__tipoToken == Tipo.PROPIEDAD_BOTTOM:
            self.nombreToken = "Propiedad_Bottom"
        elif self.__tipoToken == Tipo.PROPIEDAD_TOP:
            self.nombreToken = "Propiedad_Top"
        elif self.__tipoToken == Tipo.PROPIEDAD_RIGHT:
            self.nombreToken = "Propiedad_Right"
        elif self.__tipoToken == Tipo.PROPIEDAD_LEFT:
            self.nombreToken = "Propiedad_Left"
        elif self.__tipoToken == Tipo.PROPIEDAD_FLOAT:
            self.nombreToken = "Propiedad_Float"
        elif self.__tipoToken == Tipo.PROPIEDAD_CLEAR:
            self.nombreToken = "Propiedad_Clear"
        elif self.__tipoToken == Tipo.PROPIEDAD_MAX_WIDTH:
            self.nombreToken = "Propiedad_Max_Width"
        elif self.__tipoToken == Tipo.PROPIEDAD_MIN_WIDTH:
            self.nombreToken = "Propiedad_Min_Width"
        elif self.__tipoToken == Tipo.PROPIEDAD_MAX_HEIGHT:
            self.nombreToken = "Propiedad_Max_Height"
        elif self.__tipoToken == Tipo.PROPIEDAD_MIN_HEIGHT:
            self.nombreToken = "Propiedad_Min_Height"
        elif self.__tipoToken == Tipo.PROPIEDAD_CONTENT:
            self.nombreToken = "Propiedad_Content"
        elif self.__tipoToken == Tipo.PROPIEDAD_BORDER_TOP:
            self.nombreToken = "Propiedad_Border_Top"
        elif self.__tipoToken == Tipo.RESERVADA_PX:
            self.nombreToken = "Reservada_px"
        elif self.__tipoToken == Tipo.RESERVADA_EM:
            self.nombreToken = "Reservada_em"
        elif self.__tipoToken == Tipo.RESERVADA_REM:
            self.nombreToken = "Reservada_rem"
        elif self.__tipoToken == Tipo.RESERVADA_VH:
            self.nombreToken = "Reservada_vh"
        elif self.__tipoToken == Tipo.RESERVADA_VW:
            self.nombreToken = "Reservada_vw"
        elif self.__tipoToken == Tipo.RESERVADA_IN:
            self.nombreToken = "Reservada_in"
        elif self.__tipoToken == Tipo.RESERVADA_CM:
            self.nombreToken = "Reservada_cm"
        elif self.__tipoToken == Tipo.RESERVADA_MM:
            self.nombreToken = "Reservada_mm"
        elif self.__tipoToken == Tipo.RESERVADA_PT:
            self.nombreToken = "Reservada_pt"
        elif self.__tipoToken == Tipo.RESERVADA_PC:
            self.nombreToken = "Reservada_pc"
        elif self.__tipoToken == Tipo.RESERVADA_RELATIVE:
            self.nombreToken = "Reservada_Relative"
        elif self.__tipoToken == Tipo.RESERVADA_INLINE_BLOCK:
            self.nombreToken = "Reservada_Inline_Block"
        elif self.__tipoToken == Tipo.RESERVADA_RED:
            self.nombreToken = "Reservada_Red"
        elif self.__tipoToken == Tipo.RESERVADA_RGBA:
            self.nombreToken = "Reservada_rgba"
        elif self.__tipoToken == Tipo.RESERVADA_URL:
            self.nombreToken = "Reservada_url"
        elif self.__tipoToken == Tipo.RESERVADA_CONTENT:
            self.nombreToken = "Reservada_Content"
        elif self.__tipoToken == Tipo.RESERVADA_INHERIT:
            self.nombreToken = "Reservada_Inherit"
        elif self.__tipoToken == Tipo.RESERVADA_SOLID:
            self.nombreToken = "Reservada_Solid"
        elif self.__tipoToken == Tipo.RESERVADA_ABSOLUTE:
            self.nombreToken = "Reservada_Absolute"
        elif self.__tipoToken == Tipo.RESERVADA_ARIAL:
            self.nombreToken = "Reservada_Arial"
        elif self.__tipoToken == Tipo.RESERVADA_SANS_SERIF:
            self.nombreToken = "Reservada_Sans_Serif"
        elif self.__tipoToken == Tipo.RESERVADA_BLOCK:
            self.nombreToken = "Reservada_Block"
        elif self.__tipoToken == Tipo.IDENTIFICADOR:
            self.nombreToken = "Identificador"
        elif self.__tipoToken == Tipo.NUMERO_ENTERO:
            self.nombreToken = "NumeroEntero"
        elif self.__tipoToken == Tipo.NUMERO_DECIMAL:
            self.nombreToken = "NumeroDecimal"
        elif self.__tipoToken == Tipo.COMENTARIO:
            self.nombreToken = "Comentario"
        elif self.__tipoToken == Tipo.CADENA_STRING:
            self.nombreToken = "Cadena_String"
        elif self.__tipoToken == Tipo.SIGNO_PORCENTAJE:
            self.nombreToken = "Signo_Porcentaje"
        elif self.__tipoToken == Tipo.SIGNO_NUMERAL:
            self.nombreToken = "Signo_Numeral"
        elif self.__tipoToken == Tipo.SIGNO_MENOS:
            self.nombreToken = "Signo_Menos"
        elif self.__tipoToken == Tipo.SIGNO_POR:
            self.nombreToken = "Signo_Por"
        elif self.__tipoToken == Tipo.LLAVE_IZQ:
            self.nombreToken = "Llave_Izq"
        elif self.__tipoToken == Tipo.LLAVE_DER:
            self.nombreToken = "Llave_Der"
        elif self.__tipoToken == Tipo.PARENTESIS_IZQ:
            self.nombreToken = "Parentesis_Izq"
        elif self.__tipoToken == Tipo.PARENTESIS_DER:
            self.nombreToken = "Parentesis_Der"
        elif self.__tipoToken == Tipo.COMA:
            self.nombreToken = "Coma"
        elif self.__tipoToken == Tipo.PUNTO_Y_COMA:
            self.nombreToken = "Punto_Y_Coma"
        elif self.__tipoToken == Tipo.DOS_PUNTOS:
            self.nombreToken = "Dos_Puntos"
        elif self.__tipoToken == Tipo.PUNTO:
            self.nombreToken = "Punto"
        else:
            self.nombreToken = "Desconocido"

        return self.nombreToken