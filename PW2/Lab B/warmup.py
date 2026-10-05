"""
PW2 Lab B Part 2 -- three routes to a minimum.

Compare gradient descent, Newton, and SLSQP on two functions:
  2A: f(x) = (x-3)**2 + 1          (easy, one minimum at x=3)
  2B: g(x) = x**4 - 3*x**2 + x + 5 (harder, several stationary points)
Run:  python warmup.py
"""

import numpy as np
from scipy.optimize import newton, minimize


# ---------- 2A: easy convex function ----------

def f(x):
    return (x - 3)**2 + 1


def df(x):
    return 2 * (x - 3)


def d2f(x):
    return 2.0


# Gradient descent
x = 0.0
lr = 0.1

while True:
    step = -lr * df(x)
    x = x + step

    if abs(step) < 1e-8:
        break

print("2A Gradient descent:", x)


# Newton's method
x_newton = newton(df, 0, fprime=d2f)

print("2A Newton:", x_newton)


# SLSQP
result = minimize(f, 0, method="SLSQP")

print("2A SLSQP:", result.x[0])


# ---------- 2B: harder landscape ----------

def g(x):
    return x**4 - 3*x**2 + x + 5


def dg(x):
    return 4*x**3 - 6*x + 1


def d2g(x):
    return 12*x**2 - 6


# Run from x0 = 0 and x0 = 2

for x0 in [0, 2]:

    print(f"\n2B starting from x0 = {x0}")

    # Gradient descent
    x = float(x0)
    lr = 0.01

    for i in range(10000):
        step = -lr * dg(x)
        x = x + step

        if abs(step) < 1e-8:
            break

    print("Gradient descent:", x)
    print("g(x):", g(x))

    # Newton's method
    x_newton = newton(dg, x0, fprime=d2g)

    print("Newton:", x_newton)
    print("g(x):", g(x_newton))
    print("g''(x):", d2g(x_newton))

    if d2g(x_newton) > 0:
        print("Newton result: minimum")
    elif d2g(x_newton) < 0:
        print("Newton result: maximum")
    else:
        print("Newton result: neither")

    # SLSQP
    result = minimize(g, x0, method="SLSQP")

    print("SLSQP:", result.x[0])
    print("g(x):", result.fun)