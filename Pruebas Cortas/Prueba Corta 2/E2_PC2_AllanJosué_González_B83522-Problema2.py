import numpy as np
import matplotlib.pyplot as plt

F0=8.494 # [kmol/h]
V=4.160 # [m^3]
tau=9.862 #[h]

def Concentración(t):
    C=F0*t*np.exp(t/tau)/V
    dCdt=(F0/V)*(np.exp(t/tau)+t*np.exp(t/tau)/tau)
    return C,dCdt

def TiempoConcentrción(Cx,n,t0):
    p=0
    while p<=n:
        C,dCdt=Concentración(t0)
        t0=t0-(Cx-C)/(-dCdt)
        p+=1
    return t0,(Cx-C)

TiempoConcentrción(0.224,100,1)

t_prueba=np.arange(0,0.15,0.0001)
C_prueba,_=Concentración(t_prueba)

plt.plot(t_prueba,C_prueba)
plt.scatter(TiempoConcentrción(0.224,100,1)[0],Concentración(TiempoConcentrción(0.224,100,1)[0])[0],c='orange')
plt.xlabel('Tiempo [h]')
plt.ylabel('Concentración [kmol/m^3]')
plt.show()