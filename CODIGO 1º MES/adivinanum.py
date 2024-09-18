import random

num = random.randint(0, 10)
cont = 0  

while True:
   
    num1 = int(input("Adivina el número entre 0 y 10: "))
    cont += 1  
    if num1 < num:
            print("Demasiado bajo, intenta de nuevo.")
    elif num1 > num:
            print("Demasiado alto, intenta de nuevo.")
    else:
            print(f"¡Correcto! Adivinaste el número en {cont} intentos.")
            break 

 