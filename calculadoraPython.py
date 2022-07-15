from __future__ import division
from codecs import BufferedIncrementalEncoder
from textwrap import fill
from tkinter import *
from tkinter.tix import DisplayStyle
from turtle import right

raiz=Tk()
raiz.title("Basic Calculator")

miFrame=Frame(raiz)
miFrame.pack()#fill='both', expand=False
miFrame.config(cursor='hand2')
operacion=""
resetPantalla=False
resultado=0

#---------------pantalla-----------------
#-----------------fila1------------------
numeroPantalla=StringVar()
pantalla=Entry(miFrame,textvariable=numeroPantalla)
pantalla.grid(row=1,column=1,padx=5,pady=5,columnspan=4)
pantalla.config(bg="black",fg="#03f943",justify="right")#03f943

#---------------pulsacionesPantalla-----------------

def numeroPulsado(num):
    global operacion
    global resetPantalla

    if resetPantalla!=False:
        numeroPantalla.set(num)
        resetPantalla=False
    else:
        numeroPantalla.set(numeroPantalla.get()+num)
   
#---------------funcionSuma-----------------
def suma(num):
    global operacion
    global resultado
    global resetPantalla

    resultado+=int(num)#float
    operacion="suma"
    resetPantalla=True

    numeroPantalla.set(resultado)

#---------------funcionResta-----------------
num1=0
contador_resta=0

def resta(num):
    global operacion
    global resultado
    global num1
    global contador_resta
    global resetPantalla

    if contador_resta==0:
        num1=int(num)
        resultado=num1
    else:
        if contador_resta==1:
            resultado=num1-int(num)
        else:
            resultado=int(resultado)-int(num)

        numeroPantalla.set(resultado)
        resultado=numeroPantalla.get()
    
    contador_resta=contador_resta+1
    operacion="resta"
    resetPantalla=True
    
#---------------funcionMultiplica-----------------
contador_multiplica=0

def multiplica(num):
    global operacion
    global resultado
    global num1
    global contador_multiplica
    global resetPantalla

    if contador_multiplica==0:
        num1=int(num)
        resultado=num1
    else:
        if contador_multiplica==1:
            resultado=num1*int(num)
        else:
            resultado=int(resultado)*int(num)

        numeroPantalla.set(resultado)
        resultado=numeroPantalla.get()
    
    contador_multiplica=contador_multiplica+1
    operacion="multiplica"
    resetPantalla=True

#---------------funcionDivision-----------------
contador_division=0

def divide (num):
    global operacion
    global resultado
    global num1
    global contador_division
    global resetPantalla

    if contador_division==0:
        num1=int(num)
        resultado=num1
    else:
        if contador_division==1:
            resultado=num1/int(num)
        else:
            resultado=int(resultado)/int(num)

        numeroPantalla.set(resultado)
        resultado=numeroPantalla.get()
    
    contador_division=contador_division+1
    operacion="division"
    resetPantalla=True

#---------------funcionBorrarTodo-----------------
def borrar():
    DisplayStyle.delete(0,END)
    #numeroPantalla.set=0
    #resultado=0

#---------------funcionTotal-----------------

def total():
    global resultado
    global operacion
    global contador_resta
    global contador_multiplica
    global contador_division

    if operacion=="suma":
        numeroPantalla.set(resultado+int(numeroPantalla.get()))
        resultado=0
    elif operacion=="resta":
        numeroPantalla.set(int(resultado)-int(numeroPantalla.get()))
        resultado=0
    elif operacion=="multiplica":
        numeroPantalla.set(int(resultado)*int(numeroPantalla.get()))
        resultado=0
    elif operacion=="division":
        numeroPantalla.set(int(resultado)/int(numeroPantalla.get()))
        resultado=0
    

#---------------fila2-----------------
botonClear=Button(miFrame,text="C",width=3,command=lambda:borrar())
botonClear.grid(row=2,column=1)
botonDiv=Button(miFrame,text="÷",width=3,command=lambda:divide(numeroPantalla.get()))
botonDiv.grid(row=2,column=2)
botonMult=Button(miFrame,text="X",width=3,command=lambda:multiplica(numeroPantalla.get()))
botonMult.grid(row=2,column=3)
botonBorrar=Button(miFrame,text="⇦",width=3)
botonBorrar.grid(row=2,column=4)

#---------------fila3-----------------
#OTRA OPCIÓN command=lambad:numeroPulsado(7)
boton7=Button(miFrame,text="7",width=3,command=lambda:numeroPulsado("7"))
boton7.grid(row=3,column=1)
boton8=Button(miFrame,text="8",width=3,command=lambda:numeroPulsado("8"))
boton8.grid(row=3,column=2)
boton6=Button(miFrame,text="9",width=3,command=lambda:numeroPulsado("9"))
boton6.grid(row=3,column=3)
botonRes=Button(miFrame,text="-",width=3,command=lambda:resta(numeroPantalla.get()))
botonRes.grid(row=3,column=4)

#---------------fila3-----------------
boton4=Button(miFrame,text="4",width=3,command=lambda:numeroPulsado("4"))
boton4.grid(row=4,column=1)
boton5=Button(miFrame,text="5",width=3,command=lambda:numeroPulsado("5"))
boton5.grid(row=4,column=2)
boton6=Button(miFrame,text="6",width=3,command=lambda:numeroPulsado("6"))
boton6.grid(row=4,column=3)
botonSum=Button(miFrame,text="+",width=3,command=lambda:suma(numeroPantalla.get()))
botonSum.grid(row=4,column=4)

#---------------fila4-----------------
boton1=Button(miFrame,text="1",width=3,command=lambda:numeroPulsado("1"))
boton1.grid(row=5,column=1)
boton2=Button(miFrame,text="2",width=3,command=lambda:numeroPulsado("2"))
boton2.grid(row=5,column=2)
boton3=Button(miFrame,text="3",width=3,command=lambda:numeroPulsado("3"))
boton3.grid(row=5,column=3)
botonRes=Button(miFrame,text="=",width=3,command=lambda:total())
botonRes.grid(row=5,column=4,rowspan=2,sticky=N+S)

#---------------fila5-----------------
botonPorcen=Button(miFrame,text="%",width=3,command=lambda:numeroPulsado("%"))
botonPorcen.grid(row=6,column=1)
boton0=Button(miFrame,text="0",width=3,command=lambda:numeroPulsado("0"))
boton0.grid(row=6,column=2)
botonCom=Button(miFrame,text=",",width=3,command=lambda:numeroPulsado(","))
botonCom.grid(row=6,column=3)


raiz.mainloop()