import conver

print("1) para metros a kilometros")
print("2) para gramos a kilogramos")
print("3) para celsios a farenheit")
print("4) para kilometros a metros")
print("5) para kilogramos a gramos")
print("6) para farenheit a celsius")

opcion = int(input("¿Qué opción necesitas? "))
cant = float(input("Ingresa la cantidad a convertir: "))

if opcion == 1:
    print(f"Resultado: {conver.metroskilometros(cant):.5f} kilómetros")
elif opcion == 2:
    print(f"Resultado: {conver.gramoskilogramos(cant):.5f} kilogramos")
elif opcion == 3:
    print(f"Resultado: {conver.celciusaferenheit(cant):.5f} °F")
elif opcion == 4:
    print(f"Resultado: {conver.kilometrosmetros(cant):.5f} metros")
elif opcion == 5:
    print(f"Resultado: {conver.kilogramogramo(cant):.5f} gramos")
elif opcion == 6:
    print(f"Resultado: {conver.ferenheitcelsius(cant):.5f} °C")
else:
    print("Ingresa una opción válida.")
