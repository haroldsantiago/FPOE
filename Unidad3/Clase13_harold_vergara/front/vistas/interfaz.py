import tkinter as tk
from controladores.comunicacion import Comunicacion
from modelos.usuario import Usuario
from controladores.validaciones import Validaciones
from tkinter import messagebox
from .tabla import Tabla

class Interfaz:

    def __init__(self):
        titulos = ['Identificador', 'Marca', 'Procesador', 'Memoria Ram', 'Almacenamiento']
        columnas = ['id', 'marca', 'procesador', 'memoriaRam', 'almacenamiento']
        data = []
        self.ventanaPrincipal = tk.Tk()
        self.ventanaPrincipal.state("zoomed")
        #self.ventanaPrincipal.resizable(0, 0)
        self.comunicacion = Comunicacion(self.ventanaPrincipal)
        

        self.tabla = Tabla(self.ventanaPrincipal, titulos, columnas, data)

    def limpiar_cajas(self):
        self.entryId.delete(0, tk.END)
        self.entryMarca.delete(0, tk.END)
        self.entryProcesador.delete(0, tk.END)
        self.entryMemoriaRam.delete(0, tk.END)
        self.entryAlmacenamiento.delete(0, tk.END)

    def validar_entrada(self, valor, etiqueta_error):
        mensaje_error = Validaciones.validarLetrasNumeros(valor)
        if mensaje_error:
            etiqueta_error.config(text=mensaje_error)
        else:
            etiqueta_error.config(text="")

    def accion_guardar_boton(self, marca, procesador, memoriaRam, almacenamiento, marca_error, procesador_error, memoriaRam_error, almacenamiento_error):
        # Validaciones
        marca_msg = Validaciones.validarLetrasNumeros(marca)
        procesador_msg = Validaciones.validarLetrasNumeros(procesador)
        memoriaRam_msg = Validaciones.validarLetrasNumeros(memoriaRam)
        almacenamiento_msg = Validaciones.validarLetrasNumeros(almacenamiento)
        
        if marca_msg or procesador_msg or memoriaRam_msg or almacenamiento_msg:
            marca_error.config(text=marca_msg or "")
            procesador_error.config(text=procesador_msg or "")
            memoriaRam_error.config(text=memoriaRam_msg or "")
            almacenamiento_error.config(text=almacenamiento_msg or "")
            # Mostrar un mensaje de error general si algún campo no es válido
            messagebox.showwarning("Error", "Por favor, complete todos los campos correctamente.")
        else:
            self.comunicacion.guardar(marca, procesador, memoriaRam, almacenamiento)
            marca_error.config(text="")
            procesador_error.config(text="")
            memoriaRam_error.config(text="")
            almacenamiento_error.config(text="")
            # Mostrar un mensaje de éxito
            messagebox.showinfo("Éxito", "Los datos han sido guardados correctamente.")
            self.limpiar_cajas()
            self.accion_consultar_todo(self.entryMarca.get(), self.entryProcesador.get(), self.entryMemoriaRam.get(), self.entryAlmacenamiento.get())

    def accion_actualizar(self, id, marca, procesador, memoriaRam, almacenamiento):
        if id == '':
            self.comunicacion.guardar(id, marca, procesador, memoriaRam, almacenamiento)
        else:
            self.comunicacion.actualizar(id, marca, procesador, memoriaRam, almacenamiento)
            self.limpiar_cajas()
            self.accion_consultar_todo(self.entryMarca.get(), self.entryProcesador.get(), self.entryMemoriaRam.get(), self.entryAlmacenamiento.get())
                
            
        

    def accion_consultar_boton(self, labelConsultaMarca, labelConsultaProcesador, labelConsultaMemoriaRam, labelConsultaAlmacenamiento, id):
        resultado = self.comunicacion.consultar(id)
        labelConsultaMarca.config(text=resultado.get('marca'))
        labelConsultaProcesador.config(text=resultado.get('procesador'))
        labelConsultaMemoriaRam.config(text=resultado.get('memoriaRam'))
        labelConsultaAlmacenamiento.config(text=resultado.get('almacenamiento'))
    
    def accion_consultar_todo(self, marca, procesador, memoriaRam, almacenamiento):
        resultado = self.comunicacion.consultar_todo(marca, procesador, memoriaRam, almacenamiento)
        data = []
        for elemento in resultado:
            data.append((elemento.get('id'), elemento.get('marca'), elemento.get('procesador'), elemento.get('memoriaRam'), elemento.get('almacenamiento')))
        self.tabla.refrescar(data)
        print(resultado)
        print(type(resultado))

    def mostrar_interfaz(self):
        usuario = Usuario(self.ventanaPrincipal)

