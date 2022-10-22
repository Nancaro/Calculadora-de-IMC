#Crear un programa que calcule el IMC (Indice de masa corporal) se mide haciendo la division de el peso de una persona y la altura al cuadrado.
#Hecho por Bruno Aguirre-Nancaro

import string
from tkinter import *
from tkinter import Label
from typing import Tuple
import tkinter as tk



class Application: 
    imcValue: Label
    font1: tuple[str, str]
    
    def __init__(self, master=None):
        self.font1 =("arial"),("12")

        self.space1 = Frame(master)
        self.space1['pady'] = 10
        self.space1.pack()

        self.space2 = Frame(master)
        self.space2['padx'] = 20
        self.space2.pack()

        self.space3 = Frame(master)
        self.space3['padx'] = 20
        self.space3.pack()

        self.space4 = Frame(master)
        self.space4['padx'] = 20
        self.space4.pack()

        self.space5 = Frame(master)
        self.space5['padx'] = 20
        self.space5.pack()

        self.space6 = Frame(master)
        self.space6['padx'] = 20
        self.space6.pack()

        self.name = Label(self.space1,text="Calculadora IMC: ", font=self.font1)
        self.name["font"] = ("Arial", "10", "bold")
        self.name.pack()

        self.numberLabel = Label(self.space2, text="Peso", font=self.font1)
        self.numberLabel.pack(side=LEFT)

        self.number = Entry(self.space2)
        self.number["width"] = 30
        self.number["font"] = self.font1
        self.number.pack(side=LEFT)

        self.number2Label = Label(self.space3, text="Altura", font=self.font1)
        self.number2Label.pack(side=LEFT)

        self.number2 = Entry(self.space3)
        self.number2["width"] = 30
        self.number2["font"] = self.font1
        self.number2.pack(side=LEFT)

        # Ajuste de la caja de texto "IMC"
        self.IMCValue = Label(self.space4, text="IMC", font=self.font1)
        self.IMCValue.pack(side=LEFT)

        self.imcValue = Label(self.space5, text="", font=self.font1)
        self.imcValue.pack(side=RIGHT)

        # Ajuste del botón
        self.calcular = Button(self.space6)
        self.calcular["text"] = "CALCULAR"
        self.calcular["font"] = ("Calibri", "8")
        self.calcular["width"] = 12
        self.calcular["command"] = self.Calculadora
        self.calcular.pack()


 #Calculador
    def Calculadora(self):
        peso = self.number.get()
        altura = self.number2.get()

        resp = (float(peso)) / (float(altura) * float(altura))

        if resp < 17:
            self.imcValue["text"] = resp, 'Muy bajo de peso'
        elif resp < 18.49:
            self.imcValue["text"] = resp, 'Bajo de peso'
        elif resp < 24.99:
            self.imcValue["text"] = resp, 'Peso normal'
        elif resp < 29.99:
            self.imcValue["text"] = resp, 'Encima de peso'
        elif resp < 34.99:
            self.imcValue["text"] = resp, 'Obesidad grado 1'
        elif resp < 39.99:
            self.imcValue["text"] = resp, 'Obesidad grado 2'
        else:
            self.imcValue ["text"] = resp, 'Obesidad grado 3'

root = Tk()
root.title('Calculadora de IMC- Bruno Aguirre-Nancaro')
Application(root)
root.mainloop()