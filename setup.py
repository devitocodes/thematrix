import os
import subprocess
import sys
from setuptools import setup, find_packages


def install_custom_package(package, arguments=None, prefix=None):
    """
    Install packages with custom pip commands.
    """
    args = []
    args.extend(prefix or [])
    args.extend([sys.executable, "-m", "pip", "install"])
    args.extend(arguments or [])
    args.append(package)

    subprocess.check_call(args)


required = []
with open('requirements.txt') as f:
    for i in f.read().splitlines():
        if i[0:3] == 'git':
            name = i.split('/')[-1]
            required.append('%s @ %s@master' % (name, i))
        else:
            required.append(i)

# mpi4py needs to be install with custom commands on certain systems
mpi = os.environ.get('DEVITO_MPI')
if mpi == 0:
    required.remove('mpi4py')
if 'mpi4py' in required:
    jit = os.environ.get('DEVITO_ARCH')
    if jit in ['pgi', 'pgcc']:
        required.remove('mpi4py')

        # TODO: use `which mpicc` to get the path to `mpicc` dynamically
        prefix = ['env', 'MPICC=/opt/pgi/linux86-64/19.10/mpi/openmpi-3.1.3/bin/mpicc',
                  'CC=pgcc', 'CFLAGS=-noswitcherror']
        arguments = ['--no-cache-dir']
        install_custom_package('mpi4py', arguments, prefix)

setup(name='thematrix',
      description="Devito benchmark matrix",
      url='http://www.devitoproject.org',
      author="Devito Codes",
      author_email='g.gorman@imperial.ac.uk',
      license='MIT',
      packages=find_packages(),
      install_requires=required)