#Espacios de texto y entardas de texto principales
        labelMarca = tk.Label(self.ventanaPrincipal, text="Marca")
        self.entryMarca = tk.Entry(self.ventanaPrincipal, textvariable=usuario.marca)
        labelProcesador = tk.Label(self.ventanaPrincipal, text="Procesador")
        self.entryProcesador = tk.Entry(self.ventanaPrincipal, textvariable=usuario.procesador)
        labelMemoriaRam = tk.Label(self.ventanaPrincipal, text="Memoria Ram")
        self.entryMemoriaRam = tk.Entry(self.ventanaPrincipal, textvariable=usuario.memoriaRam)
        labelAlmacenamiento = tk.Label(self.ventanaPrincipal, text="Almacenamiento")
        self.entryAlmacenamiento = tk.Entry(self.ventanaPrincipal, textvariable=usuario.almacenamiento)
        labelId = tk.Label(self.ventanaPrincipal, text="ID")
        self.entryId = tk.Entry(self.ventanaPrincipal)

        labelConsultaMarca = tk.Label(self.ventanaPrincipal, text='',fg="red")
        labelConsultaProcesador = tk.Label(self.ventanaPrincipal, text='',fg="red")
        labelConsultaMemoriaRam = tk.Label(self.ventanaPrincipal, text='',fg="red")
        labelConsultaAlmacenamiento = tk.Label(self.ventanaPrincipal, text='',fg="red")

        #Etiquetas de error
        marca_error = tk.Label(self.ventanaPrincipal, text="", fg="red")
        marca_error.place(x=260, y=20)
        procesador_error = tk.Label(self.ventanaPrincipal, text="", fg="red")
        procesador_error.place(x=260, y=60)
        memoriaRam_error = tk.Label(self.ventanaPrincipal, text="", fg="red")
        memoriaRam_error.place(x=260, y=100)
        almacenamiento_error = tk.Label(self.ventanaPrincipal, text="", fg="red")
        almacenamiento_error.place(x=260, y=140)

        #Comandos con el teclado
        self.entryMarca.bind("<KeyRelease>", lambda event: self.validar_entrada(self.entryMarca.get(), marca_error))
        self.entryProcesador.bind("<KeyRelease>", lambda event: self.validar_entrada(self.entryProcesador.get(), procesador_error))
        self.entryMemoriaRam.bind("<KeyRelease>", lambda event: self.validar_entrada(self.entryMemoriaRam.get(), memoriaRam_error))
        self.entryAlmacenamiento.bind("<KeyRelease>", lambda event: self.validar_entrada(self.entryAlmacenamiento.get(), almacenamiento_error))

        boton_guardar = tk.Button(self.ventanaPrincipal, text="Guardar", command=lambda: 
        self.accion_guardar_boton(self.entryMarca.get(), self.entryProcesador.get(), self.entryMemoriaRam.get(), self.entryAlmacenamiento.get(), marca_error, procesador_error, memoriaRam_error, almacenamiento_error))
        
        boton_consultar_1 = tk.Button(self.ventanaPrincipal, text="Consultar 1", command=lambda:
        self.accion_consultar_boton(labelConsultaMarca, labelConsultaProcesador, labelConsultaMemoriaRam, labelConsultaAlmacenamiento, self.entryId.get()))
        
        boton_consultar_todos = tk.Button(self.ventanaPrincipal, text="Consultar todos", command=lambda:
        self.accion_consultar_todo(self.entryMarca.get(), self.entryProcesador.get(), self.entryMemoriaRam.get(), self.entryAlmacenamiento.get()))

        boton_actualizar = tk.Button(self.ventanaPrincipal, text="Actualizar", command=lambda:
        self.accion_actualizar(self.entryId.get(), self.entryMarca.get(), self.entryProcesador.get(), self.entryMemoriaRam.get(), self.entryAlmacenamiento.get()))

        boton_limpiar = tk.Button(self.ventanaPrincipal, text="Limpiar", command=lambda:
        self.limpiar_cajas())


        self.ventanaPrincipal.title("Ventana Principal")
        self.ventanaPrincipal.geometry("400x400")

        #Coordenadas de las entradas y texto principal
        labelMarca.place(x=20, y=20)
        self.entryMarca.place(x=120, y=20)
        labelProcesador.place(x=20, y=60)
        self.entryProcesador.place(x=120, y=60)
        labelMemoriaRam.place(x=20, y=100)
        self.entryMemoriaRam.place(x=120, y=100)
        labelAlmacenamiento.place(x=20, y=140)
        self.entryAlmacenamiento.place(x=120, y=140)

        boton_guardar.place(x=20, y=180)
        boton_consultar_1.place(x=100, y=180)
        boton_consultar_todos.place(x=180, y=180)
        boton_actualizar.place(x=280, y=180)
        boton_limpiar.place(x=380, y=180)

        
        
        labelConsultaMarca.place(x=100, y=260)
        labelConsultaProcesador.place(x=100, y=300)
        labelConsultaMemoriaRam.place(x=110, y=340)
        labelConsultaAlmacenamiento.place(x=120, y=380)

        labelMostrarMarca = tk.Label(self.ventanaPrincipal, text='Marca:')
        labelMostrarMarca.place(x=20, y=260)
        labelMostrarProcesador = tk.Label(self.ventanaPrincipal, text='Procesador:')
        labelMostrarProcesador.place(x=20, y=300)
        labelMostrarMemoriaRam = tk.Label(self.ventanaPrincipal, text='Memoria Ram:')
        labelMostrarMemoriaRam.place(x=20, y=340)
        labelMostrarAlmacenamiento = tk.Label(self.ventanaPrincipal, text='Almacenamiento:')
        labelMostrarAlmacenamiento.place(x=20, y=380)

        labelId.place(x=20, y=220)
        self.entryId.place(x=60, y=220)

        self.tabla.tabla.place(x=200, y=300)

        def seleccionar_elemento(_):
            for i in self.tabla.tabla.selection():
                valores = self.tabla.tabla.item(i)['values']
                self.entryId.delete(0, tk.END)
                self.entryId.insert(0, str(valores[0]))
                self.entryMarca.delete(0, tk.END)
                self.entryMarca.insert(0, str(valores[1]))
                self.entryProcesador.delete(0, tk.END)
                self.entryProcesador.insert(0, str(valores[2]))
                self.entryMemoriaRam.delete(0, tk.END)
                self.entryMemoriaRam.insert(0, str(valores[3]))
                self.entryAlmacenamiento.delete(0, tk.END)
                self.entryAlmacenamiento.insert(0, str(valores[4]))

                labelConsultaMarca.config(text= str(valores[1]))
                labelConsultaProcesador.config(text= str(valores[2]))
                labelConsultaMemoriaRam.config(text= str(valores[3]))
                labelConsultaAlmacenamiento.config(text= str(valores[4]))

        def borrar_elemento(_):
            for i in self.tabla.tabla.selection():
                self.comunicacion.eliminar(self.tabla.tabla.item(i)['values'][0])
                self.tabla.tabla.delete(i)


        self.tabla.tabla.bind('<<TreeviewSelect>>', seleccionar_elemento)
        self.tabla.tabla.bind('<Delete>', borrar_elemento)
        
        self.accion_consultar_todo(self.entryMarca.get(), self.entryProcesador.get(), self.entryMemoriaRam.get(), self.entryAlmacenamiento.get())
        self.ventanaPrincipal.mainloop()
