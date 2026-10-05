"""
PW2 Lab B Part 5 (bonus) -- find a titration's equivalence point.

titration.csv holds a titration curve: pH versus the volume of base added.
"""

import numpy as np
import matplotlib.pyplot as plt


# Read the data
data = np.loadtxt("titration.csv", delimiter=",", skiprows=1)

V = data[:, 0]
pH = data[:, 1]


# Calculate the slope
slope = np.gradient(pH, V)

# Find the equivalence point
index = np.argmax(slope)
equivalence_volume = V[index]

print("Equivalence point:", equivalence_volume, "mL")
print("Maximum slope:", slope[index])


# Create two plots
fig, axes = plt.subplots(1, 2, figsize=(12, 5))


# pH curve
axes[0].plot(V, pH)
axes[0].axvline(
    equivalence_volume,
    linestyle="--",
    label="Equivalence point"
)

axes[0].set_xlabel("Volume of base (mL)")
axes[0].set_ylabel("pH")
axes[0].set_title("Titration Curve")
axes[0].legend()
axes[0].grid(True)


# Slope curve
axes[1].plot(V, slope)
axes[1].axvline(
    equivalence_volume,
    linestyle="--",
    label="Equivalence point"
)

axes[1].set_xlabel("Volume of base (mL)")
axes[1].set_ylabel("dpH/dV")
axes[1].set_title("Slope of Titration Curve")
axes[1].legend()
axes[1].grid(True)


plt.tight_layout()
plt.savefig("titration.png", dpi=300)
plt.show()