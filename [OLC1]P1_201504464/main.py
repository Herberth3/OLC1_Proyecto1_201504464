from tkinter import ttk
from tkinter import *

class GUI:

    def __init__(self, window):
        self.wind = window
        self.wind.title("Proyecto 1")

if __name__ == "__main__":
    window = Tk()
    application = GUI(window)
    window.mainloop()
