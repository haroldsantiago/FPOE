import re

class Validaciones():
    
    def __init__(self):
        pass

    @staticmethod
    def validarLetrasNumeros(valor):
        patron = re.compile("^[A-Za-zñÑ0-9. @]+$")
        resultado = patron.match(valor) is not None
        if not resultado:
            return "Solo caracteres validos."
        return None
    
    @staticmethod
    def validarValor(valor):
        patron = re.compile("^[0-9]+$")
        resultado = patron.match(valor) is not None
        if not resultado:
            return "Solo caracteres validos."
        return None
    
    @staticmethod
    def validar_correo(correo):
        patron = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
        resultado = patron.match(correo) is not None
        if not resultado:
            return "Correo inválido."
        return None
