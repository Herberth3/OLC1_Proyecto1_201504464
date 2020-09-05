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

from Analizador_Lexico_Javascript import Analizador_Lexico_Javascript
from Analizador_Lexico_Css import Analizador_Lexico_Css
from Token import Token
from Token_Css import Token_Css

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
        self.itemReporte.add_command(label = "Errores")
        self.itemReporte.add_separator()
        self.itemReporte.add_command(label = "Arbol")

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
        #self.tab_control.tab("current", text = "lol")
        
        self.mensaje = StringVar()
        self.mensaje.set("Bienvenido a tu editor")
        self.monitor = Label(self.wind, textvar = self.mensaje, justify = "right")
        self.monitor.place(x = 0, y = 658)
    
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
        ruta = ""
    
    def abrir(self):
        global ruta
        self.mensaje.set("Abrir fichero")

        ruta = filedialog.askopenfilename(
            initialdir = ".",
            filetypes = (("js files","*.js"),
                ("html files","*.html"),
                ("css files","*.css")
            ),
            title = "Abrir un fichero."
        )

        if ruta != "":
            fichero = open(ruta, "r", encoding="utf-8")
            contenido = fichero.read()
            self.txtEntrada.delete(1.0, "end")
            self.txtEntrada.insert(1.0, contenido)
            fichero.close()
            self.configuracionArchivoActual(ruta)

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
            ("css files","*.css")]
        fichero = filedialog.asksaveasfile(title = "Guardar fichero", mode = "w",
            filetypes = tipoArchivo, defaultextension = tipoArchivo)
        
        if fichero is not None:
            ruta = fichero.name #El atributo name es la ruta completa, si está abierto
            contenido = self.txtEntrada.get(1.0, "end-1c") #recuperamos el texto
            fichero = open(ruta, "w+") #creamos el fichero o abrimos
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
        elif extension == ".css":
            self.btn2.config(state = "normal")
            self.btn1.config(state = "disabled")
            self.btn3.config(state = "disabled")
        elif extension == ".html":
            self.btn3.config(state = "normal")
            self.btn1.config(state = "disabled")
            self.btn2.config(state = "disabled")

    def analizar_Archivo(self):
        contenido = self.txtEntrada.get(1.0, "end-1c")
        if contenido.strip():   #strip() retorna True si hay escritura en la variable contenido
            contenidoConsola = ""
            extension = os.path.splitext(ruta)[1]

            if extension == ".js":
                analizador = Analizador_Lexico_Javascript()
                listaTokens = analizador.analizador_Javascript(contenido)
                self.token = Token
                for self.token in listaTokens:
                    contenidoConsola += "Lexema: " + self.token.getLexema() + "  <----> Tipo: " + self.token.getTipoEnString() + "  <----> Fila: " + str(self.token.getFila()) + "  <----> Columna: " + str(self.token.getColumna()) + "\n"
                    ##print("Lexema: " + self.token.getLexema() + "  <----> Tipo: " + self.token.getTipoEnString() + "  <----> Fila: " + str(self.token.getFila()) + "  <----> Columna: " + str(self.token.getColumna()))
                
            elif extension == ".css":
                analizador = Analizador_Lexico_Css()
                listaTokens = analizador.analizador_Css(contenido)
                self.token = Token_Css
                for self.token in listaTokens:
                    contenidoConsola += "Lexema: " + self.token.getLexema() + "  <----> Tipo: " + self.token.getTipoEnString() + "  <----> Fila: " + str(self.token.getFila()) + "  <----> Columna: " + str(self.token.getColumna()) + "\n"
                    ##print("Lexema: " + self.token.getLexema() + "  <----> Tipo: " + self.token.getTipoEnString() + "  <----> Fila: " + str(self.token.getFila()) + "  <----> Columna: " + str(self.token.getColumna()))
                
            elif extension == ".html":
                print("Estoy en un archivo html")

            
            
            self.txtConsola.config(state = "normal")
            self.txtConsola.delete(1.0, END)
            self.txtConsola.insert(1.0, contenidoConsola)
            self.txtConsola.config(state = "disabled")
            #print(contenidoConsola)
        else:
            messagebox.showinfo("Editor vacio", "Cargue un archivo o ingrese contenido")
            #print("texto vacio!")


if __name__ == "__main__":
    window = Tk()
    application = GUI(window)
    window.mainloop()   # Dispara la interfaz
