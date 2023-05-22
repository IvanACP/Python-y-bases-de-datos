import csv
import sqlite3
import tkinter as tk
import os

def guardar_registro():
    id_contacto = entry_id.get()
    nombre = entry_nombre.get()
    apellido_paterno = entry_apellido_paterno.get()
    apellido_materno = entry_apellido_materno.get()
    cumpleaños = entry_cumpleaños.get()
    telefono = entry_telefono.get()

    registro = [id_contacto, nombre, apellido_paterno, apellido_materno, cumpleaños, telefono]
    guardar_registro_csv(registro)
    guardar_registro_bdd(registro)
    mostrar_registros()

def guardar_registro_csv(registro):
    if not os.path.isfile('contactos.csv'):
        with open('contactos.csv', 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['ID_contacto', 'Nombre', 'Apellido_Pat', 'Apellido_Mat', 'Cumpleaños', 'Teléfono'])
    
    with open('contactos.csv', 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(registro)

def guardar_registro_bdd(registro):
    conexion = sqlite3.connect('contactos.db')
    cursor = conexion.cursor()
    
    cursor.execute('''INSERT INTO contactos (ID_contacto, Nombre, Apellido_Pat, Apellido_Mat, Cumpleaños, Teléfono)
                      VALUES (?, ?, ?, ?, ?, ?)''', registro)
    
    conexion.commit()
    conexion.close()

def mostrar_registros():
    if os.path.isfile('contactos.csv'):
        with open('contactos.csv', 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            registros_csv = list(reader)
    else:
        registros_csv = []

    conexion = sqlite3.connect('contactos.db')
    cursor = conexion.cursor()
    
    cursor.execute('SELECT * FROM contactos')
    registros_bdd = cursor.fetchall()

    registros_text.delete('1.0', tk.END)
    registros_text.insert(tk.END, "Registros en CSV:\n")
    for registro in registros_csv:
        registros_text.insert(tk.END, ', '.join(registro) + '\n')
    
    registros_text.insert(tk.END, "\nRegistros en BDD:\n")
    for registro in registros_bdd:
        registros_text.insert(tk.END, ', '.join(str(value) for value in registro) + '\n')
    
    conexion.close()

# Crear la ventana principal
root = tk.Tk()
root.title("Captura de Contactos")

# Crear los campos de entrada
label_id = tk.Label(root, text="ID de contacto:")
entry_id = tk.Entry(root)
label_nombre = tk.Label(root, text="Nombre:")
entry_nombre = tk.Entry(root)
label_apellido_paterno = tk.Label(root, text="Apellido Paterno:")
entry_apellido_paterno = tk.Entry(root)
label_apellido_materno = tk.Label(root, text="Apellido Materno:")
entry_apellido_materno = tk.Entry(root)
label_cumpleaños = tk.Label(root, text="Cumpleaños:")
entry_cumpleaños = tk.Entry(root)
label_telefono = tk.Label(root, text="Teléfono:")
entry_telefono = tk.Entry(root)

# Crear los botones de guardar
button_guardar_csv = tk.Button(root, text="Guardar (CSV)", command=guardar_registro)
button_guardar_bdd = tk.Button(root, text="Guardar (BDD)", command=guardar_registro)

# Posicionar los elementos en la ventana
label_id.grid(row=0, column=0, sticky=tk.E)
entry_id.grid(row=0, column=1)
label_nombre.grid(row=1, column=0, sticky=tk.E)
entry_nombre.grid(row=1, column=1)
label_apellido_paterno.grid(row=2, column=0, sticky=tk.E)
entry_apellido_paterno.grid(row=2, column=1)
label_apellido_materno.grid(row=3, column=0, sticky=tk.E)
entry_apellido_materno.grid(row=3, column=1)
label_cumpleaños.grid(row=4, column=0, sticky=tk.E)
entry_cumpleaños.grid(row=4, column=1)
label_telefono.grid(row=5, column=0, sticky=tk.E)
entry_telefono.grid(row=5, column=1)
button_guardar_csv.grid(row=6, column=0, pady=10)
button_guardar_bdd.grid(row=6, column=1, pady=10)

# Crear la ventana para mostrar los registros
registros_window = tk.Toplevel()
registros_window.title("Registros")

registros_text = tk.Text(registros_window)
registros_text.pack()

# Mostrar los registros iniciales
mostrar_registros()

# Iniciar el bucle de la aplicación
root.mainloop()
