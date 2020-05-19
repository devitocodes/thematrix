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

| Machine ID           | Mode |  JIT   |    MPI   |         OMP        |      MPI+OMP       |        OMP         | MPI+OMP  |         ACC        |      MPI+ACC       |
|----------------------|------|--------|----------|--------------------|--------------------|--------------------|----------|--------------------|--------------------|
| AZ-VM Intel 8168     | 1x1  | gcc7   | :hammer: | :heavy_check_mark: | :hammer:           | :x:                | :x:      | :hammer:           | :hammer:           |
| AZ-VM Intel 8168     | 1x2  | gcc7   | :hammer: | :x:                | :heavy_check_mark: | :x:                | :x:      | :hammer:           | :hammer:           |
| AZ-VM Intel 8168     | NxM  | gcc7   | :hammer: | :x:                | :hammer:           | :x:                | :x:      | :hammer:           | :hammer:           |
| AZ-VM Intel 8168     | 1x1  | gcc10  | :hammer: | :hammer:           | :hammer:           | :x:                | :x:      | :hammer:           | :hammer:           |
| AZ-VM Intel 8168     | 1xM  | gcc10  | :hammer: | :x:                | :hammer:           | :x:                | :x:      | :hammer:           | :hammer:           |
| AZ-VM Intel 8168     | NxM  | gcc10  | :hammer: | :x:                | :hammer:           | :x:                | :x:      | :hammer:           | :hammer:           |
| AZ-VM Intel 8168     | 1x1  | icc20  | :hammer: | :hammer:           | :hammer:           | :x:                | :x:      | :hammer:           | :hammer:           |
| AZ-VM Intel 8168     | 1xM  | icc20  | :hammer: | :x:                | :hammer:           | :x:                | :x:      | :hammer:           | :hammer:           |
| AZ-VM Intel 8168     | NxM  | icc20  | :hammer: | :x:                | :hammer:           | :x:                | :x:      | :hammer:           | :hammer:           |
| AZ-HPC Intel E5-2667 | 1x1  | gcc7   | :hammer: | :heavy_check_mark: | :hammer:           | :x:                | :x:      | :hammer:           | :hammer:           |
| AZ-HPC Intel E5-2667 | 1x2  | gcc7   | :hammer: | :x:                | :heavy_check_mark: | :x:                | :x:      | :hammer:           | :hammer:           |
| AZ-HPC Intel E5-2667 | NxM  | gcc7   | :hammer: | :x:                | :hammer:           | :x:                | :x:      | :hammer:           | :hammer:           |
| AZ-HPC Intel E5-2667 | 1x1  | gcc10  | :hammer: | :hammer:           | :hammer:           | :x:                | :x:      | :hammer:           | :hammer:           |
| AZ-HPC Intel E5-2667 | 1xM  | gcc10  | :hammer: | :x:                | :hammer:           | :x:                | :x:      | :hammer:           | :hammer:           |
| AZ-HPC Intel E5-2667 | NxM  | gcc10  | :hammer: | :x:                | :hammer:           | :x:                | :x:      | :hammer:           | :hammer:           |
| AZ-HPC Intel E5-2667 | 1x1  | icc20  | :hammer: | :hammer:           | :hammer:           | :x:                | :x:      | :hammer:           | :hammer:           |
| AZ-HPC Intel E5-2667 | 1xM  | icc20  | :hammer: | :x:                | :hammer:           | :x:                | :x:      | :hammer:           | :hammer:           |
| AZ-HPC Intel E5-2667 | NxM  | icc20  | :hammer: | :x:                | :hammer:           | :x:                | :x:      | :hammer:           | :hammer:           |
| ????   AMD    ????   | 1x1  | aocc   | :hammer: | :hammer:           | :hammer:           | :x:                | :x:      | :hammer:           | :hammer:           |
| ????   AMD    ????   | 1xM  | aocc   | :hammer: | :hammer:           | :hammer:           | :x:                | :x:      | :hammer:           | :hammer:           |
| ????   AMD    ????   | NxM  | aocc   | :hammer: | :hammer:           | :hammer:           | :x:                | :x:      | :hammer:           | :hammer:           |
| AZ-VM NVidia K80     | 1x1  | clang9 | :x:      | :x:                | :x:                | :heavy_check_mark: | :x:      | :hammer:           | :x:                |
| AZ-VM NVidia K80     | 1x2  | clang9 | :x:      | :x:                | :x:                | :hammer:           | :hammer: | :hammer:           | :hammer:           |
| AZ-VM NVidia K80     | NxM  | clang9 | :x:      | :x:                | :x:                | :x:                | :hammer: | :x:                | :hammer:           |
| AZ-VM NVidia K80     | 1x1  | pgi19  | :x:      | :x:                | :x:                | :hammer:           | :x:      | :heavy_check_mark: | :x:                |
| AZ-VM NVidia K80     | 1x2  | pgi19  | :x:      | :x:                | :x:                | :hammer:           | :hammer: | :hammer:           | :heavy_check_mark: |
| AZ-VM NVidia K80     | NxM  | pgi19  | :x:      | :x:                | :x:                | :x:                | :hammer: | :x:                | :hammer:           |
| ????   NVidia V100   | 1x1  | pgi19  | :x:      | :x:                | :x:                | :hammer:           | :x:      | :hammer:           | :x:                |
| ????   NVidia V100   | 1xM  | pgi19  | :x:      | :x:                | :x:                | :hammer:           | :hammer: | :hammer:           | :hammer:           |
| ????   NVidia V100   | NxM  | pgi19  | :x:      | :x:                | :x:                | :x:                | :hammer: | :x:                | :hammer:           |
| ????   AMD    ????   | 1x1  | aomp   | :x:      | :x:                | :x:                | :hammer:           | :x:      | :x:                | :x:                |
| ????   AMD    ????   | 1xM  | aomp   | :x:      | :x:                | :x:                | :hammer:           | :hammer: | :x:                | :x:                |
| ????   AMD    ????   | NxM  | aomp   | :x:      | :x:                | :x:                | :x:                | :hammer: | :x:                | :x:                |

Legend:
* AZ-VM : Azure Virtual Machine
* AZ-HPC : Azure HPC Machine
* OP-HPC : On-prem HPC Machine (undisclosed donor)
* Mode NxM : N=#nodes, M=#sockets(or #gpus)
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
