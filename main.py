# Versión main diferente
from catalogo import cargar_catalogo, mostrar_catalogo
from carrito import agregar_producto, eliminar_producto
from descuentos import calcular_subtotal, aplicar_descuento
from ticket import generar_ticket

catalogo = cargar_catalogo()
carrito = []
total = 0

while True:
    print("\n1.Mostrar catalogo 2.Agregar 3.Eliminar 4.Ver carrito 5.Subtotal 6.Descuento 7.Ticket 8.Salir")
    opcion = input("Selecciona una opcion: ")
    if opcion == "1":
        mostrar_catalogo(catalogo)
    elif opcion == "2":
        mostrar_catalogo(catalogo)
        agregar_producto(carrito, catalogo, input("ID: "), int(input("Cantidad: ")))
    elif opcion == "3":
        eliminar_producto(carrito, input("ID: "))
    elif opcion == "4":
        print(carrito if carrito else "El carrito esta vacio.")
    elif opcion == "5":
        print("Subtotal: $", calcular_subtotal(carrito, catalogo) if carrito else "carrito vacio")
    elif opcion == "6":
        subtotal = calcular_subtotal(carrito, catalogo)
        od = input("1.10% 2.3x2 3.Sin descuento: ")
        tipo = "porcentaje" if od=="1" else "3x2" if od=="2" else "ninguno"
        total = aplicar_descuento(subtotal, tipo)
        print("Total: $", total)
    elif opcion == "7":
        if not carrito: print("Carrito vacio")
        else:
            subtotal = calcular_subtotal(carrito, catalogo)
            total = aplicar_descuento(subtotal, "porcentaje") if input("¿Descuento 10%? s/n: ")=="s" else subtotal
            print("Registro:", generar_ticket(carrito, catalogo, total))
    elif opcion == "8":
        break
