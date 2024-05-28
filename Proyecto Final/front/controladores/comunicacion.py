import requests

class Comunicacion():

    def __init__(self, ventanaPrincipal):
        self.url1 = 'http://192.0.0.1:8000/v1/cliente'
        self.url2 = 'http://192.0.0.1:8000/v1/servicio'
        self.ventanaPrincipal = ventanaPrincipal

        pass

    def guardar(self, nombre, apellido, cedula, telefono, correo):
        try:
            print(nombre, apellido, cedula, telefono, correo)
            data = {
                'nombre': nombre,
                'apellido': apellido,
                'cedula': cedula,
                'telefono': telefono,
                'correo': correo
            }
            resultado = requests.post(self.url1, json=data)
            print(resultado.json)
            return resultado
        except:
            pass


    def guardar_servicio(self, nombre_servicio, cedula_servicio, descripcion_servicio, valor_servicio):
        try:
            print(nombre_servicio, cedula_servicio, descripcion_servicio, valor_servicio)
            data = {
                'nombre': nombre_servicio,
                'cedula': cedula_servicio,
                'descripcion': descripcion_servicio,
                'valor': valor_servicio
            }
            resultado = requests.post(self.url2, json=data)
            print(resultado.json)
            return resultado
        except:
            pass
    

    def actualizar(self,id, nombre_servicio, cedula_servicio, descripcion_servicio, valor_servicio):
        try:
            print(nombre_servicio, cedula_servicio, descripcion_servicio, valor_servicio)
            data = {
                'nombre': nombre_servicio,
                'cedula': cedula_servicio,
                'descripcion': descripcion_servicio,
                'valor': valor_servicio
            }
            resultado = requests.put(self.url2 + '/' + id + '/', json=data)
            print(resultado.json)
            return resultado
        except:
            pass

    def actualizar_cliente(self,id, nombre, apellido, cedula, telefono, correo):
        try:
            print(nombre, apellido, cedula, telefono, correo)
            data = {
                'nombre': nombre,
                'apellido': apellido,
                'cedula': cedula,
                'telefono': telefono,
                'correo': correo
            }
            resultado = requests.put(self.url1 + '/' + id + '/', json=data)
            print(resultado.json)
            return resultado
        except:
            pass


    
    def consultar(self, id):
        resultado = requests.get(self.url1 + '/' + str(id))
        return resultado.json()
    
    def eliminar(self, id):
        resultado = requests.delete(self.url2 + '/' + str(id))
        return resultado.status_code
    
    def eliminar_cliente(self, id):
        resultado = requests.delete(self.url1 + '/' + str(id))
        return resultado.status_code
    
    def consultar_todo(self, nombre_servicio, cedula_servicio, descripcion_servicio, valor_servicio):
        url = self.url2+ "?"
        print(type(cedula_servicio))
        if nombre_servicio != '':
            url = url + 'nombre=' + str(nombre_servicio) + "&"
        if cedula_servicio != '':
            url = url + 'cedula=' + str(cedula_servicio) + "&"
        if  descripcion_servicio != '':
            url = url + 'descripcion=' + str(descripcion_servicio) + "&"
        if  valor_servicio != '':
            url = url + 'valor=' + str(valor_servicio) + "&"
        print(url)
        resultado = requests.get(url)
        return resultado.json()
    
    def consultar_cliente(self, nombre, appellido, cedula, telefono, correo):
        url = self.url1+ "?"
        print(type(cedula))
        if nombre != '':
            url = url + 'nombre=' + str(nombre) + "&"
        if appellido != '':
            url = url + 'apellido=' + str(appellido) + "&"
        if  cedula != '':
            url = url + 'cedula=' + str(cedula) + "&"
        if  telefono != '':
            url = url + 'telefono=' + str(telefono) + "&"
        if  correo != '':
            url = url + 'correo=' + str(correo) + "&"
        print(url)
        resultado = requests.get(url)
        return resultado.json()