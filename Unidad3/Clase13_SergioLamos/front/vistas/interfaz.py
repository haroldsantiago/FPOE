import tkinter as tk
from controladores.comunicacion import Comunicacion
from modelos.usuario import Usuario
from controladores.validaciones import Validaciones
from tkinter import messagebox
from vistas.tabla import Tabla

class Interfaz:

    def __init__(self):
        titulos = ['identificador','Marca','Velocidad','Placa','Color']
        columnas = ['id','marca','velocidad','placa','color']
        data = []

        self.ventanaPrincipal = tk.Tk()
        #self.ventanaPrincipal.resizable(0, 0)
        self.comunicacion = Comunicacion(self.ventanaPrincipal)
        self.tabla = Tabla(self.ventanaPrincipal,titulos, columnas, data)

    def validar_entrada(self, valor, etiqueta_error):
        mensaje_error = Validaciones.validarLetrasNumeros(valor)
        if mensaje_error:
            etiqueta_error.config(text=mensaje_error)
        else:
            etiqueta_error.config(text="")

    def accion_guardar_boton(self, marca, velocidad, placa, color, marca_error, velocidad_error, placa_error, color_error):
        # Validaciones
        marca_msg = Validaciones.validarLetrasNumeros(marca)
        velocidad_msg = Validaciones.validarLetrasNumeros(velocidad)
        placa_msg = Validaciones.validarLetrasNumeros(placa)
        color_msg = Validaciones.validarLetrasNumeros(color)
        
        if marca_msg or velocidad_msg or placa_msg or color_msg:
            marca_error.config(text=marca_msg or "")
            velocidad_error.config(text=velocidad_msg or "")
            placa_error.config(text=placa_msg or "")
            color_error.config(text=color_msg or "")
            # Mostrar un mensaje de error general si algún campo no es válido
            messagebox.showwarning("Error", "Por favor, complete todos los campos correctamente.")
        else:
            self.comunicacion.guardar(marca, velocidad, placa, color)
            marca_error.config(text="")
            velocidad_error.config(text="")
            placa_error.config(text="")
            color_error.config(text="")
            # Mostrar un mensaje de éxito
            messagebox.showwarning("Éxito", "Los datos han sido guardados correctamente.")
            self.limpiar_cajas()
            self.accion_consultar_todo(self.entryMarca.get(), self.entryVelocidad.get(), self.entryPlaca.get(), self.entryColor.get())
    
    def accion_actualizar(self, id ,marca, velocidad, placa, color):

        if id =='':
            self.comunicacion.guardar(marca, velocidad, placa, color)
        
        else:
            self.comunicacion.actualizar(id, marca, velocidad, placa, color)
            self.limpiar_cajas()
            self.accion_consultar_todo(self.entryMarca.get(), self.entryVelocidad.get(), self.entryPlaca.get(), self.entryColor.get())

        

    def accion_consultar_boton(self, labelConsultaMarca, labelConsultaVelocidad, labelConsultaPlaca, labelConsultaColor, id):
        resultado = self.comunicacion.consultar(id)
        labelConsultaMarca.config(text=resultado.get('marca'))
        labelConsultaVelocidad.config(text=resultado.get('velocidad'))
        labelConsultaPlaca.config(text=resultado.get('placa'))
        labelConsultaColor.config(text=resultado.get('color'))
    
    def accion_consultar_todo(self, marca, velocidad, placa, color):
        resultado = self.comunicacion.consultar_todo(marca, velocidad, placa, color)
        data= []
        for elemento in resultado:
            data.append((elemento.get('id'),elemento.get('marca'), elemento.get('velocidad'),elemento.get('placa'),elemento.get('color')))
        self.tabla.refrescar(data)

        print(resultado)
        print(type(resultado))


    def limpiar_cajas(self):
        self.entryMarca.delete(0,tk.END)
        self.entryVelocidad.delete(0,tk.END)
        self.entryPlaca.delete(0,tk.END)
        self.entryColor.delete(0,tk.END)
        self.entryId.delete(0,tk.END)

    def mostrar_interfaz(self):
        usuario = Usuario(self.ventanaPrincipal)

