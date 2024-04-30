import threading
import time
import logging

class Hilo6(threading.Thread):
    def __init__(self, nombre):
        threading.Thread.__init__(self, name=nombre)
        self.nombre = nombre

    def run(self):
        with open("nombres.txt", "a+") as archivo:
            while True:
                nombre = input("Ingrese un nombre: ")
                archivo.write(nombre + "\n")
                archivo.flush()  # Asegura que el nombre se escriba en el archivo
                
                time.sleep(2)  # Pausa la ejecución del hilo durante 2 segundos

                
                archivo.seek(0)
                print("Todos los nombres guardados:")
                for nombre_guardado in archivo:
                    logging.debug(nombre_guardado.strip())  # Imprime cada nombre eliminando espacios extra y saltos de línea