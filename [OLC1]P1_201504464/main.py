from tkinter import ttk
#from tkinter import *
from tkinter import scrolledtext    #TextArea
from tkinter import Tk
from tkinter import Label
from tkinter import Menu
from tkinter import Button
from tkinter import filedialog
from tkinter import messagebox
from tkinter import Text
from tkinter import StringVar
from tkinter import END
import os
import webbrowser   #Abrir un archivo en el navegador
from PIL import Image

from Analizador_Lexico_Javascript import Analizador_Lexico_Javascript
from Analizador_Lexico_Css import Analizador_Lexico_Css
from Analizador_Lexico_Html import Analizador_Lexico_Html
from Analizador_Lexico_Rmt import Analizador_Lexico_Rmt
from Analizador_Sintactico_Rmt import Analizador_Sintactico_Rmt

from Analizador_Color_Javascript import Analizador_Color_Javascript #Prueba color
from Analizador_Color_Css import Analizador_Color_Css #Prueba color
from Analizador_Color_Html import Analizador_Color_Html #Prueba color
from Analizador_Color_Rmt import Analizador_Color_Rmt #Prueba color
from Token_Color import Token_Color #Prueba color

from Token import Token
from Token_Css import Token_Css
from Token_Html import Token_Html
from Token_Rmt import Token_Rmt
from Token_Rmt import Tipo
from Estado_Rmt import Estado_Rmt
from Estado_Rmt import Estado
from Token_Error import Token_Error

