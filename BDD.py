import sqlite3

conexion = sqlite3.connect('Ejemplo.db')

c=conexion.cursor()

c.execute("INSERT INTO acciones Values('24/nov/2016', 'compra', 'INV', 100, 15.43)")
c.execute("INSERT INTO acciones Values('21/oct/2021', 'sd', 'I', 200, 23.42 )")
c.execute("INSERT INTO acciones Values('2/sep/2010', 'Ayuda', 'INV', 2000, 1.42 )")
c.execute("INSERT INTO acciones Values('1/oct/2002', 'Dinero', 'INV', 100, 65.00 )")
c.execute("INSERT INTO acciones Values('1/dic/2005', 'Hola', 'IN', 20, 1.0 )")

conexion.commit()

conexion.close()
