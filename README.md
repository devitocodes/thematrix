<p align="center">
  <img src="https://raw.githubusercontent.com/devitocodes/devito/master/docs/source/_static/devito_logo.png">
</p>

# TheMatrix -- Devito benchmark matrix

[![Run TheMatrix](https://img.shields.io/badge/run-thematrix-brightgreen)](https://www.actionspanel.app/app/devitocodes/thematrix)
[![asv](http://img.shields.io/badge/benchmarked%20by-asv-blue.svg?style=flat)](https://devitocodes.github.io/devito-performance)
[![Slack Status](https://img.shields.io/badge/chat-on%20slack-%2336C5F0)](https://opesci-slackin.now.sh)

Perfomance of production-grade wave propagators implemented with Devito -- on CPUs,
GPUs, and clusters thereof.

Neat, open, and reproducible.

## Results

[Here](https://www.devitoproject.org/thematrix/)

## The matrix

| Arch    | Machine ID      |  JIT  | MPI      |  OMP     | MPI+OMP  | OMP5     | MPI+OMP5 |   ACC    | MPI+ACC  |
|---------|-----------------|-------|----------|----------| -------- | -------- | -------- | -------- | -------- |
| 1x1-CPU | Intel Xeon      | icc20 | :hammer: | :hammer: | :hammer: | :x:      | :x:      | :hammer: | :hammer: |
| 1xN-CPU | Intel Xeon      | icc20 | :hammer: | :hammer: | :hammer: | :x:      | :x:      | :hammer: | :hammer: |
| NxN-CPU | Intel Xeon      | icc20 | :hammer: | :hammer: | :hammer: | :x:      | :x:      | :hammer: | :hammer: |
| 1x1-CPU | Intel Xeon      | gcc10 | :hammer: | :hammer: | :hammer: | :x:      | :x:      | :hammer: | :hammer: |
| 1xN-CPU | Intel Xeon      | gcc10 | :hammer: | :hammer: | :hammer: | :x:      | :x:      | :hammer: | :hammer: |
| NxN-CPU | Intel Xeon      | gcc10 | :hammer: | :hammer: | :hammer: | :x:      | :x:      | :hammer: | :hammer: |
| 1x1-CPU | AMD    ????     | aocc  | :hammer: | :hammer: | :hammer: | :x:      | :x:      | :hammer: | :hammer: |
| 1xN-CPU | AMD    ????     | aocc  | :hammer: | :hammer: | :hammer: | :x:      | :x:      | :hammer: | :hammer: |
| NxN-CPU | AMD    ????     | aocc  | :hammer: | :hammer: | :hammer: | :x:      | :x:      | :hammer: | :hammer: |
| 1x1-GPU | NVidia V100     | pgi   | :x:      | :x:      | :x:      | :hammer: | :x:      | :hammer: | :x:      |
| 1xN-GPU | NVidia V100     | pgi   | :x:      | :x:      | :x:      | :hammer: | :hammer: | :hammer: | :hammer: |
| NxN-GPU | NVidia V100     | pgi   | :x:      | :x:      | :x:      | :x:      | :hammer: | :x:      | :hammer: |
| 1x1-GPU | AMD    ????     | aomp  | :x:      | :x:      | :x:      | :hammer: | :x:      | :x:      | :x:      |
| 1xN-GPU | AMD    ????     | aomp  | :x:      | :x:      | :x:      | :hammer: | :hammer: | :x:      | :x:      |
| NxN-GPU | AMD    ????     | aomp  | :x:      | :x:      | :x:      | :x:      | :hammer: | :x:      | :x:      |

Legend:
* :x: : not available / impossible
* :hammer: : work in progress
* :heavy_check_mark: : done


## Rational

* Need to ensure benchmarking is done properly and in a reproducible manner for
  reporting and publishing purposes.
* A starting point for performance optimisation and performance regression
  testing.
* Extendible for new architectures, compilers etc.
* Open to everybody -- pretty much unique in the field.

## Performance metrics

* GFLOPS
* GPOINTS
* Runtime
