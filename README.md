# pypi-cookiecutter

[`cookiecutter`](https://github.com/cookiecutter/cookiecutter) template for Python packages using [`poetry`](https://python-poetry.org/) for build and dependency management, [`pytest`](https://github.com/pytest-dev/pytest) for unit testing and [`sphinx`](https://www.sphinx-doc.org) for documentation.

Based on [Python Packages](https://py-pkgs.org/). Developed for my use so may need tweaking.

## Project structure

Creates a Python project with the following structure where `[package-name]` is the name of the package when uploaded to PyPi.

```
[package-name]
├── .github                         ┐
│   └── workflows                   │ CI workflow
│       └── build.yml               ┘
├── .flake8                         ┐
├── .gitignore                      | Tool configuration
├── .pre-commit-config.yaml         ┘
├── docs                            ┐
│   ├── make.bat                    │
│   ├── Makefile                    |
│   └── source                      |
│       ├── api                     |
│       │   ├── [package-name].md   |
│       │   ├── index.md            |
│       │   └── utils.md            |
│       ├── tutorials               | Documentation
│       │   └── getting_started.md  |
│       ├── conf.py                 |
│       ├── index.md                |
│       └── README.md               |
├── CHANGELOG.md                    │
├── CITATION.cff                    |
├── LICENSE                         |
├── README.md                       ┘
├── pyproject.toml                  ┐ 
├── src                             │
│   └── [package-name]              │ Package code and
│       ├── __init__.py             │ build configuration
│       ├── [package-name].py       │
│       └── utils.py                ┘
└── tests                           ┐
    ├── test_[package-name].py      | Unit tests
    └── test_utils.py               ┘
        
```

All objects in `[package-name].py` are made available as `[package-name].object-name` (see `__init__.py`). `utils.py` is an example utility function module.

## Pre-commits

[`black`](https://github.com/psf/black), [`isort`](https://github.com/PyCQA/isort) and [`flake8`](https://github.com/PyCQA/flake8) are run as pre-commit hooks. Run `pre-commit install` to set these up.

## Continuous integration

Uses Github Actions for continuous integration. The workflow:

1. Checks code formatting with `black`, `isort` and `flake8`.
2. Runs `pytest` and generates a code coverage `.xml` file using [`pytest-cov`](https://github.com/pytest-dev/pytest-cov).
3. Builds the package documentation using `sphinx`.
4. Generates a code coverage badge using [`genbadge`](https://github.com/smarie/python-genbadge/).
5. Pushes the documentation to GitHub pages using the [peaceiris/actions-gh-pages@v3](https://github.com/peaceiris/actions-gh-pages) action.
6. Creates a release if a tag is pushed using the [git-release](https://github.com/marketplace/actions/git-release) action.

## Resources

The following are good resources for Python package development:

* [Python Packages](https://py-pkgs.org/)
* [Hypermodern Python](https://cjolowicz.github.io/posts/hypermodern-python-01-setup/)

## License

Released under the MIT license.
