#ejercicio uno
print("Hello, World")

# condicionales
#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    if n % 2 != 0:
        print("Weird")
    elif n % 2 == 0 and 2 <= n <= 5:
        print("Not Weird")
    elif n % 2 == 0 and 6 <= n <= 20:
        print("Weird")
    else:
        print("Not Weird")


#stdin
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a + b)
    print(a - b)
    print(a * b)
    
#division
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    div= a//b
    div2= a/b
    print(div)
    print(div2)

#loop
if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        if i<n:
            
           print(i*i)

# año bisisesto
def is_leap(year):
    leap = False
    
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                leap = True
            else:
                leap = False
        else:
            leap = True
    else:
        leap = False
    
    return leap

year = int(input())
print(is_leap(year))

#metodods
if __name__ == '__main__':
    n = int(input())
    for i in range(1, n+1):
        print(i, end="")