import tkinter as tk
from tkinter import ttk
import database
from tkinter import messagebox

app = tk.Tk()
app.title('Sistema de Productos de Animales')
app.geometry('940x420')
app.config(bg='#000000')
app.resizable(False, False)

font = ('Arial', 12, 'bold')

def add_to_treeview():
    productos = database.fetch_productos()
    tree.delete(*tree.get_children())
    for producto in productos:
        tree.insert('', tk.END, values=producto)

def insertar():
    id = id_entry.get()
    producto = productos_entry.get()
    precio = precio_entry.get()
    proveedor = variable1.get()
    fecha = fecha_entry.get()
    if not (id and producto and precio and proveedor and fecha):
        messagebox.showerror('Error', 'Ingresar dato.')
    elif database.id_exists(id):
        messagebox.showerror('Error', 'ID ya existe.')
    else:
        database.insertar_productos(id, producto, precio, proveedor, fecha)
        add_to_treeview()
        messagebox.showinfo('Suceso', 'El dato ya ha sido insertado.')

def eliminar():
    selected_item = tree.focus()
    if not selected_item:
        messagebox.showerror('Error', 'Opción elegida eliminada.')
    else:
        productos_id = tree.item(selected_item)['values'][0]
        database.eliminar_productos(productos_id)
        add_to_treeview()
        messagebox.showinfo('Suceso', 'Dato eliminado.')

def limpiar(*clicked):
    if clicked:
        tree.selection_remove(tree.focus())
        id_entry.delete(0, tk.END)
        productos_entry.delete(0, tk.END)
        precio_entry.delete(0, tk.END)
        variable1.set('DogChow')
        fecha_entry.delete(0, tk.END)

def display_data(event):
    selected_item = tree.focus()
    if selected_item:
        row = tree.item(selected_item)['values']
        eliminar()
        id_entry.insert(0, row[0])
        productos_entry.insert(0, row[1])
        precio_entry.insert(0, row[2])
        variable1.set(row[3])
        fecha_entry.insert(0, row[4])
    else:
        pass
    tree.bind('<ButtonRelease>', display_data)


def actualizar():
    select_item = tree.focus()
    if not select_item:
        messagebox.showerror('Error', 'Opción elejida no actualizada.')
    else:
        id = id_entry.get()
        producto = productos_entry.get()
        precio = precio_entry.get()
        proveedor = variable1.get()
        fecha = fecha_entry.get()
        database.actualizar_productos(producto, precio, proveedor, fecha, id)
        add_to_treeview()
        eliminar()
        messagebox.showinfo('Suceso', 'Datos actualizados')

# Función para crear etiquetas y entradas con formato adecuado
def create_label_and_entry(text, y_position):
    label = tk.Label(app, font=font, text=text, fg='#fff', bg='#000000')
    label.place(x=20, y=y_position)

    entry = tk.Entry(app, font=font, fg='#000', bg='#fff', borderwidth=2, width=20)
    entry.place(x=120, y=y_position)

# Crear etiquetas y entradas para ID, Name, Role, Gender y Status
create_label_and_entry('ID:', 20)
create_label_and_entry('Productos:', 70)
create_label_and_entry('Precio:', 120)

# Crear etiqueta y entrada para Gender
gender_label = tk.Label(app, font=font, text='Proveedor:', fg='#fff', bg='#000000')
gender_label.place(x=20, y=170)

variable1 = tk.StringVar()
variable1.set('Dogchow')
options = ['Dogchow', 'Catchow']
proveedor_options = ttk.Combobox(app, font=font, textvariable=variable1, values=options, state='readonly', width=18)
proveedor_options.place(x=120, y=170)

# Crear etiqueta y entrada para Status.
create_label_and_entry('Fecha:', 220)

id_entry = tk.Entry(app, font=font, fg='#000', bg='#fff', borderwidth=2, width=20)
id_entry.place(x=120, y=20)

productos_entry = tk.Entry(app, font=font, fg='#000', bg='#fff', borderwidth=2, width=20)
productos_entry.place(x=120, y=70)

precio_entry = tk.Entry(app, font=font, fg='#000', bg='#fff', borderwidth=2, width=20)
precio_entry.place(x=120, y=120)

fecha_entry = tk.Entry(app, font=font, fg='#000', bg='#fff', borderwidth=2, width=20)
fecha_entry.place(x=120, y=220)

# Crear Treeview
tree = ttk.Treeview(app, height=15)
tree['columns'] = ('ID', 'Producto', 'Precio', 'Proveedor', 'Fecha')
style = ttk.Style()
style.configure("Treeview", background="#FFFF00", foreground="#000000")

# Configurar columnas
tree.column('#0', width=0, stretch=tk.NO)
tree.column('ID', anchor=tk.CENTER, width=120)
tree.column('Producto', anchor=tk.CENTER, width=120)
tree.column('Precio', anchor=tk.CENTER, width=120)
tree.column('Proveedor', anchor=tk.CENTER, width=100)
tree.column('Fecha', anchor=tk.CENTER, width=120)

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
