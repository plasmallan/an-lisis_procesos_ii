import pandas as pd
import numpy as np
from copy import deepcopy
import matplotlib.pyplot as plt

A=np.matrix([[9.9,9.1,4.8],
          [7.1,7.6,2.5],
          [4.7,9.9,9.9],
          [2.9,7.4,1.5],
          [8.4,6.8,7.6]])

def AijPi(A,ij):
    """
    Función que multiplica la entrada A[i,j] de la matriz A por el númer pi.
    Parámetros de entrada:
    ----------------------
    A: objeto matriz
    ij: tupla que contiene la el número de la fila i y columna j de la matriz que se quiere tomar.
    
    Salida:
    ----------------------
    valor: entrada A[i,j] de la matriz por pi.
    """
    i=ij[0]-1
    j=ij[1]-1
    valor=A[i,j]*np.pi
    return valor

AijPi(A,(4,2))