import numpy as np

# Parámetros
k=0.0014
C0=856.08
alpha=0.9
CL=C0*alpha
L=18.05
Dab=0.0028098
h=0.0001

def Analítica(z):
    return (CL-C0*np.cosh(L*np.sqrt(k/Dab)))/(np.sinh(L*np.sqrt(k/Dab)))*np.sinh(z*np.sqrt(k/Dab))+C0*np.cosh(z*np.sqrt(k/Dab))
def Derivada(f,h,t):
    x1=f(t-h)
    x2=f(t+h)
    dfdt=(x2-x1)/(2*h)
    return dfdt
u0=Derivada(Analítica,h,0)
f = lambda C: k*C/Dab # ODE
def RK4(f,zf):
    '''
    Esta función corresponde a una función que soluciona una EDO por RK4 iterando sobre un y = np.arange(y0,yf,h)
    
    Parámetros
    ------------------------
    f: función al lado derecho de la EDO
    zf: valor de la variable independiente para el cual se desea encontrar el valor de C.
    ------------------------
    C: valor de C en zf.
    '''
    u=u0
    C=C0
    z=0
    while z<=zf:
        m1=h*u
        k1=h*f(C)
        m2=h*(u+k1/2)
        k2=h*f(C+m1/2)
        m3=h*(u+k2/2)
        k3=h*f(C+m2/2)
        m4=h*(u+k3)
        k4=h*f(C+m3)
        u+=(k1+2*k2+2*k3+k4)/6
        C+=(m1+2*m2+2*m3+m4)/6
        z+=h
    return C
RK4(f,4.33)