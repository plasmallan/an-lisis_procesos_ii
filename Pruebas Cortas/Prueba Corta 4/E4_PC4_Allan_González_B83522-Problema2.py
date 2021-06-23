import numpy as np

# Parámetros
G=0.00007635 # kg/s
cp=2.30e03 # J/(kg K)
Te=283.78 # K
Tv=425.68 # K
U0=0.006691e03 # W/(m^2 K)
A0=1.68 # m^2

k=(G*cp*Te+U0*A0*Tv)/(G*cp+U0*A0)

def Integrando(t):
    T=t*k*np.log(1.40+t)*np.log(2.67+t)*np.log(t)
    return T
def IntegralMonteCarlo(F,A,N):
    ni=[]
    for iN in range(N):
        np.random.seed(np.random.randint(10**4,10**8))
        ni.append((A[1]-A[0])*np.random.uniform()+A[0])
    f=F(np.array(ni)).sum()/N
    f2=(F(np.array(ni))**2).sum()/N
    trabajo1=(f*(A[1]-A[0])+(A[1]-A[0])*np.sqrt((f2-f**2)/N))*G*cp
    trabajo2=(f*(A[1]-A[0])-(A[1]-A[0])*np.sqrt((f2-f**2)/N))*G*cp
    trabajo=np.array([trabajo1,trabajo2]).mean()
    return trabajo,trabajo1,trabajo2,1/np.sqrt(N)
IntegralMonteCarlo(Integrando,[1,5.82],10000)