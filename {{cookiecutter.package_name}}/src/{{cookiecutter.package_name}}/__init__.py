from importlib.metadata import version

__version__ = version("{{ cookiecutter.package_name }}")

from {{ cookiecutter.package_name }}.{{ cookiecutter.package_name }} import AClass, a_function  # noqa: F401
