## SIMULACIONES CON EL MODELO SEIR
# AUTOR: HÉCTOR RAÚL VALENCIA AGUILAR
# FECHA: 22/07/2020

import tkinter as tk
import numpy as np
from ExamplesSEIR import SEIR

def Ejecutar():
    y01 = eval(int1.get())
    y02 = int(int2.get())
    y03 = int(int3.get())
    y04 = int(int4.get())
    y0 = [y01,y02,y03,y04]
    y0 = np.array(y0)
    t0 = int(intt1.get())
    tf = int(inttf1.get())
    beta = float(intb.get())
    gamma = eval(intg.get())
    sigma = eval(ints.get())
    tol = float(intT.get())
    N = eval(intN.get())
    SEIR(y0,t0,tf,tol,beta,sigma,gamma,N)
    return
    
ventana = tk.Tk()
ventana.title("Condiciones iniciales-SEIR")
ventana.geometry('750x300')
ventana.configure(background='Aquamarine')
var = tk.StringVar()

e1 = tk.Label(ventana,text = 'S_0 :', bg = 'Aquamarine')
e1.place(x=20,y=20)
int1 = tk.Entry(ventana)
int1.place(x=50,y=20)

e2 = tk.Label(ventana,text = 'E_0 :', bg = 'Aquamarine')
e2.place(x=200,y=20)
int2 = tk.Entry(ventana)
int2.place(x=230,y=20)

e3 = tk.Label(ventana,text = 'I_0 :', bg = 'Aquamarine')
e3.place(x=380,y=20)
int3 = tk.Entry(ventana)
int3.place(x=410,y=20)

e4 = tk.Label(ventana,text = 'R_0 :', bg = 'Aquamarine')
e4.place(x=560,y=20)
int4 = tk.Entry(ventana)
int4.place(x=590,y=20)

t1 = tk.Label(ventana,text = 'tiempo inicial :', bg = 'Aquamarine')
t1.place(x=160,y=80)
intt1 = tk.Entry(ventana)
intt1.place(x=250,y=80)

tf = tk.Label(ventana,text = 'tiempo final:', bg = 'Aquamarine')
tf.place(x=380,y=80)
inttf1 = tk.Entry(ventana)
inttf1.place(x=460,y=80)

beta = tk.Label(ventana,text = 'beta :', bg = 'Aquamarine')
beta.place(x=20, y=160)
intb = tk.Entry(ventana)
intb.place(x=60,y=160)

gamma = tk.Label(ventana,text = 'gamma :', bg = 'Aquamarine')
gamma.place(x=200, y=160)
intg = tk.Entry(ventana)
intg.place(x=255,y=160)

sigma = tk.Label(ventana,text = 'sigma :', bg = 'Aquamarine')
sigma.place(x=400, y=160)
ints = tk.Entry(ventana)
ints.place(x=445,y=160)

N = tk.Label(ventana,text = 'N :', bg = 'Aquamarine')
N.place(x=580, y=160)
intN = tk.Entry(ventana)
intN.place(x=610,y=160)

Tol = tk.Label(ventana,text = 'tol :', bg = 'Aquamarine')
Tol.place(x=280, y=210)
intT = tk.Entry(ventana)
intT.place(x=310,y=210)

Button = tk.Button(ventana,text="Ejecutar",fg = "black",command = Ejecutar )
Button.place(x=350,y=250)


ventana.mainloop()

