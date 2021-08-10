# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 11:36:35 2021

@author: Samaung
"""

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
from scipy.optimize import curve_fit
import numpy as np

fig=plt.figure()
gráfico=fig.add_subplot(111)

start=time.time()

xs=[]
ys=[]

def reta(x,a,b):
    return a*x+b

def atualiza(i):
    dados=open("C:/Users/Samaung/OneDrive - unb.br/Documentos/Henrique/DadosExcel/dadoslive.txt.","r").read()
    linhas=dados.split("\n")
    for y in linhas:
        if len(y)>0:
            ys.append(float(y))
            if len(xs)==0:
                xs.append(time.time()-start)
            if len(ys)>len(xs):
                x=time.time()-start
                xs.append(x)
    gráfico.clear()
    if len(xs)>1:
        parametros, erro = curve_fit(reta, xs, ys)
        xFit=np.arange(0,xs[-1]+0.1, 0.1)
        gráfico.plot(xFit, reta(xFit, *parametros))
        plt.title("Valor digitado em função do tempo\na = {0}\nb = {1}".format(parametros[0], parametros[1]))
    else:
        plt.title("Valor digitado em função do tempo")
    gráfico.plot(xs,ys,"-o")
    plt.xlabel("Tempo (s)")
    plt.ylabel("Valor digitado")
    #plt.title("Valor digitado em função do tempo")
    ys.clear()
    
a=animation.FuncAnimation(fig, atualiza, interval=1)
plt.show()