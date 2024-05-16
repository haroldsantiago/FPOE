from models.modelo import Modelo
import re

class Controlador:
    def __init__(self):
        self.modelo = Modelo()

    def validar_datos(self, marca, procesador, memoriaRam, almacenamiento):
        self.modelo.set_marca(marca)
        self.modelo.set_procesador(procesador)
        self.modelo.set_memoriaRam(memoriaRam)
        self.modelo.set_almacenamiento(almacenamiento)

        return self.modelo.validar_datos()
    

    
    def validar_caracteres(self, texto):
        
        patron = re.compile(r'^[a-zA-Z0-9 ]+$')
        return bool(patron.match(texto))
    


    def enviar_datos(self, marca, procesador, memoriaRam, almacenamiento):
        self.modelo.set_marca(marca)
        self.modelo.set_procesador(procesador)
        self.modelo.set_memoriaRam(memoriaRam)
        self.modelo.set_almacenamiento(almacenamiento)

        return self.modelo.enviarDatos()
    
