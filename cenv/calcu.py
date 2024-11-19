# importar de las librerías necesarias para la interfaz gráfica y operaciones matemáticas
from tkinter import *
from tkinter import ttk
import math

#ingresar valores o signos en la pantalla
def ingresarval(tecla):
    if tecla in '0123456789.()':  # si la tecla es un número, punto o paréntesis
        entrada2.set(entrada2.get() + tecla)  # el valor a la entrada de la pantalla
    elif tecla in '*/+-':  # si la tecla es un signo
        # si el último carácter no es un signo, agregar el nuevo signo
        if entrada2.get() and entrada2.get()[-1] not in '*/+-':
            entrada2.set(entrada2.get() + tecla)  # agregar el signo
    elif tecla == '=':  # si la tecla es igual, evaluamos la expresión
        try:
            # evalua la expresión completa respetando la jerarquía de signos
            resultado = eval(entrada2.get())  # usa eval() para evaluar la expresión matemática
            entrada1.set(entrada2.get())  # mostrar la expresión ingresada en la parte superior
            entrada2.set(resultado)  # mostrar el resultado en la pantalla inferior
        except Exception as e:  # si ocurre un error 
            entrada2.set("Error")  # mostrar "Error" en la pantalla
    elif tecla == '(':  # si la tecla es un paréntesis abierto
        # abrir paréntesis solo si está al inicio o después de un operador
        if not entrada2.get() or entrada2.get()[-1] in '*/+-(':
            entrada2.set(entrada2.get() + '(')  # agregar el paréntesis abierto
    elif tecla == ')':  # si la tecla es un paréntesis cerrado
        # solo cerrar paréntesis si hay un número antes y los paréntesis están balanceados
        if (entrada2.get().count('(') > entrada2.get().count(')') and 
            entrada2.get() and entrada2.get()[-1] not in '*/+-('):
            entrada2.set(entrada2.get() + ')')  # agregar el paréntesis cerrado

# calcular la raíz cuadrada del número ingresado
def raizcuadrada():
    entrada1.set('')  # limpiar la parte superior de la pantalla
    resultado = math.sqrt(float(entrada2.get()))  # calcula la raíz cuadrada
    entrada2.set(resultado)  # muestra el resultado de la raíz cuadrada en la pantalla

# borrar el último carácter ingresado
def borrar():
    if entrada2.get():  # verifica que haya algo en la entrada antes de intentar borrar
        entrada2.set(entrada2.get()[:-1])  # elimina el último carácter de la entrada

# borrar toda la entrada
def borrartodo():
    entrada1.set('')  # limpiar la parte superior de la pantalla
    entrada2.set('')  # limpiar la pantalla de resultados

#crear la ventana principal
root = Tk()
root.title("Calculadora :3")  # título de la ventana
root.geometry("+500+80")  # posición de la ventana en la pantalla
root.columnconfigure(0, weight=1)  # configura la columna 0 con peso 1 
root.rowconfigure(0, weight=1)  # configura la fila 0 con peso 1 
root.configure(bg="#F4C2C2")  # establecer el color de fondo de la ventana

# crear el marco principal para contener los botones y la pantalla
mainframe = Frame(root, bg="#F4C2C2")
mainframe.grid(column=0, row=0, sticky=(W, N, E, S))  # configuración de la cuadrícula
mainframe.columnconfigure(0, weight=1)  # configura las columnas del marco para que se ajusten
mainframe.columnconfigure(1, weight=1)
mainframe.columnconfigure(2, weight=1)
mainframe.columnconfigure(3, weight=1)

# configurar las filas
mainframe.rowconfigure(0, weight=1)
mainframe.rowconfigure(1, weight=1)
mainframe.rowconfigure(2, weight=1)
mainframe.rowconfigure(3, weight=1)
mainframe.rowconfigure(4, weight=1)
mainframe.rowconfigure(5, weight=1)
mainframe.rowconfigure(6, weight=1)
mainframe.rowconfigure(7, weight=1)

# los estilos para los botones
estilos = ttk.Style()

# para los botones de números
estilos.configure(
    'numeros.TButton',
    font=("Arial", 22),
    width=5,
    foreground="#4A4A4A",  # color del texto en estado normal
)
estilos.map(
    'numeros.TButton',
    foreground=[('active', '#FF8C69')],  # Cambia el color del texto cuando esta activo
    background=[('active', '#FFF0F5')]  # Cambia el color de fondo cuando esta activo
)

# los botones de borrar
estilos.configure(
    'borrar.TButton',
    font=("Arial", 22),
    width=5,
    foreground="#4A4A4A",  # color del texto en estado normal
)
estilos.map(
    'borrar.TButton',
    foreground=[('active', '#A52A52')],  # cambia el color del texto cuando esta activo
    background=[('active', '#B03060')]  # cambia el color de fondo cuando esta activo
)

#los botones de operadores
estilos.configure(
    'restantes.TButton',
    font=("Arial", 22),
    width=5,
    foreground="#FF1493",  # color del texto en estado normal
)
estilos.map(
    'restantes.TButton',
    foreground=[('active', '#FF8C69')],  # cambia el color del texto cuando está activo
    background=[('active', '#F2D9E6')]  # cambia el color de fondo cuando está activo
)

