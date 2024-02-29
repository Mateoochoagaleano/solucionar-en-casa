var_numeroInt = int(input('Ingrese la cantidad de numeros a evaluar ->'))
contador = 0

for i in range(var_numeroInt):
    num = float(input("Ingrese el número -> "))
    if num >= 10 and num <= 20:
        contador += 1

print(f"La cantidad de números en el rango de 10-20 es: {contador}") 