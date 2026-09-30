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

trajectory = np.loadtxt("trajectory.csv", delimiter=",", skiprows=1)

t_traj = trajectory[:, 0]
x = trajectory[:, 1]
y_traj = trajectory[:, 2]

vx = np.gradient(x, t_traj)
vy = np.gradient(y_traj, t_traj)

speed = np.sqrt(vx**2 + vy**2)

plt.figure(figsize=(8, 6))
plt.plot(x, y_traj)
plt.xlabel("x (m)")
plt.ylabel("y (m)")
plt.title("Trajectory")
plt.tight_layout()
plt.savefig("trajectory.png")

plt.figure(figsize=(8, 6))
plt.plot(t_traj, speed)
plt.xlabel("Time (s)")
plt.ylabel("Speed (m/s)")
plt.title("Speed vs Time")
plt.tight_layout()
plt.savefig("speed.png")
