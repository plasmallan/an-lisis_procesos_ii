import numpy as np

# Parámetros
G=0.00007635 # kg/s
cp=2.30e03 # J/(kg K)
Te=283.78 # K
Tv=425.68 # K
U0=0.006691e03 # W/(m^2 K)
A0=1.68 # m^2

k=(G*cp*Te+U0*A0*Tv)/(G*cp+U0*A0)

def Derivando(t):
    T=k*np.log(1.40+t)*np.log(2.67+t)*np.log(t)
    return T
def Derivada(f,h,t):
    x1=f(t-h)
    x2=f(t+h)
    dfdt=(x2-x1)/(2*h)
    return dfdt
Derivada(Derivando,0.001,5.16)