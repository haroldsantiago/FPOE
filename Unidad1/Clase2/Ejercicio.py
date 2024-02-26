import tkinter as tk
from tkcalendar import DateEntry

#Configuracion de la ventana

ventana = tk.Tk()
ventana.geometry("500x300+200+100")
ventana.resizable(0, 0)
ventana.title("Interfaz Trabajo Final")
ventana.configure(bg="gray")

#Funcion Validar Nombre
def validar_nombre(evento):
    texto_ingresado = nom.get()
    if texto_ingresado.isalpha():
        pass
    else:
        print("¡No se permiten números ni caracteres especiales!")

#Funcion validar Apellido
def validar_apellido(evento):
    texto_ingresado = apel_1.get()
    if texto_ingresado.isalpha():
        pass
    else:
        print("¡No se permiten números ni caracteres especiales!")

#Funcion validar Edad
def validar_edad(evento):
    texto_ingresado = edad.get()
    if texto_ingresado.isdigit():
        pass
    else:
        print("¡No se permiten números ni caracteres especiales!")


#Funcion validar Correo
def validar_correo(evento):
    texto_ingresado = correo.get()
    caracteres_permitidos = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@.")
    if all(caracter in caracteres_permitidos for caracter in texto_ingresado):
        pass
    else:
        print("¡Solo se permiten letras, números, '@' y '.' en el correo electrónico!")

#Funcion validar Fecha Nacimiento
def validar_fecha(evento):
    texto_ingresado = fecha.get()
    caracteres_permitidos = set("0123456789/")
    if len(texto_ingresado) <= 10 and all(caracter in caracteres_permitidos for caracter in texto_ingresado):
        pass
    else:
        print("¡La fecha de nacimiento debe tener máximo 10 caracteres en formato DD/MM/YY y solo contener números y '/'!")

    


fecha = tk.StringVar()
apel_1 = tk.StringVar()
nom = tk.StringVar()
correo = tk.StringVar()
edad = tk.StringVar()


#Configuracion de las cajas de texto y los titulos
label1 = tk.Label(ventana, text="Nombre completo:").grid(column=0, row=0, padx=30, pady=10)
t1 = tk.Entry(ventana, width=24, textvariable=nom)
t1.grid(column=1, row=0, padx=30, pady=10)

label2 = tk.Label(ventana, text="Apellidos:").grid(column=0, row=1, padx=30, pady=10)
t2 = tk.Entry(ventana, width=24, textvariable=apel_1)
t2.grid(column=1, row=1, padx=30, pady=10)

label3 = tk.Label(ventana, text="Correo:").grid(column=0, row=2, padx=30, pady=10)
t3 = tk.Entry(ventana, width=24, textvariable=correo)
t3.grid(column=1, row=2, padx=30, pady=10)

label4 = tk.Label(ventana, text="Edad:").grid(column=0, row=3, padx=30, pady=10)
t4 = tk.Entry(ventana, width=24, textvariable=edad)
t4.grid(column=1, row=3, padx=30, pady=10)

label6 = tk.Label(ventana, text="Fecha de nacimiento:").grid(column=0, row=4, padx=30, pady=10)
t6 = tk.Entry(ventana, width=24, textvariable=fecha)
t6.grid(column=1, row=4, padx=30, pady=10)

#Enlace de las cajas de texto con los eventos del teclado
t1.bind("<KeyRelease>", validar_nombre)
t2.bind("<KeyRelease>", validar_apellido)
t3.bind("<KeyRelease>", validar_correo)
t4.bind("<KeyRelease>", validar_edad)
t6.bind("<KeyRelease>", validar_fecha)


ventana.mainloop()