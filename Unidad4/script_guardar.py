import sqlite3

def save_user():
    conn = sqlite3.connect('Tarea.db')
    cursor = conn.cursor()

    nombre = input("Ingrese el nombre: ")
    edad = input("Ingrese la edad: ")
    email = input("Ingrese el email: ")

    cursor.execute('''
    INSERT INTO users (nombre, edad, email)
    VALUES (?, ?, ?)
    ''', (nombre, edad, email))

    conn.commit()
    conn.close()

# Ejemplo de uso
save_user()
