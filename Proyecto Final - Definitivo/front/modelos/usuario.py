import tkinter as tk

class Usuario():
        
    def __init__(self, ventanaPrincipal):
        self.ventanaPrincipal = ventanaPrincipal

        #Crear Usuario
        self.id = tk.StringVar(ventanaPrincipal)
        self.nombre = tk.StringVar(ventanaPrincipal)
        self.apellido = tk.StringVar(ventanaPrincipal)
        self.cedula = tk.StringVar(ventanaPrincipal)
        self.telefono =tk.StringVar(ventanaPrincipal)
        self.correo= tk.StringVar(ventanaPrincipal)

        #Crear Servicio
        self.nombre_servicio = tk.StringVar(ventanaPrincipal)
        self.cedula_servicio = tk.StringVar(ventanaPrincipal)
        self.descripcion_servicio = tk.StringVar(ventanaPrincipal)
        self.valor_servicio = tk.StringVar(ventanaPrincipal)