#Espacios de texto y entardas de texto principales
        labelMarca = tk.Label(self.ventanaPrincipal, text="Marca")
        self.entryMarca = tk.Entry(self.ventanaPrincipal, textvariable=usuario.marca)
        labelVelocidad = tk.Label(self.ventanaPrincipal, text="Velocidad")
        self.entryVelocidad = tk.Entry(self.ventanaPrincipal, textvariable=usuario.velocidad)
        labelPlaca = tk.Label(self.ventanaPrincipal, text="Placa")
        self.entryPlaca = tk.Entry(self.ventanaPrincipal, textvariable=usuario.placa)
        labelColor = tk.Label(self.ventanaPrincipal, text="Color")
        self.entryColor = tk.Entry(self.ventanaPrincipal, textvariable=usuario.color)
        labelId = tk.Label(self.ventanaPrincipal, text="ID")
        self.entryId = tk.Entry(self.ventanaPrincipal)

        labelConsultaMarca = tk.Label(self.ventanaPrincipal, text='',fg="red")
        labelConsultaVelocidad = tk.Label(self.ventanaPrincipal, text='',fg="red")
        labelConsultaPlaca = tk.Label(self.ventanaPrincipal, text='',fg="red")
        labelConsultaColor = tk.Label(self.ventanaPrincipal, text='',fg="red")

        #Etiquetas de error
        marca_error = tk.Label(self.ventanaPrincipal, text="", fg="red")
        marca_error.place(x=260, y=20)
        velocidad_error = tk.Label(self.ventanaPrincipal, text="", fg="red")
        velocidad_error.place(x=260, y=60)
        placa_error = tk.Label(self.ventanaPrincipal, text="", fg="red")
        placa_error.place(x=260, y=100)
        color_error = tk.Label(self.ventanaPrincipal, text="", fg="red")
        color_error.place(x=260, y=140)

        #Comandos con el teclado
        self.entryMarca.bind("<KeyRelease>", lambda event: self.validar_entrada(self.entryMarca.get(), marca_error))
        self.entryVelocidad.bind("<KeyRelease>", lambda event: self.validar_entrada(self.entryVelocidad.get(), velocidad_error))
        self.entryPlaca.bind("<KeyRelease>", lambda event: self.validar_entrada(self.entryPlaca.get(), placa_error))
        self.entryColor.bind("<KeyRelease>", lambda event: self.validar_entrada(self.entryColor.get(), color_error))

        boton_guardar = tk.Button(self.ventanaPrincipal, text="Guardar", command=lambda: 
        self.accion_guardar_boton(self.entryMarca.get(), self.entryVelocidad.get(), self.entryPlaca.get(), self.entryColor.get(), marca_error, velocidad_error, placa_error, color_error))
        
        boton_consultar_1 = tk.Button(self.ventanaPrincipal, text="Consultar 1", command=lambda:
        self.accion_consultar_boton(labelConsultaMarca, labelConsultaVelocidad, labelConsultaPlaca, labelConsultaColor, self.entryId.get()))
        
        boton_consultar_todos = tk.Button(self.ventanaPrincipal, text="Consultar todos", command=lambda:
        self.accion_consultar_todo(self.entryMarca.get(), self.entryVelocidad.get(), self.entryPlaca.get(), self.entryColor.get()))

        boton_actualizar = tk.Button(self.ventanaPrincipal, text="Actualizar", command=lambda: 
        self.accion_actualizar(self.entryId.get(), self.entryMarca.get(), self.entryVelocidad.get(), self.entryPlaca.get(), self.entryColor.get()))

        boton_limpiar = tk.Button(self.ventanaPrincipal, text="Limpiar", command=lambda:self.limpiar_cajas())
    
        self.ventanaPrincipal.title("Ventana Principal")
        self.ventanaPrincipal.geometry("400x400")

        #Coordenadas de las entradas y texto principal
        labelMarca.place(x=20, y=20)
        self.entryMarca.place(x=120, y=20)
        labelVelocidad.place(x=20, y=60)
        self.entryVelocidad.place(x=120, y=60)
        labelPlaca.place(x=20, y=100)
        self.entryPlaca.place(x=120, y=100)
        labelColor.place(x=20, y=140)
        self.entryColor.place(x=120, y=140)

        boton_guardar.place(x=20, y=180)
        boton_consultar_1.place(x=100, y=180)
        boton_consultar_todos.place(x=180, y=180)
        boton_actualizar.place(x=300, y=180)
        boton_limpiar.place(x=380, y=180)
        
        labelConsultaMarca.place(x=60, y=260)
        labelConsultaVelocidad.place(x=80, y=300)
        labelConsultaPlaca.place(x=60, y=340)
        labelConsultaColor.place(x=60, y=380)

        labelMostrarMarca = tk.Label(self.ventanaPrincipal, text='Marca:')
        labelMostrarMarca.place(x=20, y=260)
        labelMostrarMarcaVelocidad = tk.Label(self.ventanaPrincipal, text='Velocidad:')
        labelMostrarMarcaVelocidad.place(x=20, y=300)
        labelMostrarMarcaPlaca = tk.Label(self.ventanaPrincipal, text='Placa:')
        labelMostrarMarcaPlaca.place(x=20, y=340)
        labelMostrarColor = tk.Label(self.ventanaPrincipal, text='Color:')
        labelMostrarColor.place(x=20, y=380)

        labelId.place(x=20, y=220)
        self.entryId.place(x=60, y=220)

        self.tabla.tabla.place(x=300,y=400)

        def seleccionar_elemento(_):
            for i in self.tabla.tabla.selection():
                valores = self.tabla.tabla.item(i)['values']
                self.entryId.delete(0,tk.END)
                self.entryId.insert(0, str(valores[0]))
                self.entryMarca.delete(0,tk.END)
                self.entryMarca.insert(0, str(valores[1]))
                self.entryVelocidad.delete(0,tk.END)
                self.entryVelocidad.insert(0, str(valores[2]))
                self.entryPlaca.delete(0,tk.END)
                self.entryPlaca.insert(0, str(valores[3]))
                self.entryColor.delete(0,tk.END)
                self.entryColor.insert(0, str(valores[4]))
                
                #Que salga en rojo
                labelConsultaMarca.config(text= str(valores[1]))
                labelConsultaVelocidad.config(text= str(valores[2]))
                labelConsultaPlaca.config(text= str(valores[3]))
                labelConsultaColor.config(text= str(valores[4]))

        def borrar_elemento(_):
            for i in self.tabla.tabla.selection():
                self.comunicacion.eliminar(self.tabla.tabla.item(i)['values'][0])
                self.tabla.tabla.delete(i)

        

        self.tabla.tabla.bind('<<TreeviewSelect>>',seleccionar_elemento)
        self.tabla.tabla.bind('<Delete>',borrar_elemento)



        self.accion_consultar_todo(self.entryMarca.get(), self.entryVelocidad.get(), self.entryPlaca.get(), self.entryColor.get())
        self.ventanaPrincipal.mainloop()
