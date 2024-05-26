import requests

class Comunicacion():

    def __init__(self, ventanaPrincipal):
        self.url = 'http://localhost:8000/v1/auto'
        self.ventanaPrincipal = ventanaPrincipal
        pass

    def guardar(self, marca, velocidad, placa, color):
        try:
            print(marca, velocidad, placa, color)
            data = {
                'marca': marca,
                'velocidad': velocidad,
                'placa': placa,
                'color': color
            }
            resultado = requests.post(self.url, json=data)
            print(resultado.json)
            return resultado
        except:
            pass

    def actualizar(self,id, marca, velocidad, placa, color):
        try:
            print(marca, velocidad, placa, color)
            data = {
                'marca': marca,
                'velocidad': velocidad,
                'placa': placa,
                'color': color
            }
            resultado = requests.put(self.url + '/' + id + '/', json=data)
            print(resultado.json)
            return resultado
        except:
            pass
    
    def consultar(self, id):
        resultado = requests.get(self.url + '/' + str(id))
        return resultado.json()
    
    def eliminar(self, id):
        resultado = requests.delete(self.url + '/' + str(id))
        return resultado.status_code
    
    def consultar_todo(self, marca, velocidad, placa, color):
        url = self.url+ "?"
        print(type(placa))
        if marca != '':
            url = url + 'marca=' + str(marca) + "&"
        if velocidad != '':
            url = url + 'velocidad=' + str(velocidad) + "&"
        if  placa != '':
            url = url + 'placa=' + str(placa) + "&"
        if  color != '':
            url = url + 'color=' + str(color) + "&"
        print(url)
        resultado = requests.get(url)
        return resultado.json()