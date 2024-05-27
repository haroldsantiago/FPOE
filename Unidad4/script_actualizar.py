import sqlite3

def update_user(user_id):
    conn = sqlite3.connect('Tarea.db')
    cursor = conn.cursor()

    nombre = input("Ingrese el nuevo nombre o presione Enter para mantener el actual: ")
    if nombre:
        cursor.execute('''
        UPDATE users
        SET nombre = ?
        WHERE id = ?
        ''', (nombre, user_id))

    edad = input("Ingrese la nueva edad o presione Enter para mantener la actual: ")
    if edad:
        cursor.execute('''
        UPDATE users
        SET edad = ?
        WHERE id = ?
        ''', (edad, user_id))

    email = input("Ingrese el nuevo email o presione Enter para mantener el actual: ")
    if email:
        cursor.execute('''
        UPDATE users
        SET email = ?
        WHERE id = ?
        ''', (email, user_id))

    conn.commit()
    conn.close()

# Ejemplo de uso
user_id = int(input("Ingrese el ID del usuario a actualizar: "))
update_user(user_id)
