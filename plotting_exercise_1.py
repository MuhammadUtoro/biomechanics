import numpy as np
import matplotlib.pyplot as plt

# This exercise is from: https://kineticstoolkit.uqam.ca/doc/matplotlib_plot_titles_labels_exercise1.html
# The task is to plot the recorded data from a sprinter for each 2 seconds as it shown in the web


t = [0.0, 2.0, 4.0, 6.0, 8.0, 10.0, 12.0, 14.0, 16.0, 18.0, 20.0]  # seconds
p = [0.0, 8.9, 28.0, 45.2, 60.4, 67.4, 75.5, 86.2, 93.0, 95.3, 100.0]  # meters

plt.plot(t,p)
plt.xlabel('Time (s)')
plt.ylabel('Position (m)')
plt.title('Race profile of a sprinter')
plt.grid(True)
plt.show()