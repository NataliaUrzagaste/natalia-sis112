lista =[8,2,3,45,7,93,10,37,90,11]
for i in range(len(lista)):
    for j in range(0,(len(lista)-i-1)):
        print (f"({lista[j]}, {lista[j+1]})")
        if (lista[j]>lista[j+1]):
            print(a)