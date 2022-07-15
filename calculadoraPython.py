from tkinter import *
from turtle import right

raiz=Tk()

miFrame=Frame(raiz)
miFrame.pack()
#---------------pantalla-----------------
pantalla=Entry(miFrame)
pantalla.grid(row=1,column=1,padx=10,pady=11)
pantalla.config(bg="black",fg="green",justify="right")#03f943



raiz.mainloop()