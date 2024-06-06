import matplotlib.pyplot as plt
from math import sin, cos, pi

Rs = 0.015
Ls = 0.001
lamaf = 0.00015

spd_rpm = 6000
pole_pair = 2
omega = spd_rpm / 60 * pole_pair * 2 * pi



voltage_phase = 90
voltage_mag = 1

# Plot the phasors
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
#ax.plot([voltage_phase, current_phase, bemf_phase], [voltage_mag, current_mag, bemf_mag], 'o-', linewidth=2)
ax.plot(voltage_phase, voltage_mag, 'o-', linewidth=2)

ax.arrow(0, 0.0, 0, 1, alpha = 0.5, width = 0.015)

# Add labels and legend
ax.set_title('Phasor Diagram for Motor', fontsize=20)
ax.legend(['Voltage', 'Current', 'BEMF'], loc='best')

# Show the plot
plt.show()