# Monte Carlo Mandelbrot Area
This repository contains Python code used for comparing the convergence rate of 
different Monte Carlo approaches. This project focuses on using Monte Carlo estimates
to determine the area of the Mandelbrot set, providing a insight into the convergence of the different Monte
Carlo approaches.

# Dependencies
The following dependencies have to be installed:
- NumPy
- SciPy
- Matplotlib
- Math

# Structure
- StoStim_Assignment1.ipynb: Main file of this repository. This one contains all the
code used to obtain and visualize the results
- Mandelbrot.py: Functions used to generate the Mandelbrot set and determine if a point
if within the mandelbrot set
- MonteCarloIntegration.py: Functions used to apply Random Sampling, Latin Hypercube Sampling
and Orthogonal sampling methods to estimate the area of the Mandelbrot set
- QuasiMonteCarlo.py: Functions used to apply Quasi Monte carlo to estimate the area of the
Mandelbrot set
- CircleSampling.py: Function used to apply Random sampling, but instead of randomly taking points
from a square, a circle is used
- ColorfulMandelbrotSet.py: Functions used to generate a Mandelbrot set on the complex plane with colors

