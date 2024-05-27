import tkinter as tk
from tkinter import ttk
from tkinter.font import Font

class Tabla2():
    def __init__(self, ventanaPrincipal, titulos, columnas, data):
        self.tabla = ttk.Treeview(ventanaPrincipal, columns=columnas, show='headings')
        self.ventanaPrincipal = ventanaPrincipal

        for posicion in range(len(columnas)):
            self.tabla.heading(columnas[posicion], text=titulos[posicion])
            self.tabla.column(columnas[posicion], width=100, stretch=tk.NO)  # Establece un ancho inicial

        self.refrescar(data)

    def refrescar(self, data):
        self.tabla.delete(*self.tabla.get_children())
        for elemento in data:
            self.tabla.insert('', 'end', values=elemento)
        self.autoajustar_columnas()

    def autoajustar_columnas(self):
        for col in self.tabla['columns']:
            max_width = 0
            for row in self.tabla.get_children():
                cell_value = self.tabla.item(row)['values'][self.tabla['columns'].index(col)]
                cell_width = Font(family="TkDefaultFont", size=10).measure(str(cell_value))
                if cell_width > max_width:
                    max_width = cell_width
            self.tabla.column(col, width=max_width + 10)  # Añade un pequeño margen