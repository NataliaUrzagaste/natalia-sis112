import funexa as exa
lista_teclado = []  
lista_aleatoria = []  

while True:  
    exa.menu()  
    opcion = int(input("Ingresa una opción: ")) 

    if opcion == 1:
     
        lista_teclado = exa.teclado(lista_teclado)  
        print("Lista desde teclado:", lista_teclado)  

    elif opcion == 2:
    
        lista_aleatoria = exa.aleatoria(lista_aleatoria)  
        print("Lista aleatoria:", lista_aleatoria) 


    elif opcion == 3:
        lista_opcion = int(input("¿En cuál lista deseas buscar? (1 = teclado, 2 = aleatoria): "))  
        if lista_opcion == 1:
            elimina = exa.lineal(lista_teclado) 
            if elimina == -1:
                print("el numero no se encuentra en la lista")
            else:
                print(elimina)
                print("se imprimio la lista generada por el usuario")

        elif lista_opcion == 2:
            elimina = exa.lineal(lista_aleatoria) 
            if elimina == -1:
                print("el numero no se encuentra en la lista")
            else:
                print(elimina)
                print("se imprimio la lista generada por el usuario")
        else:
            print("Opción de lista no válida.")   

    elif opcion == 4:
        lista_opcion = int(input("¿En cuál lista deseas buscar? (1 = teclado, 2 = aleatoria): ")) 
        if lista_opcion == 1 and lista_teclado == exa.burbuja(lista_teclado):  
            cambia = exa.binaria(lista_teclado)  
            print(cambia)
            print("se immprimio la lista generada por el usuario")
        elif lista_opcion == 2 and lista_aleatoria == exa.burbuja(lista_aleatoria): 
            cambia = exa.binaria(lista_aleatoria)  
            print(cambia)
            print("se imprimio la lista generada aleatoriamente")
        else:
         print("opcion no valida")  

    elif opcion == 5:
    
        n = int(input("Ingresa un número entero para descomponer: "))  
        resultado = exa.descomponer_numero(n)  
        print("Número descompuesto en dígitos:", resultado)  

    elif opcion == 6:
        print("Saliendo del programa...")  
        break  

    else:
        print("Opción no válida. Por favor, elige entre 1 y 7.")  