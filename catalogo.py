# Módulo de catálogo - Maneja productos de la tienda
def cargar_catalogo():
    catalogo = {
        "P001": {"nombre": "Café", "precio": 45.0, "stock": 20},
        "P002": {"nombre": "Pan", "precio": 15.0, "stock": 30},
        "P003": {"nombre": "Leche", "precio": 25.0, "stock": 15},
        "P004": {"nombre": "Azúcar", "precio": 20.0, "stock": 10}
    }
    return catalogo

def mostrar_catalogo(catalogo):
    print("ID | Nombre | Precio | Stock")
    for id_prod, datos in catalogo.items():
        print(f"{id_prod} | {datos['nombre']} | {datos['precio']} | {datos['stock']}")
