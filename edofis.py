from pyclbr import Function
from tkinter import Variable
from sympy import *
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


# numerador = y/((((x-a)**2)+(y**2))**(3/2)) - y/((((x+a)**2)+(y**2))**(3/2))
# denominador = (x-a)/((((x-a)**2)+(y**2))**(3/2)) - (x+a)/((((x+a)**2)+(y**2))**(3/2))
Variable('x')
Variable('y')
Variable('a')

a = 3*(10**-2)

# função que retorna dy/dx
def modelo(y,x):
    dydx = (y/((((x-a)**2)+(y**2))**(3/2)) - y/((((x+a)**2)+(y**2))**(3/2))) / ((x-a)/((((x-a)**2)+(y**2))**(3/2)) - (x+a)/((((x+a)**2)+(y**2))**(3/2)))
    return dydx

# condição inicial
y0 = -5

# intervalo de x
x = np.linspace(-0.06, 0.06)

# resolvendo edo
y = odeint (modelo, y0, x)

# plotando resultados
plt.plot(x,y)
plt.xlabel('dist x')
plt.ylabel('y(x)')
plt.show()

