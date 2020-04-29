# Devito benchmark matrix

## Roadmap

| Arch    | Brand  | Model |  JIT  | MPI      |  OMP     | MPI+OMP  | OMP5     | MPI+OMP5 |   ACC    | MPI+ACC  |
|---------|--------|-------|-------|----------|----------| -------- | -------- | -------- | -------- | -------- |
| 1x1-CPU | Intel  | Xeon  | icc20 | :hammer: | :hammer: | :hammer: | :x:      | :x:      | :hammer: | :hammer: |
| 1xN-CPU | Intel  | Xeon  | icc20 | :hammer: | :hammer: | :hammer: | :x:      | :x:      | :hammer: | :hammer: |
| NxN-CPU | Intel  | Xeon  | icc20 | :hammer: | :hammer: | :hammer: | :x:      | :x:      | :hammer: | :hammer: |
| 1x1-CPU | Intel  | Xeon  | gcc10 | :hammer: | :hammer: | :hammer: | :x:      | :x:      | :hammer: | :hammer: |
| 1xN-CPU | Intel  | Xeon  | gcc10 | :hammer: | :hammer: | :hammer: | :x:      | :x:      | :hammer: | :hammer: |
| NxN-CPU | Intel  | Xeon  | gcc10 | :hammer: | :hammer: | :hammer: | :x:      | :x:      | :hammer: | :hammer: |
| 1x1-CPU | AMD    | ????  | aocc  | :hammer: | :hammer: | :hammer: | :x:      | :x:      | :hammer: | :hammer: |
| 1xN-CPU | AMD    | ????  | aocc  | :hammer: | :hammer: | :hammer: | :x:      | :x:      | :hammer: | :hammer: |
| NxN-CPU | AMD    | ????  | aocc  | :hammer: | :hammer: | :hammer: | :x:      | :x:      | :hammer: | :hammer: |
| 1x1-GPU | NVidia | V100  | pgi   | :x:      | :x:      | :x:      | :hammer: | :x:      | :hammer: | :x:      |
| 1xN-GPU | NVidia | V100  | pgi   | :x:      | :x:      | :x:      | :hammer: | :hammer: | :hammer: | :hammer: |
| NxN-GPU | NVidia | V100  | pgi   | :x:      | :x:      | :x:      | :x:      | :hammer: | :x:      | :hammer: |
| 1x1-GPU | AMD    | ????  | aomp  | :x:      | :x:      | :x:      | :hammer: | :x:      | :x:      | :x:      |
| 1xN-GPU | AMD    | ????  | aomp  | :x:      | :x:      | :x:      | :hammer: | :hammer: | :x:      | :x:      |
| NxN-GPU | AMD    | ????  | aomp  | :x:      | :x:      | :x:      | :x:      | :hammer: | :x:      | :x:      |

Legend:
* :x: : not available / impossible
* :hammer: : work in progress
* :heavy_check_mark: : done


## Rational:
* Need to ensure benchmarking is done properly and in a reproducible manner for reporting/publishing purposes.
* This is a starting point for performance optimisation and performance regression testing.
* Reruns of the Rice hackathon.
* Extendible for new architectures, compilers etc.

## Objectives:
What are we trying to measure? Performance on a single node. This must be done before any valid MPI benchmark (MPI will be covered in a followup hackathon).
* GFLOPS
* GPts/s
* Performance regression with Airspeed Velocity. 

## Creating the benchmark matrix.
* Revive/generalise  https://github.com/DevitoHack-oghpc2020/starter to automate running the benchmark matrix and updating webpage.
* Columns: [Intel CPU’s, AMD CPU’s, NVidia GPU’s, AMD GPU’s]. (limiting ourselves to Azure VM’s)
* Rows: [3D isotropic acoustic, TTI] x (different programming models) x (compilers)
* OpenMP (GCC, LLVM, PGI) (CPU’s)
* OpenMP offloading (GCC, LLVM, PGI)
* OpenACC (PGI, GCC, LLVM)
* Container files for different configurations to ensure reproducibility.
* Add Airspeed velocity link to each element of the matrix (complete PR #1074 first).

Update documentation:
* Problem specification.
* Dev/user environment (what compilers and how to install them etc).
* How to run benchmark by hand?

General comments
* Reuse effort/work between CI and benchmarking?
* Hackathon to divide up the workload?
* GitHub project; open issues/backlog
* Hackathon similar to what we did for GitHub actions?
* Participants: send invite to all #development, Microsoft, NVidia, AMD, Intel. 

## Outline of workflow
* \<some-event-tbd\> triggers benchmark action.
  * Matrix of jobs: (3D isotropic acoustic, tti, tti gradient) x (different architectures) x (different programming models)
  * Each job:
    * Runs benchmark using ASV; creates/updates directry under `thematrix/benchmarks`.
    * Loop git pull/push until success:
      * ASV publish.
