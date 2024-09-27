import random
lista =[]
def aleatorio ():
    ele=int(input("dame el tamaño de la lista: "))
    minx=int(input("dame el numero minimo del aleatorio: "))
    maxx=int(input("dame el numero max del aleatorio: "))
    for i in range(ele):
        num=random.randint(minx,maxx)
        lista.append(num)
    print(lista)
    print(len(lista))

aleatorio()