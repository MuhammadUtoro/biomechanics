import numpy as np
import matplotlib.pyplot as plt

# This exercise is from: https://kineticstoolkit.uqam.ca/doc/matplotlib_plot_titles_labels_exercise1.html
# The task is to plot the recorded data from a sprinter for each 2 seconds as it shown in the web, but now there are timing gates placed at certain
# distances.

t = [0.0, 2.0, 4.0, 6.0, 8.0, 10.0, 12.0, 14.0, 16.0, 18.0, 20.0]  # seconds
p = [0.0, 8.9, 28.0, 45.2, 60.4, 67.4, 75.5, 86.2, 93.0, 95.3, 100.0]  # meters
timing_gates_time = [0.0, 2.65, 5.70, 10.25, 20.0] # seconds
p_gates = [0, 25, 50, 75, 100] # meters

plt.subplot(1,2,1)
plt.plot(t,p, label='Video Camera')
plt.xlabel('Time (s)')
plt.ylabel('Position (m)')
plt.title('Race profile of a sprinter')
plt.grid(True)
plt.subplot(1,2,2)
plt.plot(timing_gates_time,p_gates, label='Timing Gates')
plt.xlabel('Time (s)')
plt.ylabel('Position (m)')
plt.legend()
plt.title('Race profile of a sprinter')
plt.grid(True)
plt.show()