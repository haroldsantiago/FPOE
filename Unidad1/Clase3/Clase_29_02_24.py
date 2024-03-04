import tkinter as tk
from tkcalendar import DateEntry
from datetime import datetime
import re
from tkinter import messagebox

# Configuración de la ventana
ventana = tk.Tk()
ventana.geometry("500x500+200+100")
ventana.resizable(0, 0)
ventana.config(cursor="pirate")
ventana.config(relief="sunken") 
ventana.config(bd=4) 
ventana.title("Interfaz Simple")
ventana.configure(bg="gray")

def validar_nombre(evento):
    texto_ingresado = nom.get()
    if re.match("^[A-Za-z ]+$", texto_ingresado):
        nombre_error.config(text="")
    else:
        nombre_error.config(text="¡No se permiten números ni caracteres especiales!")

def validar_apellido(evento):
    texto_ingresado = apel_1.get()
    if re.match("^[A-Za-z ]+$", texto_ingresado):
        apellido_error.config(text="")
    else:
        apellido_error.config(text="¡No se permiten números ni caracteres especiales!")

# Función validar Edad
def validar_edad(evento):
    texto_ingresado = edad.get()
    if texto_ingresado.isdigit():
        edad_error.config(text="")
    else:
        edad_error.config(text="¡No se permiten letras ni caracteres especiales!")

# Función validar Correo
def validar_correo(evento):
    texto_ingresado = correo.get()
    if re.match("^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", texto_ingresado):
        correo_error.config(text="")
    else:
        correo_error.config(text="¡El correo electrónico ingresado no es válido!")

# Función validar Fecha Nacimiento
def validar_fecha(evento):
    fecha_seleccionada = fecha.get()
    fecha_actual = datetime.now().strftime('%d/%m/%Y')
    if fecha_seleccionada > fecha_actual:
        fecha_error.config(text="¡La fecha de nacimiento no puede ser posterior a la fecha actual!")
    else:
        fecha_error.config(text="")

#Funcion del boton validar
def validar_informacion():
    nombre_valido = re.match("^[A-Za-z ]+$", nom.get())
    apellido_valido = re.match("^[A-Za-z ]+$", apel_1.get())
    correo_valido = re.match("^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", correo.get())
    fecha_valida = fecha_error.cget("text") == ""

    if nombre_valido and apellido_valido and correo_valido and fecha_valida:
        tk.messagebox.showinfo("Validación Exitosa", "Todos los campos han sido completados correctamente.")
    else:
        tk.messagebox.showwarning("Advertencia", "Por favor completa todos los campos correctamente.")

# Variables
fecha = tk.StringVar()
apel_1 = tk.StringVar()
nom = tk.StringVar()
correo = tk.StringVar()
edad = tk.StringVar()

# Configuración del título
titulo = tk.Label(ventana, text="Llenar Formulario", font=("Arial", 14), bg="gray")
titulo.grid(columnspan=2, pady=10)

# Configuración de las cajas de texto y las etiquetas de error
label1 = tk.Label(ventana, text="Nombre completo:").grid(column=0, row=1, padx=30, pady=20)
t1 = tk.Entry(ventana, width=24, textvariable=nom)
t1.grid(column=1, row=1, padx=30, pady=5)
nombre_error = tk.Label(ventana, text="", fg="red", bg="gray")
nombre_error.place(x=160, y=90)

label2 = tk.Label(ventana, text="Apellidos:").grid(column=0, row=2, padx=30, pady=20)
t2 = tk.Entry(ventana, width=24, textvariable=apel_1)
t2.grid(column=1, row=2, padx=30, pady=5)
apellido_error = tk.Label(ventana, text="", fg="red", bg="gray")
apellido_error.place(x=160, y=150)

label3 = tk.Label(ventana, text="Correo:").grid(column=0, row=3, padx=30, pady=20)
t3 = tk.Entry(ventana, width=24, textvariable=correo)
t3.grid(column=1, row=3, padx=30, pady=5)
correo_error = tk.Label(ventana, text="", fg="red", bg="gray")
correo_error.place(x=140, y=210)

label4 = tk.Label(ventana, text="Edad:").grid(column=0, row=4, padx=30, pady=20)
t4 = tk.Entry(ventana, width=24, textvariable=edad)
t4.grid(column=1, row=4, padx=30, pady=5)
edad_error = tk.Label(ventana, text="", fg="red", bg="gray")
edad_error.place(x=180, y=270)

label6 = tk.Label(ventana, text="Fecha de nacimiento:").grid(column=0, row=5, padx=30, pady=20)
t6 = tk.Entry(ventana, width=24, textvariable=fecha)
t6.grid(column=1, row=5, padx=30, pady=5)
fecha_error = tk.Label(ventana, text="", fg="red", bg="gray")
fecha_error.place(x=140, y=340)


# Crear un botón para validar la información
boton_validar = tk.Button(ventana, text="Validar Información", command=validar_informacion)
boton_validar.grid(row=6, column=1, pady=10)


# Enlace de las cajas de texto con los eventos del teclado
t1.bind("<KeyRelease>", validar_nombre)
t2.bind("<KeyRelease>", validar_apellido)
t3.bind("<KeyRelease>", validar_correo)
t4.bind("<KeyRelease>", validar_edad)
t6.bind("<KeyRelease>", validar_fecha)

ventana.mainloop()
