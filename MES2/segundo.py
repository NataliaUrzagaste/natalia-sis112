import random  # Importa el módulo random para generar números aleatorios

# Función para mostrar el menú de opciones al usuario
def menu():
    print("1) Generar una lista única de números ingresados por el teclado")
    print("2) Generar una lista de números aleatorios")
    print("3) Ordenar lista")
    print("4) Búsqueda lineal")
    print("5) Búsqueda binaria")
    print("6) Descomposición de un número en dígitos")
    print("7) Salir del programa")

# Función para generar una lista con números ingresados manualmente, sin repetir
def teclado(lista):
    continuar = 's'
    while continuar == 's':  # Repite mientras el usuario quiera agregar más números
        num = int(input("Ingresa un número único: "))
        if num in lista:
            print("El número ya existe en la lista. Intenta con otro número.")
        else:
            lista.append(num)  # Agrega el número a la lista si no está repetido
            print("Número agregado correctamente.")
        
        continuar = input("¿Deseas agregar otro número? (s/n): ").strip().lower()  # Pregunta si agregar más números
    
    print("Lista final:", lista)  # Muestra la lista completa al final
    return lista  # Devuelve la lista generada

# Función para generar una lista de números aleatorios sin repetir
def aleatoria(lista):
    n = int(input("¿Cuántos números únicos deseas generar? (máximo 100): "))
    if n > 100:
        print("Error: No se pueden generar más de 100 números únicos en el rango de 1 a 100.")
        return []  # Si el número de elementos es mayor a 100, retorna una lista vacía
    
    lista = random.sample(range(1, 101), n)  # Genera n números únicos en el rango 1-100
    print("Lista generada:", lista)
    return lista  # Devuelve la lista generada

# Función para ordenar una lista con el método de burbuja
def burbuja(lista):
    n = len(lista)
    for i in range(n):  # Recorre todos los elementos de la lista
        for j in range(0, n - i - 1):  # Compara cada par de elementos consecutivos
            if lista[j] > lista[j + 1]:  # Si el elemento actual es mayor, intercambia
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista  # Devuelve la lista ordenada

# Función para realizar una búsqueda lineal en una lista
def lineal(lista):
    objetivo = int(input("Ingresa el número a encontrar: "))  # Solicita el número a buscar
    for i, valor in enumerate(lista):  # Recorre la lista buscando el objetivo
        if valor == objetivo:
            return i  # Si encuentra el número, retorna el índice
    return -1  # Si no encuentra el número, retorna -1

# Función para realizar una búsqueda binaria en una lista ordenada
def binaria(lista):
    objetivo = int(input("Ingresa el número a encontrar: "))  # Solicita el número a buscar
    lista.sort()  # Ordena la lista antes de realizar la búsqueda binaria
    izquierda, derecha = 0, len(lista) - 1  # Establece los límites de búsqueda

    while izquierda <= derecha:  # Mientras haya elementos por revisar
        medio = (izquierda + derecha) // 2  # Calcula el punto medio
        if lista[medio] == objetivo:
            return medio  # Si encuentra el número, retorna el índice
        elif lista[medio] < objetivo:
            izquierda = medio + 1  # Ajusta los límites según la búsqueda
        else:
            derecha = medio - 1
    return -1  # Si no encuentra el número, retorna -1

# Función para descomponer un número en dígitos usando recursión
def descomponer_numero(n):
    if n < 10:  # Caso base: si el número tiene solo un dígito
        return [n]
    else:  # Caso recursivo: llama a la función con n dividido entre 10
        return descomponer_numero(n // 10) + [n % 10]  # Llama a la función recursivamente y agrega el último dígito
