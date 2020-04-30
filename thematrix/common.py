import os

from tempfile import gettempdir

from devito import configuration, info, norm, __version__ as devito_version
from devito.types.dense import DiscreteFunction

__all__ = ['check_norms', 'make_unique_filename']


def check_norms(functions, reference):
    assert len(functions) == len(reference)

    for i in functions:
        if isinstance(i, DiscreteFunction):
            v = norm(i)
            info("norm(%s) = %f (expected = %f, delta = %f)"
                 % (i.name, v, reference[i.name], abs(v - reference[i.name])))


def make_unique_filename(problem, shape, space_order):
    if 'OMP_NUM_THREADS' not in os.environ:
        raise RuntimeError("OMP_NUM_THREADS must be set to run TheMatrix")
    nthreads = int(os.environ['OMP_NUM_THREADS'])

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

    template = '%s_shape%s_so%d_omp%d_%s_devito%s.asv'
    filename = template % (problem,
                           str(shape).replace(" ", ""),
                           space_order,
                           nthreads,
                           mpimode,
                           devito_version.split('.')[1])
    filename = os.path.join(gettempdir(), filename)

    return filename
