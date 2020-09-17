from importlib import import_module
import inspect
from pathlib import Path
from pkgutil import iter_modules
from tempfile import gettempdir
from traceback import format_exc
import os

import thematrix


def generate_rooflines():
    """
    Uses the roofline generator methods in the discovered classes to
    generate all rooflines for all problems

    """
    # Set up the options
    opts = {'advisor': True}
    generated_dirs = []

    roof_methods = _find_roofline_methods()
    for (method, cls) in roof_methods:
        # Run the method and retrieve the results directory
        generated_dir = method(cls, opts)
        if generated_dir:
            generated_dirs.append(generated_dir)

    # Package the retrieved result directories into a file
    _write_generated_dirs(generated_dirs)


def _find_roofline_methods():
    """
    Discovers all methods to generate rooflines in package thematrix,
    returns a list of all methods that can be called.

    """

    roof_methods = []
    # Import all submodules
    _import_thematrix_submodules()
    for name, data in inspect.getmembers(thematrix):
        # Collect the roofline methods from the classes
        for c_name, c_data in inspect.getmembers(data, predicate=inspect.isclass):
            for m_name, m_data in inspect.getmembers(c_data, predicate=inspect.isfunction):
                if m_name == 'roofline_create':
                    roof_methods.append((m_data, c_data))

    return roof_methods


def _import_thematrix_submodules():
    """
    Import all the modules defined in package thematrix to
    be able to perform inspection.

    """

    for _, name, ispkg in iter_modules(thematrix.__path__):
        if not ispkg:
            module_name = thematrix.__name__ + '.' + name
            try:
                import_module(module_name)
            except ImportError:
                print('Error: could not import module ' + module_name)
                print(format_exc())


def _write_generated_dirs(generated_dirs):
    gen_file_dir = os.path.join(gettempdir(), 'generate_rooflines_tmp')
    if not os.path.isdir(gen_file_dir):
        os.mkdir(gen_file_dir)

    gen_file_path = os.path.join(gen_file_dir, 'generated.txt')
    with open(gen_file_path, 'w+') as f:
        f.writelines(generated_dirs)
    print('Rooflines successfully generated, directories listed in: ' + gen_file_path)


if __name__ == '__main__':
    generate_rooflines()
