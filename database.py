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
            fecha INT)''')  # Aquí cerramos el paréntesis correctamente
    conn.commit()
    conn.close()

def fetch_productos():
  conn = sqlite3.connect('Productos.db')
  cursor = conn.cursor()
  cursor.execute('SELECT * FROM Productos')
  productos = cursor.fetchall()
  conn.close()
  return productos

# En el archivo database.py

def insertar_productos(id, producto, precio, proveedor, fecha):
    conn = sqlite3.connect('Productos.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO Productos (id, producto, precio, proveedor, fecha) VALUES (?,?,?,?,?)',
                   (id, producto, precio, proveedor, fecha))
    conn.commit()
    conn.close()
  
def eliminar_productos(id):
  conn = sqlite3.connect('Productos.db')
  cursor =  conn.cursor()
  cursor.execute('DELETE FROM Productos WHERE id = ?', (id,))
  conn.commit()
  conn.close() 
  
def actualizar_productos(new_producto, new_precio, new_proveedor, new_fecha, id):
  conn = sqlite3.connect('Productos.db')
  cursor = conn.cursor()
  cursor.execute("UPDATE Productos SET producto=?, precio=?, proveedor=?, fecha=? WHERE id=?",
                 (new_producto, new_precio, new_proveedor, new_fecha, id))
  conn.commit()
  conn.close()
  
def id_exists(id):
    conn = sqlite3.connect('Productos.db')
    cursor = conn.cursor()
    cursor.execute('SELECT COUNT(*) FROM Productos WHERE id = ?',  (id,))
    result = cursor.fetchone()  # Cambiado de fetchall() a fetchone()
    conn.close()
    return result[0] > 0 if result else False  # Asegurarnos de manejar el caso de que no haya resultados

crear_tabla()