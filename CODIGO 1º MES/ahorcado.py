import random

# Lista de palabras
palabras = ["chisme", "monaco", "bromita", "quiero", "nachos"]

# escoje una palabra
palabra_secreta = random.choice(palabras)
palabra_oculta = ["_"] * len(palabra_secreta)  # para los guines
intentos = 6  # intentos ´posibles
letras_intentadas = []

print("juego ahorcado")

# cuando el jugador tiene intentos y todavia haya guiones
while intentos > 0 and "_" in palabra_oculta:
    print("palabra:", palabra_oculta)  
    print("intentos restantes:", intentos)
    print("letras intentadas:", letras_intentadas) 
    letra = input("ingresa una letra: ").lower() #pedimos una letra, lower para usar minusculas
    if letra in letras_intentadas:
        print("ya usaste esta letra, inntenta con otra")
    else:
        letras_intentadas.append(letra)   # el append añade un elemento a la lista

        if letra in palabra_secreta:   # ver si esta la letra
            for i in range(len(palabra_secreta)):
                if palabra_secreta[i] == letra:
                    palabra_oculta[i] = letra
        else:
            intentos -= 1
            print("Letra incorrecta.")
    
if "_" not in palabra_oculta: # cuando el juego acabe
    print("ganaste, la palabra es:", palabra_secreta)
else:
    print("perdiste la palabra es:", palabra_secreta)
