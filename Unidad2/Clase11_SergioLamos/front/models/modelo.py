import re
import requests

response = requests.get("http://localhost:8000")

class Modelo:
    def __init__(self):
        self.marca = ""
        self.velocidad = ""
        self.placa = ""
        self.color = ""

    def set_marca(self, marca):
        self.marca = marca

    def set_velocidad(self, velocidad):
        self.velocidad = velocidad

    def set_placa(self, placa):
        self.placa = placa

    def set_color(self, color):
        self.color = color

    def validar_datos(self):
        if not re.match("^[a-zA-Z0-9 ]+$", self.marca):
            return False
        if not re.match("^[a-zA-Z0-9 .]+$", self.velocidad):
            return False
        if not re.match("^[a-zA-Z0-9 ]+$", self.placa):
            return False
        if not re.match("^[a-zA-Z0-9 ]+$", self.color):
            return False
        return True

    def enviarDatos(self):
        data = {
            "marca": self.marca,  
            "velocidad": self.velocidad,  
            "placa": self.placa,  
            "color": self.color  
        }

        response = requests.post("http://127.0.0.1:8000/v1/auto",data)
        print(response.status_code)
        print(response.content)
