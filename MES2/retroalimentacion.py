"""Desarrolla un programa en Python que simule un sistema de gestión de notas para una clase. El programa debe permitir agregar notas, 
calcular el promedio, obtener la nota máxima y la nota mínima, y mostrar todas las notas."""
notas=[]
# Función para ingresar notas
def ingresar_notas():
    print("ingresa las notas de tu estudiante")
    valor = int(input("ingrese la nota: "))
    notas.append(valor)

def borrar_notas(notas):
    borrar=int(input("dame el numero del indice: "))
    indice= notas.pop(borrar)
    print(f"{indice}")
    
def cam_nota(notas):
    ind=int(input("dame el numero de indice: "))
    note=int(input("dame la nota a reemplazar: "))
    dele= notas.pop(ind)
    add= notas.append(note)
    print(f"se ha reemplazado en el indice {dele} con la nueva nota {add}")


#funcion para mostarr
def mostrar_notas(notas):
    lista= len(notas)
    for i in range (lista):
        print(f"nota {i+1}", notas [i])

        
#funcion promedio
def calcular_promedio(notas):
    promedio = sum(notas)/ len(notas)
    print(f"el promedio es: {promedio}")


#funcion maxima y minima nota
def maximo_minimo(notas):
    print (f"la maxima nota es: {max(notas)}")
    print (f"la minima nota es: {min(notas)}")

