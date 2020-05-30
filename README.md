<p align="center">
  <img src="https://raw.githubusercontent.com/devitocodes/devito/master/docs/source/_static/devito_logo.png">
</p>

# TheMatrix -- Devito benchmark matrix

Benchmarking Devito solvers across computer architectures, execution models, compilers and anything else we can think of.

[![Run TheMatrix](https://img.shields.io/badge/run-thematrix-brightgreen)](https://www.actionspanel.app/app/devitocodes/thematrix)
[![asv](http://img.shields.io/badge/benchmarked%20by-asv-blue.svg?style=flat)](https://devitocodes.github.io/devito-performance)
[![Slack Status](https://img.shields.io/badge/chat-on%20slack-%2336C5F0)](https://opesci-slackin.now.sh)

The aim of TheMatrix is to:

* Create a platform to enable automated benchmarking across many platforms.
* Perform benchmarking in an open and reproducible manner.
* Make it extendible to new architectures, compilers etc.
* Provide performance baseline for performance optimisation; catch performance regression.

Matrix benchmark parameters include:
* Architecture: Intel® Xeon® Platinum 8168 processor (Azure), Intel Xeon E5 2667 v3 (Azure), NVIDIA Tesla K80 (Azure)
* Execution models: OpenMP, OpenMP offloading, OpenACC, MPI
* Compilers: GCC, LLVM, PGI
* Numerical solvers: isotropic acoustic (3D), TTI (3D)
* Profilers: native performance metrics (runtime, FLOPS, GPt/s), [Air Speed velocity](https://asv.readthedocs.io/en/stable/index.html).

If there is something missing that you would like to see in the matrix then please then let us know...particularly if you can contribute development effort, hardware or funding!

## The matrix of platforms tested
The table below provides a summary of the various platforms and configurations included in TheMatrix suite. Click on the links in the table for explanations and [click here](https://htmlpreview.github.io/?https://raw.githubusercontent.com/devitocodes/thematrix/generate_readme/thematrix/thematrix.html) for further details.

<table border="1" class="dataframe">  <thead>    <tr style="text-align: right;">      <th></th>      <th>Runtime specification</th>      <th>Hardware</th>    </tr>  </thead>  <tbody>    <tr>      <th><a href="https://docs.microsoft.com/en-us/azure/virtual-machines/fsv2-series">Standard-F64s-v2</a><br>ubuntu18.04<br>x86_64</th>      <td><table border="1" class="dataframe">  <thead>    <tr style="text-align: right;">      <th>Compiler</th>      <th><a href="https://github.com/devitocodes/devito/wiki/FAQ#DEVITO_MPI">MPI mode</a>,<br>number of ranks</th>      <th><a href="https://github.com/devitocodes/devito/wiki/FAQ#devito_language">Execution model</a></th>    </tr>  </thead>  <tbody>    <tr>      <td>gcc-9</td>      <td></td>      <td>openmp</td>    </tr>    <tr>      <td>gcc-9</td>      <td>basic, 2</td>      <td>openmp</td>    </tr>  </tbody></table></td>      <td>x86_64</td>    </tr>    <tr>      <th><a href="https://docs.microsoft.com/en-us/azure/virtual-machines/h-series">Standard-H16</a><br>ubuntu18.04<br>x86_64</th>      <td><table border="1" class="dataframe">  <thead>    <tr style="text-align: right;">      <th>Compiler</th>      <th><a href="https://github.com/devitocodes/devito/wiki/FAQ#DEVITO_MPI">MPI mode</a>,<br>number of ranks</th>      <th><a href="https://github.com/devitocodes/devito/wiki/FAQ#devito_language">Execution model</a></th>    </tr>  </thead>  <tbody>    <tr>      <td>gcc-9</td>      <td></td>      <td>openmp</td>    </tr>  </tbody></table></td>      <td>x86_64</td>    </tr>    <tr>      <th><a href="https://docs.microsoft.com/en-us/azure/virtual-machines/nc-series">Standard-NC6-Promo</a><br>ubuntu18.04<br>kepler</th>      <td><table border="1" class="dataframe">  <thead>    <tr style="text-align: right;">      <th>Compiler</th>      <th><a href="https://github.com/devitocodes/devito/wiki/FAQ#DEVITO_MPI">MPI mode</a>,<br>number of ranks</th>      <th><a href="https://github.com/devitocodes/devito/wiki/FAQ#devito_language">Execution model</a></th>    </tr>  </thead>  <tbody>    <tr>      <td>clang</td>      <td></td>      <td>openmp</td>    </tr>    <tr>      <td>pgi</td>      <td></td>      <td>openacc</td>    </tr>  </tbody></table></td>      <td>kepler</td>    </tr>    <tr>      <th><a href="https://docs.microsoft.com/en-us/azure/virtual-machines/nc-series">Standard-NC24-Promo</a><br>ubuntu18.04<br>kepler</th>      <td><table border="1" class="dataframe">  <thead>    <tr style="text-align: right;">      <th>Compiler</th>      <th><a href="https://github.com/devitocodes/devito/wiki/FAQ#DEVITO_MPI">MPI mode</a>,<br>number of ranks</th>      <th><a href="https://github.com/devitocodes/devito/wiki/FAQ#devito_language">Execution model</a></th>    </tr>  </thead>  <tbody>    <tr>      <td>pgi</td>      <td>basic, 4</td>      <td>openacc</td>    </tr>  </tbody></table></td>      <td>kepler</td>    </tr>  </tbody></table>

## Profiling results
This table provides a summary of the numerical models benchmarked - [click here for verbosity](https://htmlpreview.github.io/?https://raw.githubusercontent.com/devitocodes/thematrix/generate_readme/results/benchmarks.html). Click on the links in the table for profiling results.

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Airspeed velocity</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>acoustic_iso.IsotropicAcoustic.track_gflopss</th>
      <td><a href="https://www.devitoproject.org/thematrix/#acoustic_iso.IsotropicAcoustic.track_gflopss">  <figure>    <img src="https://www.devitoproject.org/thematrix/swallow.png"    alt="Airspeed velocity"</img>  </figure></a></td>
    </tr>
    <tr>
      <th>acoustic_iso.IsotropicAcoustic.track_gpointss</th>
      <td><a href="https://www.devitoproject.org/thematrix/#acoustic_iso.IsotropicAcoustic.track_gpointss">  <figure>    <img src="https://www.devitoproject.org/thematrix/swallow.png"    alt="Airspeed velocity"</img>  </figure></a></td>
    </tr>
    <tr>
      <th>acoustic_iso.IsotropicAcoustic.track_runtime</th>
      <td><a href="https://www.devitoproject.org/thematrix/#acoustic_iso.IsotropicAcoustic.track_runtime">  <figure>    <img src="https://www.devitoproject.org/thematrix/swallow.png"    alt="Airspeed velocity"</img>  </figure></a></td>
    </tr>
    <tr>
      <th>acoustic_tti.TTIAcoustic.track_gflopss</th>
      <td><a href="https://www.devitoproject.org/thematrix/#acoustic_tti.TTIAcoustic.track_gflopss">  <figure>    <img src="https://www.devitoproject.org/thematrix/swallow.png"    alt="Airspeed velocity"</img>  </figure></a></td>
    </tr>
    <tr>
      <th>acoustic_tti.TTIAcoustic.track_gpointss</th>
      <td><a href="https://www.devitoproject.org/thematrix/#acoustic_tti.TTIAcoustic.track_gpointss">  <figure>    <img src="https://www.devitoproject.org/thematrix/swallow.png"    alt="Airspeed velocity"</img>  </figure></a></td>
    </tr>
    <tr>
      <th>acoustic_tti.TTIAcoustic.track_runtime</th>
      <td><a href="https://www.devitoproject.org/thematrix/#acoustic_tti.TTIAcoustic.track_runtime">  <figure>    <img src="https://www.devitoproject.org/thematrix/swallow.png"    alt="Airspeed velocity"</img>  </figure></a></td>
    </tr>
  </tbody>
</table>

### Performance metrics
See the [Devito FAQ](https://github.com/devitocodes/devito/wiki/FAQ) for details on [how Devito computes the performance of an operator](https://github.com/devitocodes/devito/wiki/FAQ#how-does-devito-compute-the-performance-of-an-operator).
* GFLOPS - giga floating point operations per second
* FD-GPts/s - finite-difference giga grid points per second 
* Runtime