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
# Ingresar el número de estudiantes y el número de notas por estudiante
num_estudiantes = int(input("Ingrese el número de estudiantes: "))
num_notas = int(input("Ingrese el número de notas por estudiante: "))

# Inicializar la matriz de notas vacía
matriz_notas = []

# Ingresar las notas de los estudiantes
for i in range(num_estudiantes):
    print(f"\nIngrese las notas del estudiante {i+1}:")
    notas = []
    for j in range(num_notas):
        nota = float(input(f"Nota {j+1}: "))
        notas.append(nota)
    matriz_notas.append(notas)

# Calcular y mostrar el promedio de cada estudiante
for i in range(num_estudiantes):
    promedio = sum(matriz_notas[i]) / num_notas
    print(f"El promedio del estudiante {i+1} es: {promedio:.2f}")
