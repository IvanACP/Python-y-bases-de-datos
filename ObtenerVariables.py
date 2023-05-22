import sqlite3

conexion=sqlite3.connect('Ejemplo.db')
c=conexion.cursor()

fecha=''
cantidad=''
c.execute('''Select fecha, cantidad FROM acciones''')
registros=c.fetchall()
for registros in registros:
    fecha=registros[0]
    cantidad=registros[1]

conexion.close()

print ("Hora y fecha:",fecha,"Cantidad",cantidad)