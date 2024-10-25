import random      #se importa la libreria random
def geneList(lista_datos,rango,Vmin,Vmax):
    for i in range(rango):
        dato=random.randint(Vmin,Vmax)
        if dato not in lista_datos:
            lista_datos.append(dato)
        print(dato)
    return lista_datos

def encontrarNumero(lista,numero):
    for i in range(len(lista)):
        if(numero==lista[i]):
            print(f"numero encontrado en el indice: {i}")
            return 1
        
def busqueda_binaria(lista, numero):
    izquierda, derecha = 0, len(lista) -1
    while izquierda <= derecha:
        medio=(izquierda+derecha)//2
        if lista[medio]==numero:
            return medio
        elif lista[medio] < numero:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1

"""
def ordenamiento_burbuja(lista):
    n=len(lista)
    for i in range(n):
        for j in range (0,n-i-1):
            if listas[j]>lista[j+1]:
                lista[j], lista[l+1]=lista[j+1],lista[j]
    return lista"""