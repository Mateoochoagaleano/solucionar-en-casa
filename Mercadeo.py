# Inicializar variables para los productos y sus existencias
codigo_producto_1 = 1
nombre_producto_1 = "TV"
existencias_producto_1 = 5
precio_unitario_1 = 500

codigo_producto_2 = 2
nombre_producto_2 = "Computadora"
existencias_producto_2 = 10
precio_unitario_2 = 1000

codigo_producto_3 = 0
nombre_producto_3 = ""
existencias_producto_3 = 0
precio_unitario_3 = 0

codigo_producto_4 = 0
nombre_producto_4 = ""
existencias_producto_4 = 0
precio_unitario_4 = 0

codigo_producto_5 = 0
nombre_producto_5 = ""
existencias_producto_5 = 0
precio_unitario_5 = 0

codigo_producto_6 = 0
nombre_producto_6 = ""
existencias_producto_6 = 0
precio_unitario_6 = 0

codigo_producto_7 = 0
nombre_producto_7 = ""
existencias_producto_7 = 0
precio_unitario_7 = 0

codigo_producto_8 = 0
nombre_producto_8 = ""
existencias_producto_8 = 0
precio_unitario_8 = 0

codigo_producto_9 = 0
nombre_producto_9 = ""
existencias_producto_9 = 0
precio_unitario_9 = 0

codigo_producto_10 = 0
nombre_producto_10 = ""
existencias_producto_10 = 0
precio_unitario_10 = 0

# Contador para el número de productos registrados
productos_registrados = 3