class GUI:

    ruta = ""
    def __init__(self, window):
        global ruta
        ruta = ""
        #Create Window
        self.wind = window
        self.wind.title("Proyecto 1 - ML WEB")
        self.wind.geometry("900x680")
        self.wind.configure(bg = "blue")
        #Label into the windows (tittle)
        self.lb1 = Label(self.wind, text = "ML WEB EDITOR", font = ("Arial Bold", 15))
        self.lb1.place(x = 350, y = 10)

        #Menu bar
        self.menu = Menu(self.wind)
        self.itemArchivo = Menu(self.menu, tearoff = 0)
        self.itemArchivo.add_command(label = "Nuevo", command = self.nuevo)
        self.itemArchivo.add_command(label = "Abrir Archivo", command = self.abrir)
        self.itemArchivo.add_command(label = "Guardar", command = self.guardar)
        self.itemArchivo.add_command(label = "Guardar Como", command = self.guardar_como)
        self.itemArchivo.add_separator()
        self.itemArchivo.add_command(label = "Salir", command = self.wind.quit)

        #Reporte bar
        self.itemReporte = Menu(self.menu, tearoff = 0)
        self.itemReporte.add_command(label = "Reporte Javascript", command = self.generarReporteJavascript)
        self.itemReporte.add_separator()
        self.itemReporte.add_command(label = "Reporte Css", command = self.generarReporteCss)
        self.itemReporte.add_separator()
        self.itemReporte.add_command(label = "Reporte Html", command = self.generarReporteHtml)
        self.itemReporte.add_separator()
        self.itemReporte.add_command(label = "Reporte Rmt", command = self.generarReporteRmt)
        self.itemReporte.add_separator()
        self.itemReporte.add_command(label = "Arbol Identificador", command = self.generarReporteDotID)
        self.itemReporte.add_separator()
        self.itemReporte.add_command(label = "Arbol Dígitos", command = self.generarReporteDotD)
        self.itemReporte.add_separator()
        self.itemReporte.add_command(label = "Arbol Comentario", command = self.generarReporteDotC)
        self.itemReporte.add_separator()

        #Append items to the menu
        self.menu.add_cascade(label = "Archivo", menu = self.itemArchivo)
        self.menu.add_cascade(label = "Reportes", menu = self.itemReporte)
        self.wind.config(menu = self.menu)
        
        #Widget Notebook (Control de pestañas)
        self.tab_control = ttk.Notebook(self.wind)
        self.tab_control.place(x = 50, y = 50)
        self.tab1 = ttk.Frame(self.tab_control)
        #Append TextArea to the Tab
        #self.txtEntrada = scrolledtext.ScrolledText(self.tab1, width = 80, height = 24)
        self.vScroll, self.hScroll = ttk.Scrollbar(self.tab1, orient = "vertical"), ttk.Scrollbar(self.tab1, orient = "horizontal")
        self.vScroll.pack(side = "right", fill = "y")
        self.hScroll.pack(side = "bottom", fill = "x")
        self.txtEntrada = Text(self.tab1, width = 80, height = 22, wrap = "none", yscrollcommand = self.vScroll.set, xscrollcommand = self.hScroll.set)
        #self.txtEntrada.bind('<Button-1>', self.mostrarCoordenadas )
        self.txtEntrada.bind('<KeyRelease>', self.mostrarCoordenadas )
        
        #Packege scrolledtext into tab1
        self.txtEntrada.pack()
        self.vScroll.config(command = self.txtEntrada.yview)
        self.hScroll.config(command = self.txtEntrada.xview)
        self.tab_control.add(self.tab1, text = "Undefined")

        self.lb2 = Label(self.wind, text = "Console:")  #label 
        self.lb2.place(x = 50, y = 465)
        self.txtConsola = scrolledtext.ScrolledText(self.wind, width = 80, height = 10) # textArea consola
        self.txtConsola.place(x = 50, y = 490)
        self.txtConsola.config(state = "disabled")

        self.btn1 = Button(self.wind, text = "Analizar .JS", bg = "black", fg = "white", width = 15, height = 2, command=self.analizar_Archivo)    #btn Analyze
        self.btn1.place(x=750, y = 50)
        self.btn1.config(state = "disabled")
        self.btn2 = Button(self.wind, text = "Analizar .CSS", bg = "black", fg = "white", width = 15, height = 2, command=self.analizar_Archivo)    #btn Analyze
        self.btn2.place(x=750, y = 110)
        self.btn2.config(state = "disabled")
        self.btn3 = Button(self.wind, text = "Analizar .HTML", bg = "black", fg = "white", width = 15, height = 2, command=self.analizar_Archivo)    #btn Analyze
        self.btn3.place(x=750, y = 170)
        self.btn3.config(state = "disabled")
        self.btn4 = Button(self.wind, text = "Analizar .RMT", bg = "black", fg = "white", width = 15, height = 2, command=self.analizar_Archivo)    #btn Analyze
        self.btn4.place(x=750, y = 230)
        self.btn4.config(state = "disabled")
        #self.tab_control.tab("current", text = "lol")
        
        self.mensaje = StringVar()
        self.mensaje.set("Bienvenido a tu editor")
        self.monitor = Label(self.wind, textvar = self.mensaje, justify = "right")
        self.monitor.place(x = 0, y = 658)
        
        self.coordenadas = StringVar()
        self.coordenadas.set("Lineas=1 Columnas=1")
        self.monitorCoo = Label(self.wind, textvar = self.coordenadas, justify = "right")
        self.monitorCoo.place(x = 300, y = 658)
        

        #Iniciando la ventana borra los reportes de errores
        if os.path.exists("ReporteErroresJavascript.html"):
            os.remove("ReporteErroresJavascript.html")
        if os.path.exists("dotID.png"):
            os.remove("dotID.png")
        if os.path.exists("dotID.dot"):
            os.remove("dotID.dot")
        if os.path.exists("dotD.png"):
            os.remove("dotD.png")
        if os.path.exists("dotD.dot"):
            os.remove("dotD.dot")
        if os.path.exists("dotC.png"):
            os.remove("dotC.png")
        if os.path.exists("dotC.dot"):
            os.remove("dotC.dot")
        if os.path.exists("ReporteErroresCss.html"):
            os.remove("ReporteErroresCss.html")
        if os.path.exists("ReporteErroresHtml.html"):
            os.remove("ReporteErroresHtml.html")
        if os.path.exists("ReporteOperacionesRmt.html"):
            os.remove("ReporteOperacionesRmt.html")

    def mostrarCoordenadas(self, event):
        #self.coordenadas['text'] = f'x = {event.x} y = {event.y}'
        #self.coordenadas.set("x=" + str(event.x) + " y=" + str(event.y))
        self.l1 = self.txtEntrada.index('current').split('.')[0]
        self.l2 = self.txtEntrada.index('current').split('.')[1]
        self.coordenadas.set("Lineas=" + self.l1 + " Columnas=" + self.l2)
    
    def nuevo(self):
        global ruta
        self.mensaje.set("Nuevo fichero")
        self.txtEntrada.delete(1.0, END)
        self.txtConsola.config(state = "normal")
        self.txtConsola.delete(1.0, END)
        self.txtConsola.config(state = "disabled")
        self.tab_control.tab("current", text = "Undefined")
        self.btn1.config(state = "disabled")
        self.btn2.config(state = "disabled")
        self.btn3.config(state = "disabled")
        self.btn4.config(state = "disabled")
        ruta = ""
    
    def abrir(self):
        global ruta
        self.mensaje.set("Abrir fichero")

        ruta = filedialog.askopenfilename(
            initialdir = ".",
            filetypes = (("js files","*.js"),
                ("html files","*.html"),
                ("css files","*.css"),
                ("rmt files","*.rmt")
            ),
            title = "Abrir un fichero."
        )
        
        if ruta != "":
            fichero = open(ruta, "r", encoding="utf-8")
            contenido = fichero.read()
            #CONTENIDO ORIGINAL ANTES DE COLOR------------------
            self.txtEntrada.delete(1.0, "end")
            #self.txtEntrada.insert(1.0, contenido)
            #CONTENIDO ORIGINAL ANTES DE COLOR------------------
            

            #CONTENIDO DURANTE COLOR------------------
            extension = os.path.splitext(ruta)[1]
            if extension == ".js":
                analizadorColor = Analizador_Color_Javascript()
                listaT = analizadorColor.analizador_J(contenido)
            elif extension == ".css":
                analizadorColor = Analizador_Color_Css()
                listaT = analizadorColor.analizador_C(contenido)
            elif extension == ".html":
                analizadorColor = Analizador_Color_Html()
                listaT = analizadorColor.analizador_H(contenido)
            elif extension == ".rmt":
                analizadorColor = Analizador_Color_Rmt()
                listaT = analizadorColor.analizador_R(contenido)
            
            self.setColorText(listaT)
            #CONTENIDO DURANTE COLOR------------------

            fichero.close()
            self.txtConsola.config(state = "normal")
            self.txtConsola.delete(1.0, END)
            self.txtConsola.config(state = "disabled")
            self.configuracionArchivoActual(ruta)
            extension = os.path.splitext(ruta)[1]
            if os.path.exists("ReporteErroresJavascript.html") and extension == ".js":
                os.remove("ReporteErroresJavascript.html")
            if os.path.exists("dotID.png") and extension == ".js":
                os.remove("dotID.png")
            if os.path.exists("dotID.dot") and extension == ".js":
                os.remove("dotID.dot")
            if os.path.exists("dotD.png") and extension == ".js":
                os.remove("dotD.png")
            if os.path.exists("dotD.dot") and extension == ".js":
                os.remove("dotD.dot")
            if os.path.exists("dotC.png") and extension == ".js":
                os.remove("dotC.png")
            if os.path.exists("dotC.dot") and extension == ".js":
                os.remove("dotC.dot")
            if os.path.exists("ReporteErroresCss.html") and extension == ".css":
                os.remove("ReporteErroresCss.html")
            if os.path.exists("ReporteErroresHtml.html") and extension == ".html":
                os.remove("ReporteErroresHtml.html")
            if os.path.exists("ReporteOperacionesRmt.html") and extension == ".rmt":
                os.remove("ReporteOperacionesRmt.html")

    def guardar(self):
        global ruta
        self.mensaje.set("Guardar fichero")

        if ruta != "":
            contenido = self.txtEntrada.get(1.0, "end-1c") #recuperamos el texto -1 char
            fichero = open(ruta, "w+", encoding="utf-8")
            fichero.write(contenido)
            fichero.close()
            self.configuracionArchivoActual(ruta)
            self.mensaje.set("Fichero guardado correctamente")
        else:
            self.guardar_como()
    
    def guardar_como(self):
        global ruta
        self.mensaje.set("Guardar fichero como")

        tipoArchivo = [("js files","*.js"),
            ("html files","*.html"),
            ("css files","*.css"),
            ("rmt files","*.rmt")]
        fichero = filedialog.asksaveasfile(title = "Guardar fichero", mode = "w",
            filetypes = tipoArchivo, defaultextension = tipoArchivo)
        
        if fichero is not None:
            ruta = fichero.name #El atributo name es la ruta completa, si está abierto
            contenido = self.txtEntrada.get(1.0, "end-1c") #recuperamos el texto
            fichero = open(ruta, "w+", encoding="utf-8") #creamos el fichero o abrimos
            fichero.write(contenido)
            fichero.close()
            self.configuracionArchivoActual(ruta)
            self.mensaje.set("Fichero guardado correctamente")
        else:
            self.mensaje.set("Guardado cancelado")
            ruta = ""

    def configuracionArchivoActual(self, ruta):
        extension = os.path.splitext(ruta)[1]
        nombreArchivo = os.path.split(ruta)[1]
        self.tab_control.tab("current", text = nombreArchivo)
        self.habilitarBotonAnalizar(extension)

    def habilitarBotonAnalizar(self, extension):
        if extension == ".js":
            self.btn1.config(state = "normal")
            self.btn2.config(state = "disabled")
            self.btn3.config(state = "disabled")
            self.btn4.config(state = "disabled")
        elif extension == ".css":
            self.btn2.config(state = "normal")
            self.btn1.config(state = "disabled")
            self.btn3.config(state = "disabled")
            self.btn4.config(state = "disabled")
        elif extension == ".html":
            self.btn3.config(state = "normal")
            self.btn1.config(state = "disabled")
            self.btn2.config(state = "disabled")
            self.btn4.config(state = "disabled")
        elif extension == ".rmt":
            self.btn4.config(state = "normal")
            self.btn1.config(state = "disabled")
            self.btn2.config(state = "disabled")
            self.btn3.config(state = "disabled")

    def analizar_Archivo(self):
        contenido = self.txtEntrada.get(1.0, "end-1c")
        if contenido.strip():   #strip() retorna True si hay escritura en la variable contenido
            contenidoConsola = ""
            extension = os.path.splitext(ruta)[1]
            nuevoContenido = ""
            self.reporteErrorActual = ""
            self.listaOperacionesAnalizadas = list()    #Lista de las operaciones ya parseadas en archivos .rmt
            self.estadoOperacion = Estado   #Estado de la operación parseada en archivos .rmt

            if extension == ".js":
                self.analizador = Analizador_Lexico_Javascript()
                listaTokens = self.analizador.analizador_Javascript(contenido)
                nuevoContenido = self.analizador.getRecolectorND()
                self.reporteErrorActual = "ReporteErroresJavascript.html"
                if os.path.exists("dotID.png"):
                    os.remove("dotID.png")
                if os.path.exists("dotID.dot"):
                    os.remove("dotID.dot")
                if os.path.exists("dotD.png"):
                    os.remove("dotD.png")
                if os.path.exists("dotD.dot"):
                    os.remove("dotD.dot")
                if os.path.exists("dotC.png"):
                    os.remove("dotC.png")
                if os.path.exists("dotC.dot"):
                    os.remove("dotC.dot")

                self.generarPNG_Dot()
                self.generarReporteDotID()
                self.generarReporteDotD()
                self.generarReporteDotC()
                #self.token = Token
                #for self.token in listaTokens:
                    #contenidoConsola += "Lexema: " + self.token.getLexema() + "  <----> Tipo: " + self.token.getTipoEnString() + "  <----> Fila: " + str(self.token.getFila()) + "  <----> Columna: " + str(self.token.getColumna()) + "\n"
                    ##print("Lexema: " + self.token.getLexema() + "  <----> Tipo: " + self.token.getTipoEnString() + "  <----> Fila: " + str(self.token.getFila()) + "  <----> Columna: " + str(self.token.getColumna()))
                
            elif extension == ".css":
                self.analizador = Analizador_Lexico_Css()
                listaTokens = self.analizador.analizador_Css(contenido)
                nuevoContenido = self.analizador.getRecolectorND()
                self.reporteErrorActual = "ReporteErroresCss.html"
                
            elif extension == ".html":
                self.analizador = Analizador_Lexico_Html()
                listaTokens = self.analizador.analizador_Html(contenido)
                nuevoContenido = self.analizador.getRecolectorND()
                self.reporteErrorActual = "ReporteErroresHtml.html"

            elif extension == ".rmt":
                self.analizador = Analizador_Lexico_Rmt()
                parser = Analizador_Sintactico_Rmt()

                self.operaciones = contenido.split("\n")
                for o in self.operaciones:
                    listaTokens = self.analizador.analizador_Rmt(o)
                    nuevoToken = Token_Rmt(Tipo.DESCONOCIDO, "")
                    listaTokens.append(nuevoToken)

                    parser.parsear(listaTokens)
                    self.estadoOperacion = parser.getEstadoOperacion()
                    nuevaOperacion = Estado_Rmt(self.estadoOperacion, o)
                    self.listaOperacionesAnalizadas.append(nuevaOperacion)
                self.reporteOperaciones = "ReporteOperacionesRmt.html"
                self.generarHTML_Operaciones(self.listaOperacionesAnalizadas)
                webbrowser.open_new_tab(self.reporteOperaciones)
                #self.estado = Estado_Rmt
                #for self.estado in self.listaOperacionesAnalizadas:
                    #contenidoConsola += "Lexema: " + self.token.getLexema() + "  <----> Tipo: " + self.token.getTipoEnString() + "\n"
                    #print("Operación: " + self.estado.getOperacion() + "  <----> Estado: " + self.estado.getEstadoEnString())

            listaErrores = self.analizador.analizador_Error()
            if len(listaErrores) > 0:
                self.guardarND(listaTokens, extension, nuevoContenido)
                contenidoConsola = self.analizador.imprimirListaErrores()
                self.generarHTML_Errores(listaErrores, extension)
                webbrowser.open_new_tab(self.reporteErrorActual) #Abre un archivo en un nuevo tab del navegador

            self.txtConsola.config(state = "normal")
            self.txtConsola.delete(1.0, END)
            self.txtConsola.insert(1.0, contenidoConsola)
            self.txtConsola.config(state = "disabled")
        else:
            messagebox.showinfo("Editor vacio", "Cargue un archivo o ingrese contenido")

    def guardarND(self, listaT, ext, contenido):
        self.listT = listaT
        self.ext = ext
        self.cont = contenido
        nombreArchivo = os.path.split(ruta)[1]
        
        try:
            if self.ext == ".js":
                self.token = Token
                self.token = self.listT[0]
                self.path = str(self.token.getLexema()).replace("//PATHW:", "")
                self.path += nombreArchivo
            elif self.ext == ".css":
                self.token = Token_Css
                self.token = self.listT[0]
                self.path = str(self.token.getLexema()).lstrip("/*PATHW:")
                self.path = self.path.rstrip("*/")
                self.path += "/" + nombreArchivo
            elif self.ext == ".html":
                self.token = Token_Html
                self.token = self.listT[0]
                self.path = str(self.token.getLexema()).lstrip("<!-PATHW:")
                self.path = self.path.rstrip("->")
                self.path += nombreArchivo
        
            fichero = open(self.path, "w+", encoding="utf-8")
            fichero.write(self.cont)
            fichero.close()
            self.mensaje.set("Nuevo fichero generado existosamente")
        except:
            messagebox.showerror("Alerta", "No hay ruta para el nuevo documento sin errores")

    def generarHTML_Errores(self, listaE, ext):
        self.listE = listaE
        self.ext = ext
        self.tokenError = Token_Error
        indiceLista = 1
        nombreArchivoActual = os.path.split(ruta)[1]
        tipoReporte = ""

        if self.ext == ".js":
            tipoReporte = "ReporteErroresJavascript.html"
        elif self.ext == ".css":
            tipoReporte = "ReporteErroresCss.html"
        elif self.ext == ".html":
            tipoReporte = "ReporteErroresHtml.html"

        #----Begin creation html----
        html = open(tipoReporte, 'w')
        html.write('<html>\n')
        html.write('    <title>\n')
        html.write('    </title>\n')
        html.write('            <body>\n')
        html.write('                <center>\n')
        html.write('                    <h1>Tabla de Errores</h1>\n')
        html.write('                    <h5>Nombre Archivo Origen: ' + nombreArchivoActual + '</h5>\n')
        html.write('                    <table border=\" 2px \">\n')
        html.write('                        <tr>\n')
        html.write('                            <td><h3>No.</h3></td>\n')
        html.write('                            <td><h3>Caracter</h3></td>\n')
        html.write('                            <td><h3>Tipo de Error</h2></td>\n')
        html.write('                            <td><h3>Descripción</h2></td>\n')
        html.write('                            <td><h3>Fila</h3></td>\n')
        html.write('                            <td><h3>Columna</h3></td>\n')
        html.write('                        </tr>\n')
        html.write('                        <tr>\n')
        for self.tokenError in self.listE:
            html.write('                            <td>' + str(indiceLista) + '</td>\n')
            html.write('                            <td>' + self.tokenError.getCaracterError() + '</td>\n')
            html.write('                            <td>' + self.tokenError.getTipoErrorEnString() + '</td>\n')
            html.write('                            <td>' + self.tokenError.getDescripcionError() + '</td>\n')
            html.write('                            <td>' + str(self.tokenError.getFilaError()) + '</td>\n')
            html.write('                            <td>' + str(self.tokenError.getColumnaError()) + '</td>\n')
            html.write('                        </tr>\n')
            indiceLista += 1
        html.write('                    </table>\n')
        html.write('                </center>\n')
        html.write('            </body>\n')
        html.write('</html>')
        html.close()
        #----End creation html----
        messagebox.showinfo("Reporte de errores", "Reporte de Errores Creado")

    def generarHTML_Operaciones(self, listaO):
        self.listO = listaO
        self.estado = Estado_Rmt
        indiceLista = 1
        nombreArchivoActual = os.path.split(ruta)[1]

        #----Begin creation html----
        html = open('ReporteOperacionesRmt.html', 'w')
        html.write('<html>\n')
        html.write('    <title>\n')
        html.write('    </title>\n')
        html.write('            <body>\n')
        html.write('                <center>\n')
        html.write('                    <h1>Tabla de validez para operaciones</h1>\n')
        html.write('                    <h5>Nombre Archivo Origen: ' + nombreArchivoActual + '</h5>\n')
        html.write('                    <table border=\" 2px \">\n')
        html.write('                        <tr>\n')
        html.write('                            <td><h3>No.</h3></td>\n')
        html.write('                            <td><h3>Operación</h3></td>\n')
        html.write('                            <td><h3>Análisis</h2></td>\n')
        html.write('                        </tr>\n')
        html.write('                        <tr>\n')
        for self.estado in self.listO:
            html.write('                            <td>' + str(indiceLista) + '</td>\n')
            html.write('                            <td>' + self.estado.getOperacion() + '</td>\n')
            html.write('                            <td>' + self.estado.getEstadoEnString() + '</td>\n')
            html.write('                        </tr>\n')
            indiceLista += 1
        html.write('                    </table>\n')
        html.write('                </center>\n')
        html.write('            </body>\n')
        html.write('</html>')
        html.close()
        #----End creation html----
        messagebox.showinfo("Reporte de operaciones", "Reporte de Operaciones Creado")

    def generarPNG_Dot(self):
        self.dot = self.analizador.getDotID()
        if not self.dot == "":
            dot = open("dotID.dot", "w")
            dot.write(self.dot)
            dot.close()
            os.system('dot -Tpng dotID.dot -o dotID.png')

        self.dot = self.analizador.getDotD()
        if not self.dot == "":
            dot = open("dotD.dot", "w")
            dot.write(self.dot)
            dot.close()
            os.system('dot -Tpng dotD.dot -o dotD.png')

        self.dot = self.analizador.getDotC()
        if not self.dot == "":
            dot = open("dotC.dot", "w")
            dot.write(self.dot)
            dot.close()
            os.system('dot -Tpng dotC.dot -o dotC.png')

    def generarReporteJavascript(self):
        if os.path.exists("ReporteErroresJavascript.html"):
            webbrowser.open_new_tab("ReporteErroresJavascript.html")
        else:
            messagebox.showerror("Estado Reporte", "No se encontro el reporte\nGenere uno, analizando un archivo con errores.")

    def generarReporteCss(self):
        if os.path.exists("ReporteErroresCss.html"):
            webbrowser.open_new_tab("ReporteErroresCss.html")
        else:
            messagebox.showerror("Estado Reporte", "No se encontro el reporte\nGenere uno, analizando un archivo con errores.")

    def generarReporteHtml(self):
        if os.path.exists("ReporteErroresHtml.html"):
            webbrowser.open_new_tab("ReporteErroresHtml.html")
        else:
            messagebox.showerror("Estado Reporte", "No se encontro el reporte\nGenere uno, analizando un archivo con errores.")

    def generarReporteRmt(self):
        if os.path.exists("ReporteOperacionesRmt.html"):
            webbrowser.open_new_tab("ReporteOperacionesRmt.html")
        else:
            messagebox.showerror("Estado Reporte", "No se encontro el reporte\nGenere uno, analizando un archivo.")
    
    def generarReporteDotID(self):
        if os.path.exists("dotID.png"):
            o = Image.open("dotID.png")
            o.show()
        else:
            messagebox.showerror("Estado Reporte", "No se encontro el reporte Árbol Identificador\nGenere uno, analizando un archivo.")

    def generarReporteDotD(self):
        if os.path.exists("dotD.png"):
            o = Image.open("dotD.png")
            o.show()
        else:
            messagebox.showerror("Estado Reporte", "No se encontro el reporte Árbol Digitos\nGenere uno, analizando un archivo.")

    def generarReporteDotC(self):
        if os.path.exists("dotC.png"):
            o = Image.open("dotC.png")
            o.show()
        else:
            messagebox.showerror("Estado Reporte", "No se encontro el reporte Árbol Comentario\nGenere uno, analizando un archivo.")

    #CONTENIDO DURANTE COLOR------------------
    def setColorText(self, listaT):
        t = Token_Color
        for t in listaT:
            if t.getTipoEnString() == "Reservada":
                reservada = t.getLexema()
                self.txtEntrada.insert(END, reservada , 'reservada')
            elif t.getTipoEnString() == "Variable":
                variable = t.getLexema()
                self.txtEntrada.insert(END, variable , 'variable')
            elif t.getTipoEnString() == "Numero":
                numero = t.getLexema()
                self.txtEntrada.insert(END, numero , 'numero')
            elif t.getTipoEnString() == "Comentario":
                comentario = t.getLexema()
                self.txtEntrada.insert(END, comentario , 'comentario')
            elif t.getTipoEnString() == "Cadena":
                cadena = t.getLexema()
                self.txtEntrada.insert(END, cadena , 'cadena')
            elif t.getTipoEnString() == "Boolean":
                boolean = t.getLexema()
                self.txtEntrada.insert(END, boolean , 'boolean')
            elif t.getTipoEnString() == "Operador":
                operador = t.getLexema()
                self.txtEntrada.insert(END, operador , 'operador')
            else:
                cualquiera = t.getLexema()
                self.txtEntrada.insert(END, cualquiera)

        self.txtEntrada.tag_config('reservada', foreground = "red")
        self.txtEntrada.tag_config('variable', foreground = "green")
        self.txtEntrada.tag_config('numero', foreground = "blue")
        self.txtEntrada.tag_config('comentario', foreground = "gray")
        self.txtEntrada.tag_config('cadena', foreground = "yellow")
        self.txtEntrada.tag_config('boolean', foreground = "blue")
        self.txtEntrada.tag_config('operador', foreground = "orange")
                

    #CONTENIDO DURANTE COLOR------------------


if __name__ == "__main__":
    window = Tk()
    application = GUI(window)
    window.mainloop()   # Dispara la interfaz
