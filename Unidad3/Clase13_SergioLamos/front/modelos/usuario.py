import tkinter as tk

class Usuario():
        
    def __init__(self, ventanaPrincipal):
        self.ventanaPrincipal = ventanaPrincipal
        self.id = tk.StringVar(ventanaPrincipal)
        self.marca = tk.StringVar(ventanaPrincipal)
        self.velocidad = tk.StringVar(ventanaPrincipal)
        self.placa = tk.StringVar(ventanaPrincipal)
        self.color =tk.StringVar(ventanaPrincipal)