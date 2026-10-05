# CSPC - Computer Science for Physics and Chemistry

My coursework repository. Each practical is under PW<n>/Lab <X>/.

## Setup

Create the Conda environment:
conda env create -f PW1/Lab\ A/environment.yml
Activate the environment:
conda activate cspc
Run the tests:
pytest -v

## PW1 - Lab A: Reproducible Foundations

**What I built:**

Set up a reproducible Conda environment with Python 3.11, NumPy, pytest and Git and created speed.py to compare the Python loop with NumPy.

**Speed comparison (loop vs NumPy):**

-loop: 1.5707 s
-numpy: 0.0002 s
-speed-up: 7918.37x faster

**Tests:**yes all 3 tests passed successfully.

**Conclusion:**
I understood how to work with git better  and also proved for myself the theory(as it was expected numpy is the way faster 
than loop). The tests showed that the simulation works correctly and it gives the expected decay results.


## PW1 — Lab B

The observed decay data showed a clear decreasing trend over time. The overall shape was broadly consistent with the analytical exponential decay law using λ = 0.3.

The plotting script reads `decay_observed.csv`, calculates the analytical decay, and generates a side-by-side comparison plot.

Snakemake automates the workflow: it uses `decay_observed.csv` as input and runs `plot.py` to generate `figure.png`. If the output is already up to date, Snakemake does not rebuild it.

## PW2 --- Lab A

- Mean acceleration: -8.58 m/s²
- Standard deviation of acceleration: 28.72 m/s²
- Differentiation amplifies measurement noise, and the second derivative amplifies it further, making acceleration much noisier than position.
- After integrating acceleration to velocity and then position, the maximum difference between recovered and original position was 0.785 m.
## PW2 --- Lab B

### Part 2 — Optimization methods

For the simple convex function in Part 2A, all three methods agreed and reached the global minimum at x ≈ 3.

For the harder function in Part 2B, the methods did not always agree. Starting from x0 = 0, Newton's method converged to a maximum at x ≈ 0.170 because g''(x) < 0, while gradient descent and SLSQP found the minimum near x ≈ -1.301. Starting from x0 = 2, Newton and gradient descent found the minimum near x ≈ 1.131, while SLSQP found the other minimum near x ≈ -1.301.

This shows that the starting point and optimization method can affect the result on a complicated optimization landscape.

### Part 3 — Reaction kinetics

The first-order reaction rate constant was fitted by minimizing the total squared error using SLSQP.

- Fitted rate constant: k = 0.26176
- Expected value: approximately 0.25

The fitted value is close to the expected value. The measured data and fitted exponential curve are saved in `kinetics.png`.

### Part 4 — Chemical equilibrium

For the reaction H2 + I2 <=> 2 HI with K = 15.6:

- Newton equilibrium extent: x = 0.6638477
- SLSQP equilibrium extent: x = 0.6638474
- Difference between methods: approximately 2.39e-7

Equilibrium amounts:

- H2 = 0.33615 mol
- I2 = 0.33615 mol
- HI = 1.32770 mol

The equilibrium plot is saved in `equilibrium.png`.

### Part 5 — Titration bonus

The equivalence point was found by calculating the numerical slope of the pH curve and locating its maximum.

- Equivalence point: 50.0 mL
- Maximum slope: 4.0

The titration curve and slope plot are saved in `titration.png`.
