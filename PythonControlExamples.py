import control
import matplotlib.pyplot as plt
import numpy as np
import math
from scipy import signal
import control.matlab

Ts=0.0005

##################################################################
## Transfer Function of system ##
num1=[0.00943,0.01886,0.00943]
den1=[1,-1.8188,0.8224]
g=control.tf(num1,den1,Ts)

## Transfer Function of P Controller ##
numP=[1.4368]
denP=[1]
cP=control.tf(numP,denP,Ts)

## Transfer Function of PI Controller ##
numPI=[1.4352,-1.2911]
denPI=[1,-1]
cPI=control.tf(numPI,denPI,Ts)

## Transfer Function of PID Controller ##
numPID=[4.6234, -6.95451828, 2.61524470]
denPID=[1, -1, 0]
cPID=control.tf(numPID,denPID,Ts)
##################################################################

## Close Loop Feedbaack System ##
num3=[1]
den3=[1]
h = control.tf(num3,den3,Ts) 
## Open Loop Control ##
gol=control.series(g,cPID)
## Close Loop Control ##
gcl = control.feedback(gol,h)

## STEP REPONSE OF CLOSE LOOP CONTROL ##
N=500
n = np.arange(0, Ts*N, Ts)
nout, y = control.step_response(gcl, n)
plt.plot(y)
plt.xlabel('n')
plt.ylabel('y[n]')
plt.grid()
plt.show()

 ## BODE PLOT ##
[mag,phase,freq] = control.bode(gcl)
## margins ##
[gm,pm,wg,wp] = control.margin(gcl)
## dcgain ##
control.dcgain(gcl)




##################################################################
## NYQUIST PLOT ##
f_nyquist = 2*math.pi/Ts/2;
k_nyquist = math.log10(f_nyquist);
w_p = np.logspace(-20,k_nyquist,1000)
[re,im,w] = control.nyquist(gcl,w_p);
plt.grid(True)
plt.xlabel('Real')
plt.ylabel('Imaginary')
plt.ylim(-10,10)
plt.xlim(-5,12)
plt.show()
##################################################################


##################################################################
## BODE PLOT ##
[mag,phase,freq] = control.bode(gcl)
##################################################################


##################################################################
## ROOT LOCUS ##
control.matlab.rlocus(gcl)
from matplotlib import pyplot as plt
plt.ylim(-1,1)
plt.xlim(-1.5,1)
plt.grid()
plt.show()
##################################################################


##################################################################
## DAMPING FACTOR & NATURAL & POLES ##
[gm,pm,wg,wp] = control.margin(gcl)
print(control.damp(gcl))
print(control.dcgain(gcl))
##################################################################
