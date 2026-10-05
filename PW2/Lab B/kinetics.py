"""
PW2 Lab B Part 3 -- fit a reaction's rate constant to measured data.

A first-order reaction decays as C(t) = C0 * exp(-k*t).
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize


# Read the data
data = np.loadtxt("kinetics.csv", delimiter=",", skiprows=1)

t = data[:, 0]
C = data[:, 1]

# Initial concentration
C0 = C[0]


# Total error
def total_error(k):
    k = k[0]
    model = C0 * np.exp(-k * t)
    return np.sum((C - model) ** 2)


# Minimize the error
result = minimize(
    total_error,
    x0=[0.5],
    method="SLSQP",
    bounds=[(0, 5)]
)

k_fitted = result.x[0]

print("Fitted k:", k_fitted)


# Fitted curve
t_fit = np.linspace(t.min(), t.max(), 200)
C_fit = C0 * np.exp(-k_fitted * t_fit)


# Plot
plt.figure(figsize=(8, 5))

plt.scatter(t, C, label="Measured data")
plt.plot(t_fit, C_fit, label="Fitted curve")

plt.xlabel("Time")
plt.ylabel("Concentration")
plt.title("First-order reaction rate fit")
plt.legend()
plt.grid(True)

plt.savefig("kinetics.png", dpi=300)
plt.show()