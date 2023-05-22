import sqlite3

conexion=sqlite3.connect('Ejemplo.db')

c=conexion.cursor()

c.execute("SELECT * From acciones")

print(c.fetchone())

conexion.close()