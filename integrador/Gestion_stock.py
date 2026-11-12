stock_productos = {"enlatados": [], "frutas": [], "congelados": [], "panaderia": []}
stock_cantidades = {"enlatados": [], "frutas": [], "congelados": [], "panaderia": []}

def inicializar():

    for categoria in stock_productos:
        stock_productos[categoria] = []
    for categoria in stock_cantidades:
        stock_cantidades[categoria] = []

def cargar_stock():

    print("Categorias: enlatados, frutas, congelados, panaderia")
    categoria = input("Ingrese la categoria: ")

    producto = input("Ingrese el nombre del producto: ")
    cantidad = int(input("Ingrese la cantidad del producto: "))
    stock_productos[categoria].append(producto)
    stock_cantidades[categoria].append(cantidad)
    print("-Producto agregado-")

def mostrar_stock():

    print("-TOTAL DEL STOCK-")
    for categoria in stock_productos:
        print("Categoria:", categoria)
        productos = stock_productos[categoria]
        cantidades = stock_cantidades[categoria]

        if len(productos) == 0:
            print("no hay productos")
        else:
            for i in range(len(productos)):
                print(productos[i], ":", cantidades[i])

def contar(lista_cantidades):

    tipos_productos = len(lista_cantidades)
    total_unidades = sum(lista_cantidades)
    print("Cantidad de productos:", tipos_productos)
    print("Total de unidades en stock:", total_unidades)