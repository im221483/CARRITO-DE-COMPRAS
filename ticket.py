from datetime import date
def generar_ticket(carrito, catalogo, total):
    folio = "F001"
    fecha = date.today()
    print("\n==============================")
    print("           TICKET")
    print("==============================")
    for id_producto, cantidad in carrito:
        nombre = catalogo[id_producto]["nombre"]
        precio = catalogo[id_producto]["precio"]
        print("Producto:", nombre, "- Cantidad:", cantidad, "- Precio: $", precio, "- Importe: $", precio*cantidad)
        print("------------------------------")
    print("TOTAL: $", total)
    print("FECHA:", fecha, "FOLIO:", folio)
    return (folio, fecha, total)
