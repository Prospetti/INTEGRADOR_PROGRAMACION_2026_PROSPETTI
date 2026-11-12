import Menu
import Gestion_stock

def main():
    Gestion_stock.inicializar()

    while True:
        opcion = Menu.mostrar_menu()

        if opcion == 1:
            Gestion_stock.cargar_stock()
        elif opcion == 2:
            Gestion_stock.mostrar_stock()
        elif opcion == 3:
            print("Categorias: enlatados, frutas, congelados, panaderia")
            categoria = input("Ingrese la categoria que desea contar: ")
            Gestion_stock.contar(Gestion_stock.stock_cantidades[categoria])
        elif opcion == 4:
            print("Saliendooo")
            break
        else:
            print("Error, vuelva a intentar")

if __name__ == "__main__":
    main()