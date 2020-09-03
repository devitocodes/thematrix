from importlib import import_module
import inspect
from pathlib import Path
from pkgutil import iter_modules

import thematrix


def generate_rooflines():
    """
    Uses the roofline generator methods in the discovered classes to
    generate all rooflines for all problems

    """

    roof_methods = _find_roofline_methods()
    for method in roof_methods:
        method()


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
                if m_name.startswith('roofline'):
                    roof_methods.append(m_data)

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
                pass


if __name__ == '__main__':
    generate_rooflines()
