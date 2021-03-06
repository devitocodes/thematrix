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
The table below provides a summary of the various platforms and configurations included in TheMatrix suite. Click on the links in the table for explanations and [click here](https://htmlpreview.github.io/?https://github.com/devitocodes/thematrix/blob/master/thematrix/thematrix.html) for further details.

<table border="1" class="dataframe">  <thead>    <tr style="text-align: right;">      <th></th>      <th>queue</th>      <th>Runtime specification</th>      <th>Hardware</th>    </tr>  </thead>  <tbody>    <tr>      <th><a href="https://docs.microsoft.com/en-us/azure/virtual-machines/fsv2-series">Standard-F64s-v2</a></th>      <td>azure</td>      <td><table border="1" class="dataframe">  <thead>    <tr style="text-align: right;">      <th>Compiler</th>      <th><a href="https://github.com/devitocodes/devito/wiki/FAQ#DEVITO_MPI">MPI mode</a>,<br>#ranks</th>      <th><a href="https://github.com/devitocodes/devito/wiki/FAQ#devito_language">Execution model</a></th>    </tr>  </thead>  <tbody>    <tr>      <td>gcc-9</td>      <td></td>      <td>OpenMP</td>    </tr>    <tr>      <td>gcc-9</td>      <td>basic, 2</td>      <td>OpenMP</td>    </tr>  </tbody></table></td>      <td>x86_64</td>    </tr>    <tr>      <th><a href="https://docs.microsoft.com/en-us/azure/virtual-machines/hc-series">Standard-HC44rs</a></th>      <td>azure</td>      <td><table border="1" class="dataframe">  <thead>    <tr style="text-align: right;">      <th>Compiler</th>      <th><a href="https://github.com/devitocodes/devito/wiki/FAQ#DEVITO_MPI">MPI mode</a>,<br>#ranks</th>      <th><a href="https://github.com/devitocodes/devito/wiki/FAQ#devito_language">Execution model</a></th>    </tr>  </thead>  <tbody>    <tr>      <td>gcc-9</td>      <td>basic, 2</td>      <td>OpenMP</td>    </tr>  </tbody></table></td>      <td>x86_64</td>    </tr>    <tr>      <th><a href="https://docs.microsoft.com/en-us/azure/virtual-machines/h-series">Standard-H16</a></th>      <td>azure</td>      <td><table border="1" class="dataframe">  <thead>    <tr style="text-align: right;">      <th>Compiler</th>      <th><a href="https://github.com/devitocodes/devito/wiki/FAQ#DEVITO_MPI">MPI mode</a>,<br>#ranks</th>      <th><a href="https://github.com/devitocodes/devito/wiki/FAQ#devito_language">Execution model</a></th>    </tr>  </thead>  <tbody>    <tr>      <td>gcc-9</td>      <td></td>      <td>OpenMP</td>    </tr>  </tbody></table></td>      <td>x86_64</td>    </tr>    <tr>      <th><a href="https://docs.microsoft.com/en-us/azure/virtual-machines/hb-series">Standard-HB60rs</a></th>      <td>azure</td>      <td><table border="1" class="dataframe">  <thead>    <tr style="text-align: right;">      <th>Compiler</th>      <th><a href="https://github.com/devitocodes/devito/wiki/FAQ#DEVITO_MPI">MPI mode</a>,<br>#ranks</th>      <th><a href="https://github.com/devitocodes/devito/wiki/FAQ#devito_language">Execution model</a></th>    </tr>  </thead>  <tbody>    <tr>      <td>gcc-9</td>      <td>basic, 2</td>      <td>OpenMP</td>    </tr>  </tbody></table></td>      <td>x86_64</td>    </tr>    <tr>      <th><a href="https://docs.microsoft.com/en-us/azure/virtual-machines/nc-series">Standard-NC6-Promo</a></th>      <td>azure</td>      <td><table border="1" class="dataframe">  <thead>    <tr style="text-align: right;">      <th>Compiler</th>      <th><a href="https://github.com/devitocodes/devito/wiki/FAQ#DEVITO_MPI">MPI mode</a>,<br>#ranks</th>      <th><a href="https://github.com/devitocodes/devito/wiki/FAQ#devito_language">Execution model</a></th>    </tr>  </thead>  <tbody>    <tr>      <td>clang</td>      <td></td>      <td>OpenMP</td>    </tr>    <tr>      <td>pgi</td>      <td></td>      <td>OpenACC</td>    </tr>  </tbody></table></td>      <td>kepler</td>    </tr>    <tr>      <th><a href="https://docs.microsoft.com/en-us/azure/virtual-machines/nc-series">Standard-NC24-Promo</a></th>      <td>azure</td>      <td><table border="1" class="dataframe">  <thead>    <tr style="text-align: right;">      <th>Compiler</th>      <th><a href="https://github.com/devitocodes/devito/wiki/FAQ#DEVITO_MPI">MPI mode</a>,<br>#ranks</th>      <th><a href="https://github.com/devitocodes/devito/wiki/FAQ#devito_language">Execution model</a></th>    </tr>  </thead>  <tbody>    <tr>      <td>pgi</td>      <td>basic, 4</td>      <td>OpenACC</td>    </tr>  </tbody></table></td>      <td>kepler</td>    </tr>    <tr>      <th>gpu03-DUG-V100x4</th>      <td>dug</td>      <td><table border="1" class="dataframe">  <thead>    <tr style="text-align: right;">      <th>Compiler</th>      <th><a href="https://github.com/devitocodes/devito/wiki/FAQ#DEVITO_MPI">MPI mode</a>,<br>#ranks</th>      <th><a href="https://github.com/devitocodes/devito/wiki/FAQ#devito_language">Execution model</a></th>    </tr>  </thead>  <tbody>    <tr>      <td>pgi</td>      <td>basic, 4</td>      <td>OpenACC</td>    </tr>  </tbody></table></td>      <td>DUG</td>    </tr>  </tbody></table>

## Profiling results
This table provides a summary of the numerical models benchmarked - [click here for verbosity](https://htmlpreview.github.io/?https://github.com/devitocodes/thematrix/blob/master/results/benchmarks.html). Unless otherwise stated, models are three-dimensional, use 2nd order temporal and 12th order spatial discretizations, and single-precision floating point arithmetic. Click on the links in the table for profiling results and further information regarding the individual benchamrk.

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>GFLOPS</th>
      <th>FD-GPts/s</th>
      <th>Runtime</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>IsotropicAcousticForward</th>
      <td><a href="https://www.devitoproject.org/thematrix/#acoustic_iso.IsotropicAcousticForward.track_gflopss">  <figure>    <img src="https://www.devitoproject.org/thematrix/swallow.png"    alt="Airspeed velocity"</img>  </figure></a></td>
      <td><a href="https://www.devitoproject.org/thematrix/#acoustic_iso.IsotropicAcousticForward.track_gpointss">  <figure>    <img src="https://www.devitoproject.org/thematrix/swallow.png"    alt="Airspeed velocity"</img>  </figure></a></td>
      <td><a href="https://www.devitoproject.org/thematrix/#acoustic_iso.IsotropicAcousticForward.track_runtime">  <figure>    <img src="https://www.devitoproject.org/thematrix/swallow.png"    alt="Airspeed velocity"</img>  </figure></a></td>
    </tr>
    <tr>
      <th>IsotropicAcousticAdjoint</th>
      <td><a href="https://www.devitoproject.org/thematrix/#acoustic_iso_adj.IsotropicAcousticAdjoint.track_gflopss">  <figure>    <img src="https://www.devitoproject.org/thematrix/swallow.png"    alt="Airspeed velocity"</img>  </figure></a></td>
      <td><a href="https://www.devitoproject.org/thematrix/#acoustic_iso_adj.IsotropicAcousticAdjoint.track_gpointss">  <figure>    <img src="https://www.devitoproject.org/thematrix/swallow.png"    alt="Airspeed velocity"</img>  </figure></a></td>
      <td><a href="https://www.devitoproject.org/thematrix/#acoustic_iso_adj.IsotropicAcousticAdjoint.track_runtime">  <figure>    <img src="https://www.devitoproject.org/thematrix/swallow.png"    alt="Airspeed velocity"</img>  </figure></a></td>
    </tr>
    <tr>
      <th>IsotropicAcousticJacobian</th>
      <td><a href="https://www.devitoproject.org/thematrix/#acoustic_iso_jac.IsotropicAcousticJacobian.track_gflopss">  <figure>    <img src="https://www.devitoproject.org/thematrix/swallow.png"    alt="Airspeed velocity"</img>  </figure></a></td>
      <td><a href="https://www.devitoproject.org/thematrix/#acoustic_iso_jac.IsotropicAcousticJacobian.track_gpointss">  <figure>    <img src="https://www.devitoproject.org/thematrix/swallow.png"    alt="Airspeed velocity"</img>  </figure></a></td>
      <td><a href="https://www.devitoproject.org/thematrix/#acoustic_iso_jac.IsotropicAcousticJacobian.track_runtime">  <figure>    <img src="https://www.devitoproject.org/thematrix/swallow.png"    alt="Airspeed velocity"</img>  </figure></a></td>
    </tr>
    <tr>
      <th>IsotropicAcousticJacobianAdjoint</th>
      <td><a href="https://www.devitoproject.org/thematrix/#acoustic_iso_jacadj.IsotropicAcousticJacobianAdjoint.track_gflopss">  <figure>    <img src="https://www.devitoproject.org/thematrix/swallow.png"    alt="Airspeed velocity"</img>  </figure></a></td>
      <td><a href="https://www.devitoproject.org/thematrix/#acoustic_iso_jacadj.IsotropicAcousticJacobianAdjoint.track_gpointss">  <figure>    <img src="https://www.devitoproject.org/thematrix/swallow.png"    alt="Airspeed velocity"</img>  </figure></a></td>
      <td><a href="https://www.devitoproject.org/thematrix/#acoustic_iso_jacadj.IsotropicAcousticJacobianAdjoint.track_runtime">  <figure>    <img src="https://www.devitoproject.org/thematrix/swallow.png"    alt="Airspeed velocity"</img>  </figure></a></td>
    </tr>
    <tr>
      <th>IsotropicSSAForward</th>
      <td><a href="https://www.devitoproject.org/thematrix/#acoustic_iso_ssa.IsotropicSSAForward.track_gflopss">  <figure>    <img src="https://www.devitoproject.org/thematrix/swallow.png"    alt="Airspeed velocity"</img>  </figure></a></td>
      <td><a href="https://www.devitoproject.org/thematrix/#acoustic_iso_ssa.IsotropicSSAForward.track_gpointss">  <figure>    <img src="https://www.devitoproject.org/thematrix/swallow.png"    alt="Airspeed velocity"</img>  </figure></a></td>
      <td><a href="https://www.devitoproject.org/thematrix/#acoustic_iso_ssa.IsotropicSSAForward.track_runtime">  <figure>    <img src="https://www.devitoproject.org/thematrix/swallow.png"    alt="Airspeed velocity"</img>  </figure></a></td>
    </tr>
    <tr>
      <th>IsotropicSSAAdjoint</th>
      <td><a href="https://www.devitoproject.org/thematrix/#acoustic_iso_ssa_adj.IsotropicSSAAdjoint.track_gflopss">  <figure>    <img src="https://www.devitoproject.org/thematrix/swallow.png"    alt="Airspeed velocity"</img>  </figure></a></td>
      <td><a href="https://www.devitoproject.org/thematrix/#acoustic_iso_ssa_adj.IsotropicSSAAdjoint.track_gpointss">  <figure>    <img src="https://www.devitoproject.org/thematrix/swallow.png"    alt="Airspeed velocity"</img>  </figure></a></td>
      <td><a href="https://www.devitoproject.org/thematrix/#acoustic_iso_ssa_adj.IsotropicSSAAdjoint.track_runtime">  <figure>    <img src="https://www.devitoproject.org/thematrix/swallow.png"    alt="Airspeed velocity"</img>  </figure></a></td>
    </tr>
    <tr>
      <th>IsotropicSSAJacobian</th>
      <td><a href="https://www.devitoproject.org/thematrix/#acoustic_iso_ssa_jac.IsotropicSSAJacobian.track_gflopss">  <figure>    <img src="https://www.devitoproject.org/thematrix/swallow.png"    alt="Airspeed velocity"</img>  </figure></a></td>
      <td><a href="https://www.devitoproject.org/thematrix/#acoustic_iso_ssa_jac.IsotropicSSAJacobian.track_gpointss">  <figure>    <img src="https://www.devitoproject.org/thematrix/swallow.png"    alt="Airspeed velocity"</img>  </figure></a></td>
      <td><a href="https://www.devitoproject.org/thematrix/#acoustic_iso_ssa_jac.IsotropicSSAJacobian.track_runtime">  <figure>    <img src="https://www.devitoproject.org/thematrix/swallow.png"    alt="Airspeed velocity"</img>  </figure></a></td>
    </tr>
    <tr>
      <th>IsotropicSSAJacobianAdjoint</th>
      <td><a href="https://www.devitoproject.org/thematrix/#acoustic_iso_ssa_jacadj.IsotropicSSAJacobianAdjoint.track_gflopss">  <figure>    <img src="https://www.devitoproject.org/thematrix/swallow.png"    alt="Airspeed velocity"</img>  </figure></a></td>
      <td><a href="https://www.devitoproject.org/thematrix/#acoustic_iso_ssa_jacadj.IsotropicSSAJacobianAdjoint.track_gpointss">  <figure>    <img src="https://www.devitoproject.org/thematrix/swallow.png"    alt="Airspeed velocity"</img>  </figure></a></td>
      <td><a href="https://www.devitoproject.org/thematrix/#acoustic_iso_ssa_jacadj.IsotropicSSAJacobianAdjoint.track_runtime">  <figure>    <img src="https://www.devitoproject.org/thematrix/swallow.png"    alt="Airspeed velocity"</img>  </figure></a></td>
    </tr>
    <tr>
      <th>TTIAcousticForward</th>
      <td><a href="https://www.devitoproject.org/thematrix/#acoustic_tti.TTIAcousticForward.track_gflopss">  <figure>    <img src="https://www.devitoproject.org/thematrix/swallow.png"    alt="Airspeed velocity"</img>  </figure></a></td>
      <td><a href="https://www.devitoproject.org/thematrix/#acoustic_tti.TTIAcousticForward.track_gpointss">  <figure>    <img src="https://www.devitoproject.org/thematrix/swallow.png"    alt="Airspeed velocity"</img>  </figure></a></td>
      <td><a href="https://www.devitoproject.org/thematrix/#acoustic_tti.TTIAcousticForward.track_runtime">  <figure>    <img src="https://www.devitoproject.org/thematrix/swallow.png"    alt="Airspeed velocity"</img>  </figure></a></td>
    </tr>
    <tr>
      <th>TTIAcousticAdjoint</th>
      <td><a href="https://www.devitoproject.org/thematrix/#acoustic_tti_adj.TTIAcousticAdjoint.track_gflopss">  <figure>    <img src="https://www.devitoproject.org/thematrix/swallow.png"    alt="Airspeed velocity"</img>  </figure></a></td>
      <td><a href="https://www.devitoproject.org/thematrix/#acoustic_tti_adj.TTIAcousticAdjoint.track_gpointss">  <figure>    <img src="https://www.devitoproject.org/thematrix/swallow.png"    alt="Airspeed velocity"</img>  </figure></a></td>
      <td><a href="https://www.devitoproject.org/thematrix/#acoustic_tti_adj.TTIAcousticAdjoint.track_runtime">  <figure>    <img src="https://www.devitoproject.org/thematrix/swallow.png"    alt="Airspeed velocity"</img>  </figure></a></td>
    </tr>
    <tr>
      <th>Elastic</th>
      <td><a href="https://www.devitoproject.org/thematrix/#elastic.Elastic.track_gflopss">  <figure>    <img src="https://www.devitoproject.org/thematrix/swallow.png"    alt="Airspeed velocity"</img>  </figure></a></td>
      <td><a href="https://www.devitoproject.org/thematrix/#elastic.Elastic.track_gpointss">  <figure>    <img src="https://www.devitoproject.org/thematrix/swallow.png"    alt="Airspeed velocity"</img>  </figure></a></td>
      <td><a href="https://www.devitoproject.org/thematrix/#elastic.Elastic.track_runtime">  <figure>    <img src="https://www.devitoproject.org/thematrix/swallow.png"    alt="Airspeed velocity"</img>  </figure></a></td>
    </tr>
    <tr>
      <th>Viscoelastic</th>
      <td><a href="https://www.devitoproject.org/thematrix/#viscoelastic.Viscoelastic.track_gflopss">  <figure>    <img src="https://www.devitoproject.org/thematrix/swallow.png"    alt="Airspeed velocity"</img>  </figure></a></td>
      <td><a href="https://www.devitoproject.org/thematrix/#viscoelastic.Viscoelastic.track_gpointss">  <figure>    <img src="https://www.devitoproject.org/thematrix/swallow.png"    alt="Airspeed velocity"</img>  </figure></a></td>
      <td><a href="https://www.devitoproject.org/thematrix/#viscoelastic.Viscoelastic.track_runtime">  <figure>    <img src="https://www.devitoproject.org/thematrix/swallow.png"    alt="Airspeed velocity"</img>  </figure></a></td>
    </tr>
  </tbody>
</table>

### Performance metrics
See the [Devito FAQ](https://github.com/devitocodes/devito/wiki/FAQ) for details on [how Devito computes the performance of an operator](https://github.com/devitocodes/devito/wiki/FAQ#how-does-devito-compute-the-performance-of-an-operator).
* GFLOPS - giga floating point operations per second
* FD-GPts/s - finite-difference giga grid points per second 
* Runtime
