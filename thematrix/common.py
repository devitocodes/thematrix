import os
import sys
from subprocess import check_call

from tempfile import gettempdir

from devito import configuration, info, __version__ as devito_version
from devito.types.dense import DiscreteFunction
from benchmarks.user import benchmark

__all__ = ['check_norms', 'make_unique_filename', 'run_benchmark']


def check_norms(fn_norms, reference):
    with open(fn_norms, 'r') as f:
        norms = eval(f.read())

    assert isinstance(norms, dict)
    assert isinstance(reference, dict)
    assert set(norms) == set(reference)

    for k, v in norms:
        norm = float(v)
        info("norm(%s) = %f (expected = %f, delta = %f)"
             % (k, norm, reference[k], abs(norm - reference[k])))


def make_unique_filename(problem, shape, space_order):
    # Analyze setup for shared-memory execution (CPU vs GPU, OpenMP vs OpenACC vs ...)
    if 'DEVITO_PLATFORM' not in os.environ:
        raise RuntimeError("DEVITO_PLATFORM must be set to run TheMatrix")
    platform = os.environ['DEVITO_PLATFORM']

    if 'DEVITO_LANGUAGE' not in os.environ:
        raise RuntimeError("DEVITO_LANGUAGE must be set to run TheMatrix")
    language = os.environ['DEVITO_LANGUAGE']
    if language == "openmp":
        language = "omp"
    elif language == "openacc":
        language = "acc"
    else:
        assert language == "C"
        raise RuntimeError("Cannot run TheMatrix with DEVITO_LANGUAGE=C")

    if platform not in ['amdX', 'nvidiaX']:
        if language == "omp" and "OMP_NUM_THREADS" not in os.environ:
            raise RuntimeError("OMP_NUM_THREADS must be set to run TheMatrix with "
                               "DEVITO_LANGUAGE=openmp on a CPU")
        elif language == "acc":
            raise NotImplementedError("Trying to run OpenACC on CPU ?")

    shmmode = "%s-%s" % (platform, language)

    # Analyze setup for distributed-memory execution (MPI)
    if 'MPI_NUM_PROCS' not in os.environ:
        raise RuntimeError("MPI_NUM_PROCS must be set to run TheMatrix")
    nprocs = int(os.environ['MPI_NUM_PROCS'])
    if nprocs > 1:
        if 'DEVITO_MPI' not in os.environ:
            raise RuntimeError("Running with more than 1 MPI process, so DEVITO_MPI "
                               "must be set to run TheMatrix")
        mpimode = "mpi-%s-%d" % (os.environ['DEVITO_MPI'], nprocs)
    else:
        mpimode = "nompi"

    # Create unique filename
    template = '%s_shape%s_so%d_%s_%s_devito%s'
    fn = template % (problem,
                     str(shape).replace(" ", ""),
                     space_order,
                     shmmode,
                     mpimode,
                     devito_version.split('.')[1])
    fn = os.path.join(gettempdir(), fn)

    # Append suffixes
    fn_perf = "%s.asv" % fn
    fn_norms = "%s.norms" % fn

    return fn_perf, fn_norms


def run_benchmark(problem, shape, space_order, tn, fn_perf, fn_norms):
    pyversion = sys.executable

    program = benchmark.__file__

    command = [pyversion, program, 'run', '-P', problem]
    command.extend(['-d'] + [str(i) for i in shape])
    command.extend(['-so', str(space_order)])
    command.extend(['--tn', str(tn)])
    command.extend(['--dump-summary', fn_perf])
    command.extend(['--dump-norms', fn_norms])
    command.extend(['--autotune', 'off'])  # TODO: Drop me

    check_call(command)
