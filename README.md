# Código de Proyecto.

- El código se realiza con el lenguaje de Python, Tkinter y SQLite.

## Código de Base de Datos No-Relacional

- Conexión a la base de datos SQLite (SQLite3) y creación de tabla con comandos de SQLite para crear tabla de base de tados, lista con sus comandos.

```python
import sqlite3

def crear_tabla():
    conn = sqlite3.connect('Productos.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Productos (
            id TEXT PRIMARY KEY,
            producto TEXT,
            precio INT,
            proveedor TEXT,
            fecha INT)''')
    conn.commit()
    conn.close()

def fetch_productos():
  conn = sqlite3.connect('Productos.db')
  cursor = conn.cursor()
  cursor.execute('SELECT * FROM Productos')
  productos = cursor.fetchall()
  conn.close()
  return productos

```

- Se incerta los datos de productos.

```python

def insertar_productos(id, producto, precio, proveedor, fecha):
    conn = sqlite3.connect('Productos.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO Productos (id, producto, precio, proveedor, fecha) VALUES (?,?,?,?,?)',
                   (id, producto, precio, proveedor, fecha))
    conn.commit()
    conn.close()
```

- Eliminar datos ingresados.

```python
def eliminar_productos(id):
  conn = sqlite3.connect('Productos.db')
  cursor =  conn.cursor()
  cursor.execute('DELETE FROM Productos WHERE id = ?', (id,))
  conn.commit()
  conn.close()

```

- Actualizar datos.

```python
def actualizar_productos(new_producto, new_precio, new_proveedor, new_fecha, id):
  conn = sqlite3.connect('Productos.db')
  cursor = conn.cursor()
  cursor.execute("UPDATE Productos SET producto=?, precio=?, proveedor=?, fecha=? WHERE id=?",
                 (new_producto, new_precio, new_proveedor, new_fecha, id))
  conn.commit()
  conn.close()

```

- Verificando la existencia de tabla.

```python
def id_exists(id):
    conn = sqlite3.connect('Productos.db')
    cursor = conn.cursor()
    cursor.execute('SELECT COUNT(*) FROM Productos WHERE id = ?',  (id,))
    result = cursor.fetchone()
    conn.close()
    return result[0] > 0 if result else

crear_tabla()

```

## Código de GUI

1. Incorporamos librerias que permiten importar elementos como.
1. **Tkinter** para GUI.
1. **database** para conectar con base de datos
1. **messagebox** para mensajes de casillas.

### Ventana de GUI

- Creamos una ventana de tamaño mediano/grande con color de base negro y no expandible.

```python
app = tk.Tk()
app.title('Sistema de Productos de Animales')
app.geometry('940x420')
app.config(bg='#000000')
app.resizable(False, False)

font = ('Arial', 12, 'bold')
```

- Creando etiquetas de entrada de datos.

```python
create_label_and_entry('ID:', 20)
create_label_and_entry('Productos:', 70)
create_label_and_entry('Precio:', 120)

# Crear etiqueta y entrada para Proveedor
gender_label = tk.Label(app, font=font, text='Proveedor:', fg='#fff', bg='#000000')
gender_label.place(x=20, y=170)

variable1 = tk.StringVar()
variable1.set('Dogchow')
options = ['Dogchow', 'Catchow']
proveedor_options = ttk.Combobox(app, font=font, textvariable=variable1, values=options, state='readonly', width=18)
proveedor_options.place(x=120, y=170)

# Crear etiqueta y entrada para Fecha.
create_label_and_entry('Fecha:', 220)

id_entry = tk.Entry(app, font=font, fg='#000', bg='#fff', borderwidth=2, width=20)
id_entry.place(x=120, y=20)

productos_entry = tk.Entry(app, font=font, fg='#000', bg='#fff', borderwidth=2, width=20)
productos_entry.place(x=120, y=70)

precio_entry = tk.Entry(app, font=font, fg='#000', bg='#fff', borderwidth=2, width=20)
precio_entry.place(x=120, y=120)

fecha_entry = tk.Entry(app, font=font, fg='#000', bg='#fff', borderwidth=2, width=20)
fecha_entry.place(x=120, y=220)
```

- Creando ventana usando Treeview para ingresar y almacenar los datos.

```python
# Crear Treeview
tree = ttk.Treeview(app, height=15)
tree['columns'] = ('ID', 'Producto', 'Precio', 'Proveedor', 'Fecha')
style = ttk.Style()
style.configure("Treeview", background="#FFFF00", foreground="#000000")

# Configurar columnas
# Encabezados de columnas
tree.heading('ID', text='ID')
tree.heading('Producto', text='Producto')
tree.heading('Precio', text='Precio')
tree.heading('Proveedor', text='Proveedor')
tree.heading('Fecha', text='Fecha')  # Asegúrate de que el texto sea 'Fecha'

# Encabezados de columnas
# Encabezados de columnas
tree.heading('ID', text='ID')
tree.heading('Producto', text='Producto')
tree.heading('Precio', text='Precio')
tree.heading('Proveedor', text='Proveedor')
tree.heading('Fecha', text='Fecha')  # Corregir el texto de la etiqueta "State" a "Fecha"

# Posicionar Treeview
tree.place(x=320, y=15)

# Botones
add_button = tk.Button(app, command=insertar, font=font, text='Agendar Dato', fg='#fff', bg='#05A312', width=18)
add_button.place(x=120, y=310)

clear_button = tk.Button(app, command=lambda: limpiar(True), font=font, text='Nuevo Producto', fg='#fff', bg='#0000FF', width=18)
clear_button.place(x=120, y=350)

update_button = tk.Button(app, command=actualizar, font=font, text='Actualizar Producto', fg='#fff', bg='#0000FF', width=18)
update_button.place(x=340, y=350)

delete_button = tk.Button(app, command=eliminar, font=font, text='Eliminar Producto', fg='#fff', bg='#FF0000', width=18)
delete_button.place(x=560, y=350)

app.mainloop()

```
# Proyecto-Productos-Alimenticios
