import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import cumulative_trapezoid

data = np.loadtxt("freefall.csv", delimiter=",", skiprows=1)

t = data[:, 0]
y = data[:, 1]
v = np.gradient(y, t)
a = np.gradient(v, t)
print("Mean acceleration:", a.mean())
print("Standard deviation:", a.std())

v_recovered = cumulative_trapezoid(a, t, initial=0) + v[0]
y_recovered = cumulative_trapezoid(v_recovered, t, initial=0) + y[0]

max_difference = np.max(np.abs(y_recovered - y))

print("Maximum position difference:", max_difference)
fig, axes = plt.subplots(3, 1, sharex=True, figsize=(8, 8))

axes[0].plot(t, y)
axes[0].set_ylabel("Position (m)")

axes[1].plot(t, v)
axes[1].set_ylabel("Velocity (m/s)")

axes[2].plot(t, a)
axes[2].axhline(-9.81, linestyle="--")
axes[2].set_ylabel("Acceleration (m/s²)")
axes[2].set_xlabel("Time (s)")

plt.tight_layout()
plt.savefig("motion.png")
