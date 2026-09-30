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