# variables de entrada
entrada1 = StringVar()  # variable para mostrar la expresión en la parte superior de la pantalla
label_entrada1 = ttk.Label(
    mainframe, textvariable=entrada1, font=("Arial", 15), anchor="e", background="#F4C2C2", foreground="#4A4A4A"
)
label_entrada1.grid(column=0, row=0, columnspan=4, sticky=(W, N, E, S))  # colocar la etiqueta en la pantalla

entrada2 = StringVar()  # variable para mostrar los resultados en la parte inferior de la pantalla
label_entrada2 = ttk.Label(
    mainframe, textvariable=entrada2, font=("Arial", 40), anchor="e", background="#F4C2C2", foreground="#4A4A4A"
)
label_entrada2.grid(column=0, row=1, columnspan=4, sticky=(W, N, E, S))  # colocar la etiqueta en la pantalla

# crear los botones con sus estilos y asignarles la acción correspondiente
button0 = ttk.Button(mainframe, text="0", style="numeros.TButton", command=lambda: ingresarval('0'))
button1 = ttk.Button(mainframe, text="1", style="numeros.TButton", command=lambda: ingresarval('1'))
button2 = ttk.Button(mainframe, text="2", style="numeros.TButton", command=lambda: ingresarval('2'))
button3 = ttk.Button(mainframe, text="3", style="numeros.TButton", command=lambda: ingresarval('3'))
button4 = ttk.Button(mainframe, text="4", style="numeros.TButton", command=lambda: ingresarval('4'))
button5 = ttk.Button(mainframe, text="5", style="numeros.TButton", command=lambda: ingresarval('5'))
button6 = ttk.Button(mainframe, text="6", style="numeros.TButton", command=lambda: ingresarval('6'))
button7 = ttk.Button(mainframe, text="7", style="numeros.TButton", command=lambda: ingresarval('7'))
button8 = ttk.Button(mainframe, text="8", style="numeros.TButton", command=lambda: ingresarval('8'))
button9 = ttk.Button(mainframe, text="9", style="numeros.TButton", command=lambda: ingresarval('9'))

button_borrar = ttk.Button(mainframe, text=chr(9003), style="borrar.TButton", command=borrar)  # símbolo de borrar
button_borrartodo = ttk.Button(mainframe, text="C", style="borrar.TButton", command=borrartodo)
button_parentesisabre = ttk.Button(mainframe, text="(", style="restantes.TButton", command=lambda: ingresarval('('))
button_parentesiscierra = ttk.Button(mainframe, text=")", style="restantes.TButton", command=lambda: ingresarval(')'))
button_punto = ttk.Button(mainframe, text=".", style="restantes.TButton", command=lambda: ingresarval('.'))

button_division = ttk.Button(mainframe, text=chr(247), style="restantes.TButton", command=lambda: ingresarval('/'))  # sivisión
button_multiplicacion = ttk.Button(mainframe, text="x", style="restantes.TButton", command=lambda: ingresarval('*'))
button_resta = ttk.Button(mainframe, text="-", style="restantes.TButton", command=lambda: ingresarval('-'))
button_suma = ttk.Button(mainframe, text="+", style="restantes.TButton", command=lambda: ingresarval('+'))

button_igual = ttk.Button(mainframe, text="=", style="restantes.TButton", command=lambda: ingresarval('='))
button_raizcuadrada = ttk.Button(mainframe, text="√", style="restantes.TButton", command=raizcuadrada)

# colocar los botones en el grid
button_parentesisabre.grid(column=0, row=2, sticky=(W, N, E, S))
button_parentesiscierra.grid(column=1, row=2, sticky=(W, N, E, S))
button_borrartodo.grid(column=2, row=2, sticky=(W, N, E, S))
button_borrar.grid(column=3, row=2, sticky=(W, N, E, S))
button7.grid(column=0, row=3, sticky=(W, N, E, S))
button8.grid(column=1, row=3, sticky=(W, N, E, S))
button9.grid(column=2, row=3, sticky=(W, N, E, S))
button_division.grid(column=3, row=3, sticky=(W, N, E, S))
button4.grid(column=0, row=4, sticky=(W, N, E, S))
button5.grid(column=1, row=4, sticky=(W, N, E, S))
button6.grid(column=2, row=4, sticky=(W, N, E, S))
button_multiplicacion.grid(column=3, row=4, sticky=(W, N, E, S))
button1.grid(column=0, row=5, sticky=(W, N, E, S))
button2.grid(column=1, row=5, sticky=(W, N, E, S))
button3.grid(column=2, row=5, sticky=(W, N, E, S))
button_suma.grid(column=3, row=5, sticky=(W, N, E, S))
button0.grid(column=0, row=6, columnspan=2, sticky=(W, N, E, S))
button_punto.grid(column=2, row=6, sticky=(W, N, E, S))
button_resta.grid(column=3, row=6, sticky=(W, N, E, S))
button_igual.grid(column=0, row=7, columnspan=3, sticky=(W, N, E, S))
button_raizcuadrada.grid(column=3, row=7, sticky=(W, N, E, S))

# configurar el espacio entre los botones
for child in mainframe.winfo_children():
    child.grid_configure(ipady=10, padx=1, pady=1)

# bucle principal para que la interfaz gráfica esté en ejecución
root.mainloop()
