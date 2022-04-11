import scipy
import matplotlib.pyplot as plt   # MATLAB plotting functions
from control.matlab import *  # MATLAB-like functions
import numpy as np

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
# feedback gain
K = [0, 0.001, 0]

A = np.array(A)
B = np.array(B)
C = np.array(C)
D = np.array(D)
K = np.array(K)

Acl = A - B*K
# Calc. dc gain
ss_motor = ss(Acl, B, C, D)

Sys = tf(ss_motor)

print(dcgain(Sys))

# Compute state feedback transfer function
Kr = 424
Bcl = B/Kr
ss_motor_cls = ss(Acl, Bcl, C, D)
Sys_cls = tf(ss_motor_cls)

plt.figure(1)
# Specify timeline
t = np.linspace(0, 5, 10000)
# Plot step response
yout, T = step(Sys_cls * 1000, t)
plt.plot(T.T, yout.T)
plt.grid()
plt.show(block=True)
