import sqlite3

# Conectar a la base de datos (si no existe, se creará)
conn = sqlite3.connect('Tarea.db')
cursor = conn.cursor()

# Crear la tabla
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    edad INTEGER NOT NULL,
    email TEXT NOT NULL UNIQUE
)
''')

# Confirmar los cambios y cerrar la conexión
conn.commit()
conn.close()
