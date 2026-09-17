def calcular_subtotal(carrito, catalogo):
    subtotal = 0
    for id_producto, cantidad in carrito:
        subtotal += catalogo[id_producto]["precio"] * cantidad
    return subtotal

def aplicar_descuento(subtotal, tipo_descuento):
    reglas = {"porcentaje": 0.10, "3x2": 1/3}
    if tipo_descuento == "porcentaje":
        return subtotal - (subtotal * reglas["porcentaje"])
    elif tipo_descuento == "3x2":
        return subtotal - (subtotal * reglas["3x2"])
    else:
        return subtotal
