import tkinter as tk
from tkinter import messagebox
from controllers.controlador import Controlador

class Vista:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.geometry("250x300+200+100")
        self.ventana.title("Interfaz Simple")
        self.ventana.resizable(0, 0)
        self.ventana.configure(bg="gray")
        
        self.controlador = Controlador()
        
        # Configuración de las entradas y etiquetas
        self.setup_entrada("marca", self.validar_caracteres_marca)
        self.setup_entrada("velocidad", self.validar_caracteres_velocidad)
        self.setup_entrada("placa", self.validar_caracteres_placa)
        self.setup_entrada("color", self.validar_caracteres_color)

        # Botón de validación
        self.button_validar = tk.Button(self.ventana, text="Validar", command=self.validar_datos)
        self.button_validar.pack()

    def setup_entrada(self, campo, validation_method):
        label = tk.Label(self.ventana, text=f"{campo.capitalize()}:")
        label.pack()
        entry = tk.Entry(self.ventana)
        entry.pack()
        label_error = tk.Label(self.ventana, text="", fg="red",bg="gray")
        label_error.pack()
        entry.bind("<KeyRelease>", validation_method)
        setattr(self, f"entry_{campo}", entry)
        setattr(self, f"label_error_{campo}", label_error)

    def validar_datos(self):
        marca = self.entry_marca.get()
        velocidad = self.entry_velocidad.get()
        placa = self.entry_placa.get()
        color = self.entry_color.get()

        resultado = self.controlador.validar_datos(marca, velocidad, placa, color)
        if resultado:
            messagebox.showinfo("Validación", "La información es válida.")
            resultado1 = self.controlador.enviar_datos(marca,velocidad,placa,color)
            resultado1
        else:
            messagebox.showerror("Validación", "La información no es válida.")

    def validar_caracteres_marca(self, event):
        self.validar_caracteres_generico(self.entry_marca, self.label_error_marca)

    def validar_caracteres_velocidad(self, event):
        self.validar_caracteres_generico(self.entry_velocidad, self.label_error_velocidad)

    def validar_caracteres_placa(self, event):
        self.validar_caracteres_generico(self.entry_placa, self.label_error_placa)

    def validar_caracteres_color(self, event):
        self.validar_caracteres_generico(self.entry_color, self.label_error_color)

    def validar_caracteres_generico(self, widget, label_error):
        texto = widget.get()
        if not self.controlador.validar_caracteres(texto):
            label_error.config(text="Solo caracteres válidos")
        else:
            label_error.config(text="")
