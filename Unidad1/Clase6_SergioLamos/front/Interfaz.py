import tkinter as tk
from tkinter import messagebox
import re


import requests

response = requests.get("http://localhost:8000")
#print(response.content)

# Configuración de la ventana
ventana = tk.Tk()
ventana.geometry("400x400+200+100")
ventana.resizable(0, 0)
ventana.config(cursor="pirate")
ventana.config(relief="sunken") 
ventana.config(bd=4) 
ventana.title("Interfaz Simple")
ventana.configure(bg="gray")

# Funciones de validación
def validar_marca(event=None):
    texto_ingresado = marca.get()
    if re.match("^[A-Za-z0-9 ]+$", texto_ingresado):
        marca_error.config(text="")
    else:
        marca_error.config(text="¡No se permiten caracteres especiales!")

def validar_velocidad(event=None):
    texto_ingresado = velocidad.get()
    if re.match("^[0-9.]+$", texto_ingresado):
        velocidad_error.config(text="")
    else:
        velocidad_error.config(text="¡Solo se permiten números!")

def validar_placa(event=None):
    texto_ingresado = placa.get()
    if re.match("^[A-Za-z0-9 ]+$", texto_ingresado):
        placa_error.config(text="")
    else:
        placa_error.config(text="¡Solo se permiten letras y números!")

def validar_color(event=None):
    texto_ingresado = color.get()
    if re.match("^[A-Za-z ]+$", texto_ingresado):
        color_error.config(text="")
    else:
        color_error.config(text="¡Solo se permiten letras!")

# Función de validación global
def validar_informacion():
    marca_valida = re.match("^[A-Za-z0-9 ]+$", marca.get())
    velocidad_valida = re.match("^[0-9.]+$", velocidad.get())
    placa_valida = re.match("^[A-Za-z0-9 ]+$", placa.get())
    color_valido = re.match("^[A-Za-z ]+$", color.get())

    if marca_valida and velocidad_valida and placa_valida and color_valido:
        messagebox.showinfo("Validación Exitosa", "Todos los campos han sido completados correctamente.")

        data = {
            "marca": marca.get(),  
            "velocidad": velocidad.get(),  
            "placa": placa.get(),  
            "color": color.get()  
        }

        response = requests.post("http://127.0.0.1:8000/v1/auto",data)
        print(response.status_code)
        print(response.content)



    else:
        messagebox.showwarning("Advertencia", "Por favor completa todos los campos correctamente.")

# Variables
marca = tk.StringVar()
velocidad = tk.StringVar()
placa = tk.StringVar()
color = tk.StringVar()

# Configuración del título
titulo = tk.Label(ventana, text="Llenar Formulario de las cualidades del carro", font=("Arial", 14), bg="gray")
titulo.grid(columnspan=2, pady=10)

# Configuración de las cajas de texto y las etiquetas de error
label1 = tk.Label(ventana, text="Marca:")
label1.grid(column=0, row=1, padx=30, pady=20)
t1 = tk.Entry(ventana, width=24, textvariable=marca)
t1.grid(column=1, row=1, padx=30, pady=5)
marca_error = tk.Label(ventana, text="", fg="red", bg="gray")
marca_error.place(x=140, y=90)

label2 = tk.Label(ventana, text="Velocidad:")
label2.grid(column=0, row=2, padx=30, pady=20)
t2 = tk.Entry(ventana, width=24, textvariable=velocidad)
t2.grid(column=1, row=2, padx=30, pady=5)
velocidad_error = tk.Label(ventana, text="", fg="red", bg="gray")
velocidad_error.place(x=140, y=150)

label3 = tk.Label(ventana, text="Placa:")
label3.grid(column=0, row=3, padx=30, pady=20)
t3 = tk.Entry(ventana, width=24, textvariable=placa)
t3.grid(column=1, row=3, padx=30, pady=5)
placa_error = tk.Label(ventana, text="", fg="red", bg="gray")
placa_error.place(x=140, y=210)

label4 = tk.Label(ventana, text="Color:")
label4.grid(column=0, row=4, padx=30, pady=20)
t4 = tk.Entry(ventana, width=24, textvariable=color)
t4.grid(column=1, row=4, padx=30, pady=5)
color_error = tk.Label(ventana, text="", fg="red", bg="gray")
color_error.place(x=140, y=270)

# Crear un botón para validar la información
boton_validar = tk.Button(ventana, text="Validar", command=validar_informacion)
boton_validar.grid(row=6, column=1, pady=10)

# Enlace de las cajas de texto con los eventos del teclado
t1.bind("<KeyRelease>", validar_marca)
t2.bind("<KeyRelease>", validar_velocidad)
t3.bind("<KeyRelease>", validar_placa)
t4.bind("<KeyRelease>", validar_color)

# Lanzar la ventana
ventana.mainloop()