from importlib import import_module
import inspect
from pathlib import Path
from pkgutil import iter_modules

import thematrix


def find_all_roofline_methods():
    """
    Testing implementation: discover all rooflining functions

    """

    _import_thematrix_submodules()
    for name, data in inspect.getmembers(thematrix):
        print(name)


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
    find_all_roofline_methods()
