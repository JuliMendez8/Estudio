import numpy as np
import matplotlib.pyplot as plt

X=np.linspace(-5, 5, 50).astype(float)
Y=(1*X**3) - (4*X**2) + (1*X) + 6 #Modelo

# Truco para los ejes

plt.plot(X,0*Y,'-r',0*X,Y,'-r',X, Y,'-k')
plt.grid()
plt.xlabel('Valores de x')
plt.ylabel('Valores de y')
plt.axis([-10,10,-10,10])
plt.show()