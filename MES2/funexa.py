import random  

def menu():
    print("1) Generar una lista única de números ingresados por el teclado")
    print("2) Generar una lista de números aleatorios")
    print("3) Búsqueda lineal")
    print("4) Búsqueda binaria")
    print("5) Descomposición de un número en dígitos")
    print("6) Salir del programa")

def teclado (lista):
    n = int(input("ingresa de cuantos elemenetos quieres tu lista"))
    for i in range(n):
        num=int(input("ingresa el elemneto de tu lista:"))
        lista.append(num)
    return lista


def aleatoria(lista):
    n = int(input("¿Cuántos números únicos deseas generar?: "))
    x=int(input("¿Cual es el minimo de tu lista?: "))
    y=int(input("¿Cual es el maximo de tu lista?: "))

    lista = random.sample(range(x, y), n)  
    return lista  

def burbuja(lista):
    n = len(lista)
    for i in range(n):  
        for j in range(0, n - i - 1): 
            if lista[j] > lista[j + 1]: 
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista  

def lineal(lista):
    objetivo = int(input("Ingresa el número a encontrar: "))  
    for i, valor in enumerate(lista):  
        if valor == objetivo:
            return i  
    return -1  


def binaria(lista):
    objetivo = int(input("Ingresa el número a encontrar: "))  
    lista.sort() 
    izquierda, derecha = 0, len(lista) - 1 

    while izquierda <= derecha:  
        medio = (izquierda + derecha) // 2  
        if lista[medio] == objetivo:
            return medio  
        elif lista[medio] < objetivo:
            izquierda = medio + 1  
        else:
            derecha = medio - 1
    return -1  

def descomponer_numero(n):
    if n < 10:  
        return [n]
    else:  
        return descomponer_numero(n // 10) + [n % 10]  
