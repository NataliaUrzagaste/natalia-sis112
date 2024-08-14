#x=int(input("dame el primer numero")) #el int es para numeros, el input en general todo(usa mas espacio de memoria)
#y=int(input("dame el segundo numero"))
#print(x) #puedes poner el int a la hora de imprimir para definir la variable tambien
#3print(type(x)) # el type es para definir la variable de retorno XD

def Calcular(operacion, num1, num2):
    if operacion == 1:
        resu = num1 + num2
    elif operacion == 2:
        resu = num1 - num2
    elif operacion == 3:
        resu = num1 * num2
    elif operacion == 4:
        if num2 == 0:
            print("Error: Division por cero")
        else:
            resu = num1 / num2
    elif operacion == 5:
        resu = num1 ** num2
    elif operacion == 6:
        resu = math.sqrt(num1)
    return resu


print("CALCULADORA BASICA")
print("-----------------")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")
print("5. Potenciación")
print("6. Raíz cuadrada")
print("Elige una opción: ")
operacion = int(input())
print("elige tu primer numero")
num1 = int(input())
print("elige tu segundo numero")
num2 = int(input())
print("el resultado es",Calcular(operacion, num1, num2))

