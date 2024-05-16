import re
import requests

response = requests.get("http://localhost:8000")

class Modelo:
    def __init__(self):
        self.marca = ""
        self.procesador = ""
        self.memoriaRam = ""
        self.almacenamiento = ""

    def set_marca(self, marca):
        self.marca = marca

    def set_procesador(self, procesador):
        self.procesador = procesador

    def set_memoriaRam(self, memoriaRam):
        self.memoriaRam = memoriaRam

    def set_almacenamiento(self, almacenamiento):
        self.almacenamiento = almacenamiento

    def validar_datos(self):
        if not re.match("^[a-zA-Z0-9 ]+$", self.marca):
            return False
        if not re.match("^[a-zA-Z0-9 ]+$", self.procesador):
            return False
        if not re.match("^[a-zA-Z0-9 ]+$", self.memoriaRam):
            return False
        if not re.match("^[a-zA-Z0-9 ]+$", self.almacenamiento):
            return False
        return True

    def enviarDatos(self):
        data = {
            "marca": self.marca,  
            "procesador": self.procesador,  
            "memoriaRam": self.memoriaRam,  
            "almacenamiento": self.almacenamiento  
        }

        response = requests.post("http://127.0.0.1:8000/v1/computador",data)
        print(response.status_code)
        print(response.content)
