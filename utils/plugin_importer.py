from inspect import isclass
from pkgutil import iter_modules
from pathlib import Path
from importlib import import_module


def import_plugins(name, file):
    """
    Imports all modules from the current directory (typically run from a __init__.py file).

    Should probably only be used for modules which aren't directly referenced in code as the modules won't be determined
    until runtime (and an IDE won't know what you are importing).

    Adapted from Julien Harbulot's blog: https://julienharbulot.com/python-dynamical-import.html.

    :param name: Set this to __name__
    :param file: Set this to __file__
    """

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
