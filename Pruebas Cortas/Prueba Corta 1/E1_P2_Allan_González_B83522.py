import pandas as pd
import numpy as np
from copy import deepcopy
import matplotlib.pyplot as plt

# Se crean las dos matrices con Numpy
A=np.matrix([[2.8,9.3],
            [4.2,3.1],
            [1.4,9.1]])
B=np.matrix([[8.1,5.3,7.7],
            [6.7,2.0,5.8]])

# Se calcula la traza del producto de ambas matrices
np.trace(np.matmul(A,B))