# aqui se pondran las funciones del teclado y se enviaran
# a la pantalla que tenemos en el disenyo
from tkinter import *

class PresionarCalculadora():

    def __init__(self):
        self.operacion  = ""
        self.resultado  = 0.0
        self.contador   = 0
        # propiedades
        self.__boton0   = "0"
        self.__botonP   = "."

    # ------------------------- numeros 0 y Punto --------------------------------
    def pushbutton0(self, presionarboton):
        # Primero comprueba si esta vacio el campo
        if len(presionarboton.get()) == 2 and presionarboton.get() == "0.":
            pass
        else:
            presionarboton.set(presionarboton.get() + self.__boton0)

    
    def pushbuttonP(self, presionarboton):
        # Primero comprueba si esta vacio el campo
        if len(presionarboton.get()) == 2 and presionarboton.get() == "0.":
            presionarboton.set("0" + self.__botonP)
            contador = 1
        else:
            texto = str()
            texto = presionarboton.get()
            for i in texto:
                if i == "." and contador == 1:
                    pass
                else:
                    presionarboton.set(presionarboton.get() + self.__botonP)
                    contador = 1
    
    #------------------------------ botones borrar -----------------------------
    # borrar caracter por caracter
    def pushbuttonR(self, presionarboton):
        if len(presionarboton.get()) == 0:
            pass
        else:
            texto1 = str()
            texto1 = presionarboton.get()
            
            texto2 = []
            texto2 = list(texto1)
            texto2.pop()

            textoS = "".join(texto2)
            
            presionarboton.set(textoS)
    '''
    def pushbuttonB(self, presionarboton):
        objOp = operaciones_calc.OperacionesNumericas()
        valor = True
        operaciones_calc.OperacionesNumericas.funcion_limpiar(objOp,valor,presionarboton)
        presionarboton.set("0.")
    
    def pushbuttonL(self, presionarboton):
        presionarboton.set("0.")

'''