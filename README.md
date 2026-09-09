# CSPC — Practical Work 1

#Lab A — Reproducible Foundations: Environment, Git & GitHub

#Environment
The project was developed using:
Python 3.11
NumPy
pytest
Git
Conda

The Conda environment is defined in `PW1/Lab A/environment.yml`.

### Testing

The radioactive decay simulation was tested using:

```bash
pytest -v

All three tests passed successfully.

The tests verify:
the simulation starts with N0 atoms;
negative decay rates are rejected;
the simulation agrees with the analytical exponential decay law within the required tolerance.
Performance Comparison

The Python loop implementation was compared with the vectorised NumPy implementation using speed.py.

Implementation	Time:
Python loop	1.5707 s
NumPy	0.0002 s

The measured speed-up was:
7918.37× faster with NumPy.

Conclusion:

1.The experiment shows that vectorisation with NumPy can provide a very large performance improvement compared with iterating over individual atoms using a pure-Python loop.
2.Test also confirms that the simulation produces results consistent with the expected radioactive decay law.