# Menú principal
while True:
    print("\n1. Comprar producto")
    print("2. Vender producto")
    print("3. Mostrar inventario")
    print("4. Registrar nuevo producto")
    print("5. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":  # Comprar producto
        print("Productos disponibles:")
        print(f"1. {nombre_producto_1} - Código: {codigo_producto_1}")
        print(f"2. {nombre_producto_2} - Código: {codigo_producto_2}")
        print(f"3. {nombre_producto_3} - Código: {codigo_producto_3}")
        print(f"4. {nombre_producto_4} - Código: {codigo_producto_4}")
        print(f"5. {nombre_producto_5} - Código: {codigo_producto_5}")
        print(f"6. {nombre_producto_6} - Código: {codigo_producto_6}")
        print(f"7. {nombre_producto_7} - Código: {codigo_producto_7}")
        print(f"8. {nombre_producto_8} - Código: {codigo_producto_8}")
        print(f"9. {nombre_producto_9} - Código: {codigo_producto_9}")
        print(f"10. {nombre_producto_10} - Código: {codigo_producto_10}")
        
        codigo_producto = int(input("Ingrese el código del producto que desea comprar: "))
        cantidad = int(input("Ingrese la cantidad que desea comprar: "))
        
        if codigo_producto == codigo_producto_1:
            existencias_producto_1 += cantidad
            print(f"Se han añadido {cantidad} unidades del producto {nombre_producto_1}.")
        elif codigo_producto == codigo_producto_2:
            existencias_producto_2 += cantidad
            print(f"Se han añadido {cantidad} unidades del producto {nombre_producto_2}.")
        else:
            print("Producto no válido.")

    elif opcion == "2":  # Vender producto
        print("Productos disponibles:")
        print(f"1. {nombre_producto_1} - Código: {codigo_producto_1}")
        print(f"2. {nombre_producto_2} - Código: {codigo_producto_2}")
        print(f"3. {nombre_producto_3} - Código: {codigo_producto_3}")
        print(f"4. {nombre_producto_4} - Código: {codigo_producto_4}")
        print(f"5. {nombre_producto_5} - Código: {codigo_producto_5}")
        print(f"6. {nombre_producto_6} - Código: {codigo_producto_6}")
        print(f"7. {nombre_producto_7} - Código: {codigo_producto_7}")
        print(f"8. {nombre_producto_8} - Código: {codigo_producto_8}")
        print(f"9. {nombre_producto_9} - Código: {codigo_producto_9}")
        print(f"10. {nombre_producto_10} - Código: {codigo_producto_10}")
        
        codigo_producto = int(input("Ingrese el código del producto que desea vender: "))
        if codigo_producto == codigo_producto_1:
            cantidad = int(input(f"Ingrese la cantidad que desea vender de {nombre_producto_1}: "))
            if existencias_producto_1 >= cantidad:
                existencias_producto_1 -= cantidad
                print(f"Se han vendido {cantidad} unidades del producto {nombre_producto_1}.")
            else:
                print("No hay suficientes existencias para vender.")
        elif codigo_producto == codigo_producto_2:
            cantidad = int(input(f"Ingrese la cantidad que desea vender de {nombre_producto_2}: "))
            if existencias_producto_2 >= cantidad:
                existencias_producto_2 -= cantidad
                print(f"Se han vendido {cantidad} unidades del producto {nombre_producto_2}.")
            else:
                print("No hay suficientes existencias para vender.")
        else:
            print("El producto no está en el inventario.")

    elif opcion == "3":  # Mostrar inventario
        print("Inventario:")
        print(f"Código: {codigo_producto_1}, Nombre: {nombre_producto_1}, Existencias: {existencias_producto_1}, Precio Unitario: {precio_unitario_1}")
        print(f"Código: {codigo_producto_2}, Nombre: {nombre_producto_2}, Existencias: {existencias_producto_2}, Precio Unitario: {precio_unitario_2}")
        print(f"Código: {codigo_producto_3}, Nombre: {nombre_producto_3}, Existencias: {existencias_producto_3}, Precio Unitario: {precio_unitario_3}")
        print(f"Código: {codigo_producto_4}, Nombre: {nombre_producto_4}, Existencias: {existencias_producto_4}, Precio Unitario: {precio_unitario_4}")
        print(f"Código: {codigo_producto_5}, Nombre: {nombre_producto_5}, Existencias: {existencias_producto_5}, Precio Unitario: {precio_unitario_5}")
        print(f"Código: {codigo_producto_6}, Nombre: {nombre_producto_6}, Existencias: {existencias_producto_6}, Precio Unitario: {precio_unitario_6}")
        print(f"Código: {codigo_producto_7}, Nombre: {nombre_producto_7}, Existencias: {existencias_producto_7}, Precio Unitario: {precio_unitario_7}")
        print(f"Código: {codigo_producto_8}, Nombre: {nombre_producto_8}, Existencias: {existencias_producto_8}, Precio Unitario: {precio_unitario_8}")
        print(f"Código: {codigo_producto_9}, Nombre: {nombre_producto_9}, Existencias: {existencias_producto_9}, Precio Unitario: {precio_unitario_9}")
        print(f"Código: {codigo_producto_10}, Nombre: {nombre_producto_10}, Existencias: {existencias_producto_10}, Precio Unitario: {precio_unitario_10}")

    elif opcion == "4":  # Registrar nuevo producto
        if productos_registrados < 10:
            nuevo_codigo = input("Ingrese el código del nuevo producto: ")
            nuevo_nombre = input("Ingrese el nombre del nuevo producto: ")
            nuevo_existencias = int(input("Ingrese la cantidad inicial de existencias del nuevo producto: "))
            nuevo_precio = float(input("Ingrese el precio unitario del nuevo producto: "))
            
            if productos_registrados == 3:
                codigo_producto_3 = nuevo_codigo
                nombre_producto_3 = nuevo_nombre
                existencias_producto_3 = nuevo_existencias
                precio_unitario_3 = nuevo_precio
            elif productos_registrados == 4:
                codigo_producto_4 = nuevo_codigo
                nombre_producto_4 = nuevo_nombre
                existencias_producto_4 = nuevo_existencias
                precio_unitario_4 = nuevo_precio
            elif productos_registrados == 5:
                codigo_producto_5 = nuevo_codigo
                nombre_producto_5 = nuevo_nombre
                existencias_producto_5 = nuevo_existencias
                precio_unitario_5 = nuevo_precio
            elif productos_registrados == 6:
                codigo_producto_6 = nuevo_codigo
                nombre_producto_6 = nuevo_nombre
                existencias_producto_6 = nuevo_existencias
                precio_unitario_6 = nuevo_precio
            elif productos_registrados == 7:
                codigo_producto_7 = nuevo_codigo
                nombre_producto_7 = nuevo_nombre
                existencias_producto_7 = nuevo_existencias
                precio_unitario_7 = nuevo_precio
            elif productos_registrados == 8:
                codigo_producto_8 = nuevo_codigo
                nombre_producto_8 = nuevo_nombre
                existencias_producto_8 = nuevo_existencias
                precio_unitario_8 = nuevo_precio
            elif productos_registrados == 9:
                codigo_producto_9 = nuevo_codigo
                nombre_producto_9 = nuevo_nombre
                existencias_producto_9 = nuevo_existencias
                precio_unitario_9 = nuevo_precio
            elif productos_registrados == 10:
                codigo_producto_10 = nuevo_codigo
                nombre_producto_10 = nuevo_nombre
                existencias_producto_10 = nuevo_existencias
                precio_unitario_10 = nuevo_precio
            
            productos_registrados += 1
            print("Producto registrado.")
        else:
            print("Se ha alcanzado el límite máximo de productos registrados.")

    elif opcion == "5":  # Salir
        print("¡Hasta luego!")
        break

    else:  # Opción inválida
        print("Opción no válida. Por favor, seleccione una opción válida.")