#Scipy e pra matemática, ciẽncia e engenharia pog pog
from scipy.constants import *
import scipy.fft
import numpy as np
from scipy import interpolate as intp
from scipy.interpolate import UnivariateSpline
import matplotlib.pyplot as plt
x = np.linspace(0,4,12)
y = np.cos(x**2/3+4)
plt.plot(x,y,'o')
plt.show()
'''f1 = intp.interp1d(x,y,kind = 'linear')
f2 = intp.interp1d(x,y,kind = 'cubic')
plt.plot(x,y,'o',xnew,f1(xnew), '-', xnew, f2(xnew), '--')
plt.legend(['data', 'linear', 'cubic', 'nearest'], loc = 'best')
plt.show()'''

a = np.exp(2j * np.pi * np.arange(8) / 8)
print(a)
b = scipy.fft.fft(a)
print(b)

print(pi)
print(c)
print(speed_of_light)
print(h)
print(G)
print(electron_mass)

x = np.linspace(-3,3,50)
y = np.exp(-x**2) + 0.1 * np.random.randn(50)
xs = np.linspace(-3,-3,1000)
plt.plot(x,y,'ro',ms=5)
plt.plot(x,y,'ro',ms=5)
spl = UnivariateSpline(x,y)
#smoothing factor 0
spl.set_smoothing_factor(0)
plt.plot(xs,spl(xs), 'yellow', lw=3)
plt.show()
