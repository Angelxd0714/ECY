import sqlite3

# Conectar a la base de datos (creará un nuevo archivo si no existe)
conn = sqlite3.connect('hash_passwords.db')

# Crear un objeto cursor para ejecutar comandos SQL
cursor = conn.cursor()

# Crear una tabla llamada 'usuarios'
cursor.execute('''
    CREATE TABLE IF NOT EXISTS passwords (
        password BLOB NOT NULL PRIMARY KEY,
        salt BLOB NOT NULL
    )
''')

# Guardar (commit) los cambios y cerrar la conexión
conn.commit()
conn.close()

def insert_password(password, salt):
    conn = sqlite3.connect('hash_passwords.db')
    cursor = conn.cursor()

    cursor.execute("INSERT INTO passwords VALUES (?, ?)", (password, salt))

    conn.commit()
    conn.close()
