## SIMULACIONES CON EL MODELO SEIR
# AUTOR: HÉCTOR RAÚL VALENCIA AGUILAR
# FECHA: 22/07/2020

import numpy as np
import pandas as pd
from pandas import ExcelWriter
import matplotlib.pyplot as plt
from rkf45 import rkf45


# from rk4 import rk4
# from rkf23 import rkf23


def SEIR(y0,t0,tf,tol,beta,sigma,gamma,N):

    #DEFINIMOS LA FUNCIÓN QUE DETERMINA LA ECUACIÓN DIFERENCIAL DEL MODELO
    def f(t, y):
        f = [-beta*y[0]*y[2]/N, beta*y[0]*y[2]/N - sigma*y[1], sigma*y[1] - gamma*y[2], gamma*y[2]]
        f = np.array(f)
        return f

    #Utilizamos el método de Runge-Kutta-Fehlberg para resolver la ecuación diferencial.


    (a,b) = rkf45(f,y0,t0,tf,tol)

    #(a,b) = rk4(f,y0,t0,tf,tol)

    #O bien podemos usar el método de segundo y tercer orden:

    ### (a,b) = rkf23(f,y0,t0,tf,tol)

    b = np.reshape(b, (int(len(b)/4), 4))

    #Ahora guardamos los datos en un archivo csv

    df = {'Tiempo': a,'Suceptibles' : b[:,0],'Expuestos': b[:,1],'Infectados': b[:,2],'Recuperados':b[:,3]}
    df = pd.DataFrame(df)
    #Podemos observar los primeros datos del data frame utilizando:
    print(df.head())
    df.to_excel('Simulación SEIR.xlsx')


    #Mostramos el gráfico.

    plt.plot(a,b[:,0],label = 'Suceptibles')
    plt.plot(a,b[:,1],label = 'Expuestos')
    plt.plot(a,b[:,2],label = 'Infectados')
    plt.plot(a,b[:,3],label = 'Recuperados')
    plt.title('MODELO-SEIR')
    plt.xlabel('Tiempo')
    plt.legend()
    plt.show()

    