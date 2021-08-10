# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 18:44:03 2021

@author: Samaung
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy.optimize import curve_fit

dados=pd.read_excel("C:/Users/Samaung/OneDrive - unb.br/Documentos/Henrique/DadosExcel/histograma.xlsx")

x=dados["Est. (m)"]

n=plt.hist(x, ec="k",bins=np.arange(0,31,1))

bins=n[1][1:]

midbins=[i-0.5 for i in bins]
freq=n[0]

def gaussiana(x, a, b, c):
    return a*np.exp(-(x-b)**2/(2*c**2))

parametros, erro = curve_fit(gaussiana, midbins, freq)
xFit=np.arange(0,30.01,0.01)
plt.plot(xFit, gaussiana(xFit, *parametros))
print("a =", parametros[0])
print("b =", parametros[1])
print("c =", parametros[2])
print("Matris de covariância =", erro)