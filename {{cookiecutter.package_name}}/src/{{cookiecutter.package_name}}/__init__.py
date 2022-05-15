"""Add an introduction to the ``{{ cookiecutter.package_name }}`` module here.
"""


from importlib.metadata import version

__version__ = version("{{ cookiecutter.package_name }}")

from {{ cookiecutter.package_name }}.{{ cookiecutter.package_name }} import *  # noqa: F401, F403

__all__ = []
for module in dir():
    if not module.startswith("__") and module != "{{ cookiecutter.package_name }}":
        __all__.append(module)
