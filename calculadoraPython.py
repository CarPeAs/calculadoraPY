from codecs import BufferedIncrementalEncoder
from tkinter import *
from turtle import right

raiz=Tk()

miFrame=Frame(raiz)
miFrame.pack()
#---------------pantalla-----------------
pantalla=Entry(miFrame)
pantalla.grid(row=1,column=1,padx=5,pady=5,columnspan=4)
pantalla.config(bg="black",fg="#03f943",justify="right")#03f943

#---------------fila1-----------------
boton7=Button(miFrame,text="7",width=3)
boton7.grid(row=2,column=1)
boton8=Button(miFrame,text="8",width=3)
boton8.grid(row=2,column=2)
boton9=Button(miFrame,text="9",width=3)
boton9.grid(row=2,column=3)
botonDiv=Button(miFrame,text="/",width=3)
botonDiv.grid(row=2,column=4)

raiz.mainloop()