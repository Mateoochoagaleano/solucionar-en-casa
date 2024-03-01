import os

# Definir los precios de los productos
PRECIO_COMPUTADOR = 5000000
PRECIO_TABLETA = 2000000
PRECIO_VIDEOBEAM = 700000
PRECIO_TELEVISOR = 4000000

# Inicializar variables para contar la cantidad de productos comprados
cantidad_computadores = 0
cantidad_tabletas = 0
cantidad_videobeams = 0
cantidad_televisores = 0

# Función para limpiar la pantalla
def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

# Función para mostrar el menú de opciones
def mostrar_menu():
    limpiar_pantalla()
    print("<<< MENÚ DE OPCIONES >>>")
    print("1. Computador de escritorio")
    print("2. Tableta")
    print("3. Videobeam")
    print("4. Televisor")
    print("5. Facturar")

# Inicializar variable para el total a pagar
total_a_pagar = 0

# Loop principal
while True:
    mostrar_menu()
    opcion = input("Ingrese el número de opción (1-5): ")

    if opcion == '1':
        cantidad_computadores += 1
        total_a_pagar += PRECIO_COMPUTADOR
    elif opcion == '2':
        cantidad_tabletas += 1
        total_a_pagar += PRECIO_TABLETA
    elif opcion == '3':
        cantidad_videobeams += 1
        total_a_pagar += PRECIO_VIDEOBEAM
    elif opcion == '4':
        cantidad_televisores += 1
        total_a_pagar += PRECIO_TELEVISOR
    elif opcion == '5':
        limpiar_pantalla()
        print("RESUMEN DE COMPRA")
        print("Computadores de escritorio:", cantidad_computadores)
        print("Tabletas:", cantidad_tabletas)
        print("Videobeams:", cantidad_videobeams)
        print("Televisores:", cantidad_televisores)
        print("Total a pagar: $", total_a_pagar)
        break
    else:
        print("Opción inválida. Por favor, ingrese un número válido. ")