# The ktk.TimeSeries type is largely inspired by Matlab’s timeseries and tscollection. Every TimeSeries contains time, data, events and metadata.
# A TimeSeries in its simplest form contains a time attribute and at least one data series. For example:

import kineticstoolkit as ktk
import kineticstoolkit.lab as ktk
import numpy as np
import matplotlib.pyplot as plt

ts = ktk.TimeSeries()                     # Create an empty TimeSeries
# ts.time = np.arange(0, 10, 0.1)           # Assign time
# ts.data["Sinus"] = np.sin(ts.time)        # Create a data series
# ts.data["Cosinus"] = np.cos(ts.time)      # Create another data series
# ts.data["SquareRoot"] = np.sqrt(ts.time)  # Create yet another data series

# ts.plot("Sinus")
# plt.xlabel("Time (s)")
# plt.axis([0, 10, -1, 1])
# plt.show()

# Extracting and plotting marker data from file:
c3d_contents = ktk.read_c3d('Squat_2_0001.c3d', convert_point_unit=True)

c3d_ptinfo = c3d_contents["Points"].data
c3d_ts = c3d_contents["Points"].time
c3d_alginfo = c3d_contents["Analogs"].data

SIAS_markers = c3d_ptinfo["SIAS_left"][:,2]
plt.subplot(1,2,1)
plt.plot(SIAS_markers,'--k')
plt.xlabel("Time (s)")
plt.ylabel("Height (m)")


# Extracting and plotting force data from file
# print(c3d_alginfo)
zforce_info = c3d_alginfo["FP02_FZ1"]

plt.subplot(1,2,2)
plt.plot(zforce_info,'-b')
plt.xlabel("Time (s)")
plt.tight_layout()
plt.show()
