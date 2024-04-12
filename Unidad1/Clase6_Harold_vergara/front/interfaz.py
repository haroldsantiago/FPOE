import tkinter as tk
from datetime import datetime
import re
from tkinter import messagebox


import requests

response = requests.get("http://127.0.0.1:8000/")
#print(response.content)


ventana = tk.Tk()
ventana.geometry("500x500+200+100")
ventana.resizable(0, 0)
ventana.config(cursor="pirate")
ventana.config(relief="sunken") 
ventana.config(bd=4) 
ventana.title("Interfaz Simple")
ventana.configure(bg="gray")

def validar_marca(evento):
    texto_ingresado = marca.get()
    if re.match("^[A-Za-z0-9 ]+$", texto_ingresado):
        marca_error.config(text="")
    else:
        marca_error.config(text="¡No se permiten caracteres especiales!")

def validar_procesador(evento):
    texto_ingresado = procesador.get()
    if re.match("^[A-Za-z0-9 ]+$", texto_ingresado):
        procesador_error.config(text="")
    else:
        procesador_error.config(text="¡No permiten caracteres especiales!")

def validar_almacenamiento(evento):
    texto_ingresado = almacenamiento.get()
    if re.match("^[0-9a-zA-Z ]+$", texto_ingresado):
        almacenamiento_error.config(text="")
    else:
        almacenamiento_error.config(text="¡No se permiten caracteres especiales!")

def validar_ram(evento):
    texto_ingresado = ram.get()
    if re.match("^[0-9a-zA-Z ]+$", texto_ingresado):
        ram_error.config(text="")
    else:
        ram_error.config(text="¡No se permiten letras ni caracteres especiales!")


def validar_informacion():
    marca_eval = re.match("^[A-Za-z0-9 ]+$", marca.get())
    procesador_eval = re.match("^[A-Za-z0-9 ]+$", procesador.get())
    ram_eval = re.match("^[0-9a-zA-Z ]+$", ram.get())
    almacenamiento_eval = re.match("^[0-9a-zA-Z ]+$", almacenamiento.get())

    if marca_eval and procesador_eval and ram_eval and almacenamiento_eval:
        messagebox.showinfo("Validación Exitosa", "Todos los campos han sido completados correctamente.")

        data = {
            "marca": marca.get(),
            "procesador": procesador.get() ,
            "almacenamiento":  almacenamiento.get(),
            "memoriaRam": ram.get()
        }
        response=requests.post("http://127.0.0.1:8000/v1/computador", data)
        print(response.status_code)
        print(response.content)

    else:
        messagebox.showwarning("Advertencia", "Por favor completa todos los campos correctamente.")

marca = tk.StringVar()
procesador = tk.StringVar()
ram = tk.StringVar()
almacenamiento = tk.StringVar()


# Configuración del título
titulo = tk.Label(ventana, text="Llenar Formulario", font=("Arial", 14), bg="gray")
titulo.grid(columnspan=2, pady=10)

# Configuración de las cajas de texto y las etiquetas de error
label1 = tk.Label(ventana, text="Marca:").grid(column=0, row=1, padx=30, pady=20)
t1 = tk.Entry(ventana, width=24, textvariable=marca)
t1.grid(column=1, row=1, padx=30, pady=5)
marca_error = tk.Label(ventana, text="", fg="red", bg="gray")
marca_error.place(x=160, y=90)

label2 = tk.Label(ventana, text="procesador:").grid(column=0, row=2, padx=30, pady=20)
t2 = tk.Entry(ventana, width=24, textvariable=procesador)
t2.grid(column=1, row=2, padx=30, pady=5)
procesador_error = tk.Label(ventana, text="", fg="red", bg="gray")
procesador_error.place(x=160, y=150)

label3 = tk.Label(ventana, text="Memoria Ram:").grid(column=0, row=3, padx=30, pady=20)
t3 = tk.Entry(ventana, width=24, textvariable=ram)
t3.grid(column=1, row=3, padx=30, pady=5)
almacenamiento_error = tk.Label(ventana, text="", fg="red", bg="gray")
almacenamiento_error.place(x=180, y=270)

label4 = tk.Label(ventana, text="Almacenamiento:").grid(column=0, row=4, padx=30, pady=20)
t4 = tk.Entry(ventana, width=24, textvariable=almacenamiento)
t4.grid(column=1, row=4, padx=30, pady=5)
ram_error = tk.Label(ventana, text="", fg="red", bg="gray")
ram_error.place(x=170, y=210)



boton_validar = tk.Button(ventana, text="guardar", command=validar_informacion)
boton_validar.grid(row=6, column=1, pady=10)


# Enlace de las cajas de texto con los eventos del teclado
t1.bind("<KeyRelease>", validar_marca)
t2.bind("<KeyRelease>", validar_procesador)
t3.bind("<KeyRelease>", validar_ram)
t4.bind("<KeyRelease>", validar_almacenamiento)

ventana.mainloop()
