import numpy as np

def F1(x,y):
    """
    Función que regresa el valor de la función 1 y el valor de sus dos derivadas parciales para x y y.
    """
    return x**3-y**(3/5)-2,3*x**2,-3*y**(-2/5)/5

def F2(x,y):
    """
    Función que regresa el valor de la función 2 y el valor de sus dos derivadas parciales para x y y.
    """
    return np.exp(5*x/3)-x*y-9,5*np.exp(5*x/3)/3-y,-x

def JacobianoInverso(x,y):
    """
    Función que calcula el Jacobiano inverso de las dos funciones F1 y F2, una matriz compuesta de las derivadas parciales.
    """
    _,df1dx,df1dy=F1(x,y)
    _,df2dx,df2dy=F2(x,y)
    jacobiano=np.matrix([[df1dx,df1dy],
                        [df2dx,df2dy]])
    jacobianoInverso=np.linalg.inv(jacobiano)
    return jacobianoInverso

def SistemaEcuaciones(x0,y0,n):
    """
    Función que obtiene una solución para las dos variables x y y del sistema de ecuaciones compuesto por F1 y F2 y el
    error estimado para ambas ecuaciones.
    """
    p=0
    while p<=n:
        f1,_,_=F1(x0,y0)
        f2,_,_=F2(x0,y0)
        g1=0-f1
        g2=0-f2
        delta=np.matrix([g1,
                         g2])
        solucion=JacobianoInverso(x0,y0)*delta.reshape(2,1)
        x0+=np.array(solucion)[0][0]
        y0+=np.array(solucion)[1][0]
        p+=1
        errores=(g1,g2)
    return x0,y0,errores

SistemaEcuaciones(100,20,1000)