from tkinter import *  # Importa todo de tkinter (para la interfaz gráfica)
from tkinter import ttk  # Importa ttk, el cual proporciona widgets con un estilo mejorado
import math  # Importa el módulo math para realizar cálculos matemáticos si es necesario

# Crea la ventana principal
root = Tk()
root.title("Calculadora :3")  # Establece el título de la ventana
root.geometry("+500+80")  # Establece la posición inicial de la ventana en la pantalla

# Configura el fondo de la ventana principal
root.configure(bg="#F4C2C2")

# Crea un marco (frame) donde se agregarán los widgets (botones, etiquetas, etc.)
mainframe = Frame(root, bg="#F4C2C2")
mainframe.grid(column=0, row=0)  # Coloca el frame en la ventana

# Establece los estilos de los botones mediante ttk.Style()
estilos = ttk.Style()

# Estilo para los botones de números
estilos.configure(
    'numeros.TButton',  # Nombre del estilo
    font=("Arial", 22),  # Tipo de letra y tamaño
    width=5,  # Ancho de cada botón
    background="#F2D9E6",  # Color de fondo del botón (esto no aplica directamente a ttk, será manejado por el tema)
    foreground="#4A4A4A",  # Color del texto del botón
    relief="flat"  # Establece el estilo de borde (sin relieve)
)

# Estilo para los botones de borrar
estilos.configure(
    'borrar.TButton',
    font=("Arial", 22),
    width=5,
    foreground="#FFFFFF",  # Color del texto
    background="#FF6F61",  # Color de fondo
    relief="flat"
)

# Estilo para los botones restantes (operadores, etc.)
estilos.configure(
    'restantes.TButton',
    font=("Arial", 22),
    width=5,
    foreground="#333333",  # Color del texto
    relief="flat"  # Estilo sin relieve
)

# Map para cambiar el color cuando el botón está en estado activo (presionado)
estilos.map(
    'borrar.TButton',
    background=[('active', '#FF8C69')],  # Color de fondo cuando el botón es presionado
    foreground=[('active', '#FFFFFF')]   # Color del texto cuando el botón es presionado
)

# Crear y colocar los labels de entrada, donde se mostrará la expresión y el resultado
entrada1 = StringVar()  # Variable vinculada a la primera entrada
label_entrada1 = ttk.Label(
    mainframe, textvariable=entrada1, font=("Arial", 15), anchor="e", background="#F4C2C2", foreground="#4A4A4A"
)
label_entrada1.grid(column=0, row=0, columnspan=4, sticky=(W, E))

entrada2 = StringVar()  # Variable vinculada a la segunda entrada
label_entrada2 = ttk.Label(
    mainframe, textvariable=entrada2, font=("Arial", 40), anchor="e", background="#F4C2C2", foreground="#4A4A4A"
)
label_entrada2.grid(column=0, row=1, columnspan=4, sticky=(W, E))

# Crear los botones con los estilos definidos anteriormente
button0 = ttk.Button(mainframe, text="0", style="numeros.TButton")
button1 = ttk.Button(mainframe, text="1", style="numeros.TButton")
button2 = ttk.Button(mainframe, text="2", style="numeros.TButton")
button3 = ttk.Button(mainframe, text="3", style="numeros.TButton")
button4 = ttk.Button(mainframe, text="4", style="numeros.TButton")
button5 = ttk.Button(mainframe, text="5", style="numeros.TButton")
button6 = ttk.Button(mainframe, text="6", style="numeros.TButton")
button7 = ttk.Button(mainframe, text="7", style="numeros.TButton")
button8 = ttk.Button(mainframe, text="8", style="numeros.TButton")
button9 = ttk.Button(mainframe, text="9", style="numeros.TButton")

button_borrar = ttk.Button(mainframe, text=chr(9003), style="borrar.TButton")  # Usando el símbolo de borrar
button_borrartodo = ttk.Button(mainframe, text="C", style="borrar.TButton")  # Botón de borrar todo
button_patentesisabre = ttk.Button(mainframe, text="(", style="restantes.TButton")
button_parentesiscierra = ttk.Button(mainframe, text=")", style="restantes.TButton")
button_punto = ttk.Button(mainframe, text=".", style="restantes.TButton")

button_division = ttk.Button(mainframe, text=chr(247), style="restantes.TButton")  # Símbolo de división
button_multiplicacion = ttk.Button(mainframe, text="x", style="restantes.TButton")
button_resta = ttk.Button(mainframe, text="-", style="restantes.TButton")
button_suma = ttk.Button(mainframe, text="+", style="restantes.TButton")

button_igual = ttk.Button(mainframe, text="=", style="restantes.TButton")
button_raizcuadrada = ttk.Button(mainframe, text="√", style="restantes.TButton")

# Colocar los botones en el grid de la interfaz
button_patentesisabre.grid(column=0, row=2)
button_parentesiscierra.grid(column=1, row=2)
button_borrartodo.grid(column=2, row=2)
button_borrar.grid(column=3, row=2)

button7.grid(column=0, row=3)
button8.grid(column=1, row=3)
button9.grid(column=2, row=3)
button_division.grid(column=3, row=3)

button4.grid(column=0, row=4)
button5.grid(column=1, row=4)
button6.grid(column=2, row=4)
button_multiplicacion.grid(column=3, row=4)

button1.grid(column=0, row=5)
button2.grid(column=1, row=5)
button3.grid(column=2, row=5)
button_suma.grid(column=3, row=5)

button0.grid(column=0, row=6, columnspan=2, sticky=(W, E))  # Botón 0 ocupa dos columnas
button_punto.grid(column=2, row=6)
button_resta.grid(column=3, row=6)

button_igual.grid(column=0, row=7, columnspan=3, sticky=(W, E))  # Botón igual ocupa tres columnas
button_raizcuadrada.grid(column=3, row=7)

# Aplica configuración de espacio (relleno) a todos los widgets dentro de mainframe
for child in mainframe.winfo_children():
    child.grid_configure(ipady=10, padx=1, pady=1)  # Esto agrega un poco de espacio dentro y alrededor de cada botón

# Inicia el bucle principal de la interfaz gráfica (espera eventos)
root.mainloop()
