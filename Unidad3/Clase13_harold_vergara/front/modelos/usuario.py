import tkinter as tk

class Usuario():
        
    def __init__(self, ventanaPrincipal):
        self.ventanaPrincipal = ventanaPrincipal
        self.id = tk.StringVar(ventanaPrincipal)
        self.marca = tk.StringVar(ventanaPrincipal)
        self.procesador = tk.StringVar(ventanaPrincipal)
        self.memoriaRam = tk.StringVar(ventanaPrincipal)
        self.almacenamiento =tk.StringVar(ventanaPrincipal)

