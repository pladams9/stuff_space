"""
Adapted from Julien Harbulot's blog: https://julienharbulot.com/python-dynamical-import.html.
"""

from inspect import isclass
from pkgutil import iter_modules
from pathlib import Path
from importlib import import_module


def import_all_modules(name, file):
    # iterate through the modules in the current package
    package_dir = Path(file).resolve().parent
    for (_, module_name, _) in iter_modules([str(package_dir)]):

        # import the module and iterate through its attributes
        module = import_module(f"{name}.{module_name}")
        for attribute_name in dir(module):
            attribute = getattr(module, attribute_name)

            if isclass(attribute):
                # Add the class to this package's variables
                globals()[attribute_name] = attribute
