"""
PW2 Lab B Part 4 -- chemical equilibrium via the equilibrium constant K.

Reaction H2 + I2 <=> 2 HI, starting from 1 mol H2 and 1 mol I2.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import newton, minimize


K = 15.6
a = b = 1.0


# ---------- Equilibrium equation ----------

def k_imbalance(x):
    return (2 * x)**2 / ((a - x) * (b - x)) - K


# ---------- Method 1: Newton root-finding ----------

x_newton = newton(k_imbalance, x0=0.5)

print("Newton x:", x_newton)


# ---------- Method 2: SLSQP minimization ----------

def squared_imbalance(x):
    return k_imbalance(x[0])**2


result = minimize(
    squared_imbalance,
    x0=[0.5],
    method="SLSQP",
    bounds=[(0, 0.999)]
)

x_slsqp = result.x[0]

print("SLSQP x:", x_slsqp)
print("Difference:", abs(x_newton - x_slsqp))


# ---------- Equilibrium amounts ----------

H2_eq = a - x_newton
I2_eq = b - x_newton
HI_eq = 2 * x_newton

print("\nEquilibrium amounts:")
print("H2:", H2_eq, "mol")
print("I2:", I2_eq, "mol")
print("HI:", HI_eq, "mol")


# ---------- Plot ----------

x_values = np.linspace(0, 0.999, 300)

H2_values = a - x_values
I2_values = b - x_values
HI_values = 2 * x_values

plt.figure(figsize=(8, 5))

plt.plot(x_values, H2_values, label="H2")
plt.plot(x_values, I2_values, label="I2")
plt.plot(x_values, HI_values, label="HI")

plt.axvline(
    x_newton,
    linestyle="--",
    label="Equilibrium"
)

plt.xlabel("Reaction extent x")
plt.ylabel("Amount (mol)")
plt.title("Chemical Equilibrium: H2 + I2 <=> 2 HI")
plt.legend()
plt.grid(True)

plt.savefig("equilibrium.png", dpi=300)
plt.show()