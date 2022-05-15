"""Module docstring for ``cdtcloud`` module.
"""


from importlib.metadata import version

__version__ = version("{{ cookiecutter.package_name }}")

from {{ cookiecutter.package_name }}.{{ cookiecutter.package_name }} import *  # noqa: F401, F403

__all__ = []
for module in dir():
    if not module.startswith("__") and module != "cdtcloud":
        __all__.append(module)
