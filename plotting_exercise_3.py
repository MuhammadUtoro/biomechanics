import numpy as np
import matplotlib.pyplot as plt

# This exercise is from: https://kineticstoolkit.uqam.ca/doc/matplotlib_style_exercise.html
# The plotting must be as followed
# The video camera curve must be full-line with square marker 
# The timing-gates curve must be dashed-black line with round markers

# Video camera data
t = [0.0, 2.0, 4.0, 6.0, 8.0, 10.0, 12.0, 14.0, 16.0, 18.0, 20.0]  # seconds
p = [0.0, 8.9, 28.0, 45.2, 60.4, 67.4, 75.5, 86.2, 93.0, 95.3, 100.0]  # meters

# Timing gates data (placed at positions 0m, 25m, 50m, 75m and 100m)
timing_gates_time = [0.0, 2.65, 5.70, 10.25, 20.0]  # seconds
p_gates = [0, 25, 50, 75, 100] # meters

plt.plot(t, p, 's-k', label='Video Camera')
plt.plot(timing_gates_time, p_gates, 'o--k', label='Timing Gates')
plt.legend()
plt.xlabel('Time (s)')
plt.ylabel('Position (m)')
plt.title('Race profile of a sprinter')
plt.grid(True)
plt.show()