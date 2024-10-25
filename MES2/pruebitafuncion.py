import random 

lista = []

def menu ():
    print("ingresar lista")
    print("generar uns lista aleatoria")
    print("ordenar lista")
    print("busqueda lineal")
    print("busqueda binaria")


def ingresar (lista):
    agregado=int(input("agrega los elementos de la lista"))
    if agregado not in lista:
        lista.append(agregado)
    return lista

def generar (lista):
    rango=int(input("ingresar cuantos elementos tendra la lista"))
    Vmin=int(input("ingrese el valor minimo de la lista"))
    Vmax=int(input("ingrese el valor maximo de la lista"))
    for i in range(rango):
        dato=random.randint(Vmin,Vmax)
        if dato not in lista:
            lista.append(dato)
        print(dato)
    return lista

def ordenar (lista):
    
    