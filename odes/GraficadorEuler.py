import numpy as np
import matplotlib.pyplot as plt


data = np.loadtxt('data.dat')
tiempo=data[:,0]
v=data[:,1]
x=data[:,2]

plt.figure()
plt.plot(tiempo,x,label='posición')
plt.xlabel('t(s)')
plt.ylabel('x(m)')
plt.title("Posición para armónico simple")
plt.grid()
plt.legend()
plt.savefig('posicion.png')

plt.figure()
plt.plot(x,v,label="X vs V")
plt.xlabel('x(m)')
plt.ylabel('v(m/s)')
plt.title("velocidad para armonico simple")
plt.grid()
plt.legend()
plt.savefig('velocidad.png')