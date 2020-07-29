## MÉTODO DE RUNGE-KUTTA-FEHLBERG DE CUARTO ORDEN;
# AUTOR : HÉCTOR RAÚL VALENCIA AGUILAR
# FECHA : 20/07/2020

import numpy as np


def rkf45(f,y0,t0,tf,tol):
    t = t0
    y = y0
    ts = np.array(t)
    ys = np.array(y)
    d = np.spacing(1)
    hmin = (10**6)*d
    hmax = 0.1*(tf-t0)

    #Calculamos el paso de tiempo inicial:
    h = min(hmax,0.84*( tol/np.linalg.norm( f(t,y) ) )**(1/4) )

    while t < tf-h:
        if h > hmax:
            h = hmax
        if h < hmin:
            h = hmin
        k1 = f(t,y)
        k2 = f(t + h/4, y + h*k1/4)
        k3 = f(t + 3*h/8, y + h*(3*k1 + 9*k2)/32 )
        k4 = f(t + 12*h/13, y + h*(1932*k1 - 7200*k2 + 7296*k3 )/2197 )
        k5 = f(t + h, y + h*(439*k1/216 - 8*k2 + 3680*k3/513 - 845*k4/4104) )
        k6 = f(t + h/2, y + h*(-8*k1/27 + 2*k2 - 3544*k3/2565 + 1859*k4/4104 -11*k5/40) )
        tnew = t + h
        ynew = y + h*(25*k1/216 + 1408*k3/2565 + 2197*k4/4104 -k5/5)
        e = h*(np.linalg.norm(k1/360 -128*k3/4275 - 2197*k4/75240 + k5/50 + 2*k6/55 ))
        if e <= tol:
            t = tnew
            y = ynew
            ts = np.append(ts,t)
            ys = np.append(ys,y)

        #Calculamos el nuevo paso de tiempo
        h = h*min(4,0.84*(h*tol/e)**(1/4))
    return ts,ys





