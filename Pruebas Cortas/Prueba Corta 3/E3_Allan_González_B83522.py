import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

data=np.loadtxt("Datos_PC3.txt",skiprows=1).tolist()
data.sort(key = lambda x:x[0])
data=np.array(data)

R=8.314472
def Arrhenius(T,A,Ea):
    return A*np.exp(-Ea/((T+273.15)*R*10**-3))
coefs,covs=curve_fit(Arrhenius,data[:,0],data[:,1]*10**-7)
plt.figure(dpi=120)
plt.scatter(data[:,0],data[:,1]*10**-7,color="black")
plt.plot(data[:,0],Arrhenius(data[:,0],coefs[0],coefs[1]))
plt.legend(["Ajuste","Datos"])
plt.xlabel("Temperatura [°C]")
plt.ylabel("Constante de Reacción [s^-1]")
plt.savefig("AllanGonzález_PruebaCorta3.png")
plt.show()
k=Arrhenius(52.25,coefs[0],coefs[1])
k
error=((6.26e-07-k)/6.26e-07)*100
error