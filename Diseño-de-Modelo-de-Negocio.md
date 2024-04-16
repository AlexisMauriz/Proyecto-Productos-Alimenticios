# Diseño de Modelo de Negocio.

## Listado de Entidades

### Ventas **(ED)**

- ID **(PK)**
- Producto
- Precio
- Proveedores
- Fecha **(UQ)**

## Relaciones

1. Una **Venta** _puede llegar a ser de_ a 1 o Muchos **ProductoS** (_1 a M_).
1. Un **Producto** _Pertenece_ a 1 o muchas **Productos** (_1 a OM_).
1. Un **Proveedor** _Puede ser _ 1 o muchas **Provedores** (_1 a M_).

## Diagramas

### Modelo Relacional de la Base de Datos No-Relacional

1[Diagrama de Negocio](./Diagrama%20-%20Modelo%20de%20Negocio.png)

## Reglas de Negocio

### Registro con metodología CRUD

1. Registrar ID de Producto.
1. Registrar Producto vendido.
1. Registrar Pricio.
1. Seleccionar Proveedor.
1. Registrar Fecha de Venta
1. Eliminar un cliente.

### Productos

1. Registrar todos los productos.
1. Actualizar un producto.
1. Eliminar un producto.

### Venta

1. Registrar todas las ventas.
1. Actualizar una venta.
1. Actualizar precio de productos.
1. Emiminar una venta.
1. Identificar Proveedor de Productos.

### Proveedores

1. Registar un proveedor.
1. Actualizar Proveedor de productos.
1. Emiminar registro de Proveedor.
1. Identificar Proveedor de Productos.

### Fecha

1. Registar Fecha de Venta.
1. Actualizar Fecha Venta.
1. Emiminar registro de Venta.
