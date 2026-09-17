# Modulo carrito - version final

def agregar_producto(carrito, catalogo, id_producto, cantidad):
    carrito.append((id_producto, cantidad))

# Validar stock antes de agregar

def eliminar_producto(carrito, id_producto):
        if not carrito:
        print("El carrito esta vacio.")
        return
    for producto in carrito:
        if producto[0] == id_producto:
            carrito.remove(producto)
            print("Producto eliminado.")
            return
            
