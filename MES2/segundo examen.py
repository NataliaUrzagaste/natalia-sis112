import segundo as exa
lista_teclado = []  # Lista para almacenar números ingresados por teclado
lista_aleatoria = []  # Lista para almacenar números generados aleatoriamente

while True:  # Ciclo infinito que se rompe solo cuando el usuario elige salir
    exa.menu()  # Muestra el menú de opciones
    opcion = int(input("Ingresa una opción: "))  # Lee la opción elegida por el usuario

    if opcion == 1:
        # Opción 1: Genera lista con números únicos ingresados por el usuario
        lista_teclado = exa.teclado(lista_teclado)  # Llama a la función para generar la lista desde teclado
        print("Lista desde teclado:", lista_teclado)  # Muestra la lista generada

    elif opcion == 2:
        # Opción 2: Genera lista con números aleatorios únicos
        lista_aleatoria = exa.aleatoria(lista_aleatoria)  # Llama a la función para generar la lista aleatoria
        print("Lista aleatoria:", lista_aleatoria)  # Muestra la lista generada

    elif opcion == 3:
        # Opción 3: Ordena una de las listas seleccionadas
        lista_opcion = int(input("¿Cuál lista deseas ordenar? (1 = teclado, 2 = aleatoria): "))  # Solicita la lista a ordenar
        if lista_opcion == 1:
            lista_ordenada = exa.burbuja(lista_teclado)  # Ordena la lista desde teclado usando burbuja
            print("Lista desde teclado ordenada:", lista_ordenada)  # Muestra la lista ordenada
        elif lista_opcion == 2:
            lista_ordenada = exa.burbuja(lista_aleatoria)  # Ordena la lista aleatoria usando burbuja
            print("Lista aleatoria ordenada:", lista_ordenada)  # Muestra la lista ordenada
        else:
            print("Opción de lista no válida.")  # Si la opción no es válida, muestra un mensaje de error

    elif opcion == 4:
        # Opción 4: Realiza una búsqueda lineal en una lista seleccionada
        lista_opcion = int(input("¿En cuál lista deseas buscar? (1 = teclado, 2 = aleatoria): "))  # Solicita la lista para buscar
        if lista_opcion == 1:
            elimina = exa.lineal(lista_teclado)  # Llama a la función de búsqueda lineal en la lista desde teclado
        elif lista_opcion == 2:
            elimina = exa.lineal(lista_aleatoria)  # Llama a la función de búsqueda lineal en la lista aleatoria
        else:
            print("Opción de lista no válida.")  # Si la opción no es válida, muestra un mensaje de error
            continue
        print("Resultado de búsqueda lineal:", elimina)  # Muestra el resultado de la búsqueda lineal

    elif opcion == 5:
        # Opción 5: Realiza una búsqueda binaria en una lista ordenada
        lista_opcion = int(input("¿En cuál lista deseas buscar? (1 = teclado, 2 = aleatoria): "))  # Solicita la lista para buscar
        if lista_opcion == 1 and lista_teclado == sorted(lista_teclado):  # Asegura que la lista esté ordenada
            cambia = exa.binaria(lista_teclado)  # Llama a la función de búsqueda binaria en la lista desde teclado
        elif lista_opcion == 2 and lista_aleatoria == sorted(lista_aleatoria):  # Asegura que la lista esté ordenada
            cambia = exa.binaria(lista_aleatoria)  # Llama a la función de búsqueda binaria en la lista aleatoria
        else:
            print("La lista seleccionada no está ordenada. Ordénala antes de realizar una búsqueda binaria.")  # Muestra mensaje si no está ordenada
            continue
        print("Resultado de búsqueda binaria:", cambia)  # Muestra el resultado de la búsqueda binaria

    elif opcion == 6:
        # Opción 6: Descompone un número en dígitos
        n = int(input("Ingresa un número entero para descomponer: "))  # Solicita el número a descomponer
        resultado = exa.descomponer_numero(n)  # Llama a la función para descomponer el número en dígitos
        print("Número descompuesto en dígitos:", resultado)  # Muestra el número descompuesto en dígitos

    elif opcion == 7:
        print("Saliendo del programa...")  # Muestra un mensaje de despedida
        break  # Sale del ciclo y termina el programa

    else:
        print("Opción no válida. Por favor, elige entre 1 y 7.")  # Si la opción no es válida, muestra un mensaje de error