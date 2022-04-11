import scipy
import matplotlib.pyplot as plt   # MATLAB plotting functions
from control.matlab import *  # MATLAB-like functions

PolePairs = 2
Rs = 0.16;      # ohm
Ls = 0.00015;   # H
flux = 0.00125  # Wb
J = 5e-6;       # N-m-s^2/rad
B = 2.5e-6;     # N-m-s / rad

Kt = 3/2*PolePairs * flux
Ke = flux

s = tf('s')

A = [[0, 1, 0], [0, -B/J, Kt/J], [0, -Ke/Ls, -Rs/Ls]]
B = [[0], [0], [1/Ls]]
C = [0, 1, 0]
D = 0

ss_motor = ss(A, B, C, D)

Gs = tf(ss_motor)

print(Gs)

#PI controller
Cs = 0.001 + 0.01/s
Sys = feedback(Cs*Gs)

# Calc. system poles
print(pole(Sys))

plt.figure(1)
# step response
target_speed = 6000
yout, T = step(Sys * target_speed, 5)
plt.plot(T.T, yout.T)
plt.grid()
plt.show(block=False)

plt.figure(2)
# controller output voltage
Vs = Cs / (1+Cs*Gs)
yout, T = step(Vs*target_speed, 5)
plt.plot(T.T, yout.T)
plt.grid()
plt.show()
