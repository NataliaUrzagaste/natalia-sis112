lista = []
import random
def teclado (lista):
    n = int(input("ingresa de cuantos elemenetos quieres tu lista"))
    for i in range(n):
        num=int(input("ingresa el elemneto de tu lista:"))
        lista.append(num)
    return lista
teclado(lista)