#num=0
#n=int(input())
#nume= (n/2) * (n + 1)
#print(nume)
#while num<n:
    #num= num+1
    #if num%2:
        #print(num)

#codigo con matrices para sacar promedio 
# dimens de la matris
filas = int(input("ingresa el número de filas "))
columnas = int(input("ingresa el número de columnas "))

elementos = [] #lista para los elementos
i=0
j=0
print("ingresa los elementos de la matriz")
for i in range(filas):
    for j in range(columnas):
        valor = float(input(f"Elemento en la posición [{i}, {j}]: ")) #f para mesclar texto y numeros en {}
        elementos.append(valor)

suma_total = sum(elementos) #suma todoslos elementos
total_elementos = len(elementos) #cuenta todos los elemnetos
promedio = suma_total / total_elementos
#  promedio
print("El promedio de los elementos de la matriz es:", promedio)