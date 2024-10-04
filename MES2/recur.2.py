import funrecur as tarea
import time
lista_datos=[]
tamaño=int(input("Ingrese el rango de la lista: "))
minimo=int(input("Ingrese el valor minimo de la lista: "))
maximo=int(input("Ingrese el valor maximo de la lista: "))

inicio=time.time()
tarea.geneList(lista_datos,tamaño,minimo,maximo)
fin=time.time()

print(f"tiempo transcurrido de la generación de la lista \n{(fin-inicio)*1000} ms")
#print(lista_datos)
print(len(lista_datos))
print(type(lista_datos))
num=int(input("Ingrese el numero a encontrar: "))

tarea.encontrarNumero(lista_datos,num)