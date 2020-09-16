import os
import sys
from subprocess import check_call

from tempfile import gettempdir

from devito import configuration, info, __version__ as devito_version
from devito.compiler import sniff_mpi_distro
from devito.types.dense import DiscreteFunction
from benchmarks.user import benchmark
import benchmarks.user.advisor.run_advisor as run_advisor
import benchmarks.user.advisor.roofline as roofline
import benchmarks.user.advisor.advisor_to_json as advisor_to_json

__all__ = ['check_norms', 'run_prepare', 'run_benchmark', 'run_rooflines']


def check_norms(fn_norms, reference):
    with open(fn_norms, 'r') as f:
        norms = eval(f.read())

    assert isinstance(norms, dict)
    assert isinstance(reference, dict)
    assert set(norms) == set(reference)

    for k, v in norms.items():
        norm = float(v)
        info("norm(%s) = %f (expected = %f, delta = %f)"
             % (k, norm, reference[k], abs(norm - reference[k])))


def run_prepare(problem, shape, space_order):
    identifier = _generate_problem_identifier(problem, shape, space_order)
    fn = os.path.join(gettempdir(), identifier)
    # Append suffixes
    fn_perf = "%s.asv" % fn
    fn_norms = "%s.norms" % fn

    return fn_perf, fn_norms

def _generate_problem_identifier(problem, shape, space_order):
    """
    Generates a unique identifier for a given problem, useful for file creation.

    """
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

    if platform in ['amdX', 'nvidiaX']:
        for i in ['OMP_NUM_THREADS', 'OMP_PLACES', 'OMP_PROC_BIND']:
            try:
                v = os.environ.pop(i, None)
                if v:
                    raise RuntimeError("%s cannot be set to `%s` with DEVITO_PLATFORM=%s"
                                       % (i, v, platform))
            except KeyError:
                pass
    else:
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
    identifier = template % (problem,
                     str(shape).replace(" ", ""),
                     space_order,
                     shmmode,
                     mpimode,
                     devito_version.split('.')[1])
    return identifier

def mpiify_command(command):
    # Is it with MPI? If so, add mpi arguments to command.
    assert 'MPI_NUM_PROCS' in os.environ
    nprocs = int(os.environ['MPI_NUM_PROCS'])
    if nprocs > 1:
        assert 'DEVITO_MPI' in os.environ
        mpi_distro = sniff_mpi_distro(mpicmd)
        if mpi_distro == "OpenMPI":
            command.extend(['mpirun', '-n', str(nprocs), '--bind-to', 'socket'])
        elif mpi_distro == "MPICH":
            command.extend(['mpirun', '-n', str(nprocs), '--bind-to', 'socket'])
        elif mpi_distro == "IntelMPI":
            command.extend(['mpirun', '-n', str(nprocs), '--bind-to', 'socket'])
        else:
            raise RuntimeError("Unknown MPI distribution")


def run_benchmark(problem, shape, space_order, tn, fn_perf, fn_norms, op='forward'):
    pyversion = sys.executable
    mpicmd = "mpirun"

    command = []

    mpiify_command(command)

    command.extend([pyversion, benchmark.__file__, 'run', '-P', problem])
    command.extend(['-d'] + [str(i) for i in shape])
    command.extend(['-so', str(space_order)])
    command.extend(['--tn', str(tn)])
    command.extend(['--dump-summary', fn_perf])
    command.extend(['--dump-norms', fn_norms])
    command.extend(['--operator', op])
    command.extend(['--autotune', 'off'])  # TODO: Drop me


    check_call(command)


def run_rooflines(ident, problem, shape, space_order, tn, op='forward'):
    """
    Generates rooflines using every rooflining tool available.
    Currently available rooflining tools:
    - Intel Advisor

    """

    _run_roofline_advisor(ident, problem, shape, space_order, tn, op)


def _run_roofline_advisor(ident, problem, shape, space_order, tn, op):
    """
    Generates a performance roofline (image + data) using Intel Advisor.

    """

    pyversion = sys.executable
    mpicmd = "mpirun"

    advisor_command = []
    roofline_command = []
    json_command = []

    mpiify_command(advisor_command)

    # Autogenerate the unique identifier for the program
    ident = _generate_problem_identifier(ident, shape, space_order)

    tmp_results = os.path.join(gettempdir(), ident)
    profiling_dir = '%s_advisor_profiling' % ident
    roof_image = '%s_advisor_roof_overview' % ident
    roof_data = '%s_advisor_roof_data' % ident

    image_path = os.path.join(full_result_path, roof_image)
    data_path = os.path.join(full_result_path, roof_data)

    # First, build the command to run profiling on Advisor
    advisor_command.extend([pyversion, run_advisor.__file__])
    advisor_command.extend(['--path', benchmark.__file__])
    advisor_command.extend(['--exec-args', 'run -P ' + problem + ' -d ' +
                            ' '.join([str(i) for i in shape]) + ' -so ' +
                            str(space_order) + ' --tn ' + str(tn) +
                            ' --operator ' + op + ' --autotune off'])
    advisor_command.extend(['--output', tmp_results])
    advisor_command.extend(['--name', profiling_dir])

    # Second, build the command to generate the roofline in png format
    roofline_command.extend([pyversion, roofline.__file__])
    roofline_command.extend(['--mode', 'overview'])
    roofline_command.extend(['--name', image_path])
    roofline_command.extend(['--project', tmp_results])

    # Third, build the command to extract the roofline data in JSON format
    json_command.extend([pyversion, advisor_to_json.__file__])
    json_command.extend(['--name', data_path])
    json_command.extend(['--project', tmp_results])

    # Run all three commands subsequently
    if check_call(advisor_command) == 0:
      check_call(roofline_command)
      check_call(json_command)
