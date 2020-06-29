from tkinter import *
import funciones_calc
# creacion de raiz para el frame principal
raiz = Tk()
raiz.title("Calculadora")

miFrame = Frame(raiz, width = 220, height = 220)
miFrame.pack()

# variable para cambio de operacion
operacion = ""
# variable para el resultado
resultado = 0.0
# variable para contar
contador = 0

# ----------------------- PANTALLA-------------------------------------------
# Variable para aceptar numero en pantalla
numerosPantalla = StringVar()

pantalla = Entry(miFrame,textvariable = numerosPantalla)
# las funciones "columnspan o rowspan" sirven en el caso usemos grid en lugar
# de place para decir cuantas columnas o filas ocuparemos sin descuadrar 
pantalla.grid(row = 1, column=1, padx = 10, pady = 10)
pantalla.config(background = "black", fg = "white", justify = "right")
pantalla.place(x=10, y=10, height=30, width=200)
# el objeto que llamara a mi clase con los numeros en cada instancia
# y el objeto que realizara las operaciones
numerosPantalla.set("0.")
objeto = funciones_calc.PresionarCalculadora()

# ------------------------ PULSACIONES TECLADO ------------------------------
def numero_pulsado(num):
    global operacion

    if numerosPantalla.get() == "0." and operacion =="":
        numerosPantalla.set(num)
    elif operacion !="":
        numerosPantalla.set(num)
        operacion = ""
    else:
        numerosPantalla.set(numerosPantalla.get() + num)


# ----------------------------- FUNCION SUMA -------------------------------
def suma(num):
    global operacion
    global resultado

    resultado += float(num)  
    operacion = "suma"
    numerosPantalla.set(resultado)

# ----------------------------- FUCION RESTA ------------------------------
def resta(num):
    global operacion
    global resultado
    global contador

    if numerosPantalla.get() == "0.":
        pass
    elif len(numerosPantalla.get()) == 0:
        pass
    else:
        if contador == 0:
            resultado = float(numerosPantalla.get())
            numerosPantalla.set(resultado)
            operacion = "resta"
            contador = 1
        else:
            resultado -= float(num)  
            numerosPantalla.set(resultado)
            operacion = "resta"

# -------------------------- FUCION PRODUCTO ----------------------------
def producto(num):
    global operacion
    global resultado
    global contador

    if numerosPantalla.get() == "0.":
        pass
    elif len(numerosPantalla.get()) == 0:
        pass
    else:
        if contador == 0:
            resultado = float(numerosPantalla.get())
            numerosPantalla.set(resultado)
            operacion = "MULTIPLICAION"
            contador = 1
        else:
            resultado *= float(num)  
            numerosPantalla.set(resultado)
            operacion = "resta"

# --------------------------- FUCION DIVISION -----------------------------
def division(num):
    global operacion
    global resultado
    global contador

    if numerosPantalla.get() == "0.":
        pass
    elif len(numerosPantalla.get()) == 0:
        pass
    elif contador == 1 and (numerosPantalla.get() == "0" or numerosPantalla.get() == "0."):
        numerosPantalla.set("ERROR")
    else:
        if contador == 0:
            resultado = float(numerosPantalla.get())
            numerosPantalla.set(resultado)
            operacion = "division"
            contador = 1
        else:
            resultado /= float(num)  
            numerosPantalla.set(resultado)
            operacion = "division"
        

#------------------------ Fila1 ---------------------------------------------
botonBorrar = Button(miFrame, text = "CE", width = 3)
# por si queremos usar grid
#boton7.grid(row = 5, column = 1)
botonBorrar.place(x=10, y=45, height=30, width=50) 
botonPot    = Button(miFrame, text = "C", width = 3)
botonPot.place(x=65, y=45, height=30, width=50) 
botonRaiz   = Button(miFrame, text = "<-", width = 3,
    command = lambda:funciones_calc.PresionarCalculadora.pushbuttonR(objeto, numerosPantalla))
botonRaiz.place(x=120, y=45, height=30, width=50)
# command = lambda:funciones_calc.PresionarCalculadora.pushbuttonR(objeto,numerosPantalla)

# division
botonDiv    = Button(miFrame, text = "➗", width = 3,
    command = lambda : division(numerosPantalla.get()))
botonDiv.place(x=175, y=45, height=30, width=35)

#------------------------ Fila2 ---------------------------------------------
# numero 7
boton7      = Button(miFrame, text = "7", width = 3, 
    command = lambda:numero_pulsado("7"))
boton7.place(x=10, y=80, height=30, width=50) 

# numero 8
boton8      = Button(miFrame, text = "8", width = 3, 
    command = lambda:numero_pulsado("8"))
boton8.place(x=65, y=80, height=30, width=50)

# Numero 9
boton9      = Button(miFrame, text = "9", width = 3, 
    command = lambda:numero_pulsado("9"))
boton9.place(x=120, y=80, height=30, width=50)

# Multiplicacion
botonProd   = Button(miFrame, text = "*", width = 3,
    command = lambda : producto(numerosPantalla.get()))
botonProd.place(x=175, y=80, height=30, width=35)

#------------------------ Fila3 ---------------------------------------------
# Numero 4

boton4      = Button(miFrame, text = "4", width = 3, 
    command = lambda:numero_pulsado("4"))
boton4.place(x=10, y=115, height=30, width=50)

# Numero 5
boton5      = Button(miFrame, text = "5", width = 3, 
    command = lambda:numero_pulsado("5"))
boton5.place(x=65, y=115, height=30, width=50) 

# Numero 6
boton6      = Button(miFrame, text = "6", width = 3, 
    command = lambda:numero_pulsado("6"))
boton6.place(x=120, y=115, height=30, width=50)

# Resta
botonresta  = Button(miFrame, text = "-", width = 3,
    command=lambda: resta(numerosPantalla.get()))
botonresta.place(x=175, y=115, height=30, width=35)

#------------------------ Fila4 ---------------------------------------------
# numero 1
boton1      = Button(miFrame, text = "1", width = 3, 
    command = lambda:numero_pulsado("1"))
boton1.place(x=10, y=150, height=30, width=50) 

# numero 2
boton2      = Button(miFrame, text = "2", width = 3, 
    command = lambda:numero_pulsado("2"))
boton2.place(x=65, y=150, height=30, width=50) 

# numero 3
boton3      = Button(miFrame, text = "3", width = 3, 
    command = lambda:numero_pulsado("3"))
boton3.place(x=120, y=150, height=30, width=50)

# suma
botonsuma   = Button(miFrame, text = "+", width = 3,
    command = lambda:suma(numerosPantalla.get()))
botonsuma.place(x=175, y=150, height=30, width=35)

#------------------------ Fila5 ---------------------------------------------
boton1      = Button(miFrame, text = "0", width = 3,
    command = lambda:funciones_calc.PresionarCalculadora.pushbutton0(objeto, numerosPantalla))
boton1.place(x=10, y=185, height=30, width=50) 
boton2      = Button(miFrame, text = ".", width = 3,
    command = lambda:funciones_calc.PresionarCalculadora.pushbuttonP(objeto, numerosPantalla))
boton2.place(x=65, y=185, height=30, width=50) 
boton3      = Button(miFrame, text = "%", width = 3)
boton3.place(x=120, y=185, height=30, width=50)

# boton igual
botonigual  = Button(miFrame, text = "=", width = 3)
botonigual.place(x=175, y=185, height=30, width=35)

# Final del codigo
raiz.mainloop()