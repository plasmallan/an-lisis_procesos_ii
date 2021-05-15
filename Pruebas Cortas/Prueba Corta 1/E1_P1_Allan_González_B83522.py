import pandas as pd
import numpy as np
from copy import deepcopy
import matplotlib.pyplot as plt

"""
# Problema 1

Se tiene la ecuación química balanceada:

$$C_{6}H_{8}+C_{8}H_{12}=C_{14}H_{20}$$

Para estimar posibles concentraciones en el equilibrio, se puede tomar que las concentraciones iniciales de $A=C_{6}H_{8}$ y $B=C_{8}H_{12}$ son iguales a $x$ y que el equilibrio puede ser alcanzado una vez se toman partes iguales de cada uno de los compuestos, por ejemplo tomando la mitad de $A$ y $B$ para formar $C$ se tiene que:

$$\frac{\frac{x}{2}+\frac{x}{2}}{\left(x-\frac{x}{2}\right)^2}=153.818\Rightarrow x=0.026\textrm{ [frac.mol]}$$

De esta forma, se entiende que las concentraciones iniciales de $A$ y $B$ corresponden a $0.026$, mientras que una vez alcanzado el equilibrio, las concentraciones de estos son de $0.013$ y la de $C$ de $0.026$
"""

# Se importan los datos y se visualizan las primeras 5 líneas
data=pd.read_csv('Concentrations.csv',low_memory=False,delimiter=';')
data.head()

# Se calcula la constante Q para cada uno de los que se hayan en el sistema
Q=pd.DataFrame(data['Concentration C']/data['Concentration A']/data['Concentration B'])

# Se almacena Q como arreglo de numpy para simplificar la obtención de los valores que se desean a continuación
Qarray=np.array(Q)

#Se buscan los que están en equilibrio y se almacenan en Qeq, se retorna el la cantidad que cumplen la condición
Qeq=Qarray[np.where(np.abs(Qarray-153.818)<1)]
len(Qeq)