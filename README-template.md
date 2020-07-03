<p align="center">
  <img src="https://raw.githubusercontent.com/devitocodes/devito/master/docs/source/_static/devito_logo.png">
</p>

# TheMatrix -- Devito benchmark matrix

Benchmarking Devito solvers across computer architectures, execution models, compilers and anything else we can think of.

[![Run TheMatrix](https://img.shields.io/badge/run-thematrix-brightgreen)](https://www.actionspanel.app/app/devitocodes/thematrix)
[![asv](http://img.shields.io/badge/benchmarked%20by-asv-blue.svg?style=flat)](http://www.devitoproject.org/thematrix/)
[![Slack Status](https://img.shields.io/badge/chat-on%20slack-%2336C5F0)](https://opesci-slackin.now.sh)

The aim of TheMatrix is to:

* Create a platform to enable automated benchmarking across many platforms.
* Perform benchmarking in an open and reproducible manner.
* Make it extendible to new architectures, compilers etc.
* Provide performance baseline for performance optimisation; catch performance regression.

Matrix benchmark parameters include:
* Architecture: Intel® Xeon® Platinum 8168 processor (Azure), Intel® Xeon® E5 2667 v3 (Azure), NVIDIA® Tesla® K80 (Azure)
* Execution models: OpenMP, OpenMP offloading, OpenACC, MPI (and mixed)
* Compilers: GCC, LLVM, PGI
* Numerical solvers: isotropic acoustic, isotropic skew-self-adjoint acoustic, isotropic elastic, isotropic viscoelastic, TTI acoustic
* Profilers: native performance metrics computed by Devito (runtime, FLOPS, GPt/s)
* Visualization: [Air Speed velocity](https://asv.readthedocs.io/en/stable/index.html).

If there is something missing that you would like to see in the matrix then please then let us know...particularly if you can contribute development effort, hardware or funding!

## The matrix of platforms tested
The table below provides a summary of the various platforms and configurations included in TheMatrix suite. Click on the links in the table for explanations and [click here](${THEMATRIX_HTML}) for further details.

${THEMATRIX_TABLE}

## Profiling results
This table provides a summary of the numerical models benchmarked - [click here for verbosity](${BENCHMARKS_HTML}). Unless otherwise stated, models are three-dimensional, use 2nd order temporal and 12th order spatial discretizations, and single-precision floating point arithmetic. Click on the links in the table for profiling results and further information regarding the individual benchamrk.

${BENCHMARKS_TABLE}

### Performance metrics
See the [Devito FAQ](https://github.com/devitocodes/devito/wiki/FAQ) for details on [how Devito computes the performance of an operator](https://github.com/devitocodes/devito/wiki/FAQ#how-does-devito-compute-the-performance-of-an-operator).
* GFLOPS - giga floating point operations per second
* FD-GPts/s - finite-difference giga grid points per second 
* Runtime
