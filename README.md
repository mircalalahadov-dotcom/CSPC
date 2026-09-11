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

