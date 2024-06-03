import requests

class Comunicacion():

    def __init__(self, ventanaPrincipal):
        self.url = 'http://localhost:8000/v1/computador'
        self.ventanaPrincipal = ventanaPrincipal
        pass

    def guardar(self, marca, procesador, memoriaRam, almacenamiento):
        try:
            print(marca, procesador, memoriaRam, almacenamiento)
            data = {
                'marca': marca,
                'procesador': procesador,
                'memoriaRam': memoriaRam,
                'almacenamiento': almacenamiento
            }
            resultado = requests.post(self.url, json=data)
            print(resultado.json)
            return resultado
        except:
            pass
    
    def consultar(self, id):
        resultado = requests.get(self.url + '/' + str(id))
        print(resultado.text)
        print(resultado.status_code)
        try:
            return resultado.json()
        except ValueError:
            print("Respuesta no es un JSON válido.")
            return None
    
    def consultar_todo(self, marca, procesador, memoriaRam, almacenamiento):
        url = self.url + "?"
        print(type(memoriaRam))
        if marca != '':
            url = url + 'marca=' + str(marca) + "&"
        if procesador != '':
            url = url + 'procesador=' + str(procesador) + "&"
        if  memoriaRam != '':
            url = url + 'memoriaRam=' + str(memoriaRam) + "&"
        if  almacenamiento != '':
            url = url + 'almacenamiento=' + str(almacenamiento) + "&"
        resultado = requests.get(url)
        return resultado.json()
    
    def actualizar(self, id, marca, procesador, memoriaRam, almacenamiento):
        try:
            print(marca, procesador, memoriaRam, almacenamiento)
            data = {
                'marca': marca,
                'procesador': procesador,
                'memoriaRam': memoriaRam,
                'almacenamiento': almacenamiento
            }
            resultado = requests.put(self.url + '/' + id + '/', json=data)
            print(resultado.json)
            return resultado
        except:
            pass

    def eliminar(self, id):
        resultado = requests.delete(self.url + '/' + str(id))
        return resultado.status_code
