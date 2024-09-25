"""Desarrolla un programa en Python que simule un sistema de gestión de notas para una clase. El programa debe permitir agregar notas, 
calcular el promedio, obtener la nota máxima y la nota mínima, y mostrar todas las notas."""

import retroalimentacion

while True:
    print("\n gestión de notas:")
    print("1. agregar notas")
    print("2. mostrar notas")
    print("3. promedio")
    print("4. elimina una nota")
    print("5. cambia una nota")
    print("6. máxima y mínima nota")
    print("7. salir")
    opcion = input("Elige una opción (1-7): ")

    if opcion == '1':
        #ingresa notas
        ingresar=retroalimentacion.ingresar_notas()
        print(ingresar)

    elif opcion == '2':
        #muestar nota
        mostrar=retroalimentacion.mostrar_notas()
        print(mostrar)

    elif opcion == '3':
        #para promediar
        prom=retroalimentacion.calcular_promedio()
        print(prom)

    elif opcion == '4':
        #pata la mayor y menor
        elimina=retroalimentacion.borrar_notas()
        print(elimina)

    elif opcion == '5':
        #pata la mayor y menor
        cambia=retroalimentacion.cam_nota()
        print(cambia)

    elif opcion == '6':
        #pata la mayor y menor
        maxymin=retroalimentacion.maximo_minimo()
        print(maxymin)

    elif opcion == '7':
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Por favor, elige entre 1 y 5.")