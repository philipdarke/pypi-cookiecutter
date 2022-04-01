# pypi-cookiecutter

[`cookiecutter`](https://github.com/cookiecutter/cookiecutter) template for Python packages using [`poetry`](https://python-poetry.org/) for build and dependency management, [`pytest`](https://github.com/pytest-dev/pytest) for unit testing and [`sphinx`](https://www.sphinx-doc.org) for documentation.

Based on [Python Packages](https://py-pkgs.org/). Developed for my use so may need tweaking e.g. the links in README.md.

## Project structure

Creates a Python ``>=3.8,<3.10`` project under the MIT license with the following structure.

```
package-name
├── .github                    ┐
│   └── workflows              │ CI workflow
│       └── build.yml          ┘
├── .flake8                    ┐
├── .gitignore                 | Configuration
├── .pre-commit-config.yaml    ┘
├── docs                       ┐
│   ├── make.bat               │
│   ├── Makefile               |
│   ├── source                 |
│       ├── README.md          |
│       ├── conf.py            | Documentation
│       ├── index.md           |
│       ├── api.md             |
├── LICENSE                    │
├── README.md                  |
├── CITATION.cff               |
├── CHANGELOG.md               ┘
├── pyproject.toml             ┐ 
├── src                        │
│   └── package-name           │ Package code and build
│       ├── __init__.py        │
│       └── package-name.py    ┘
└── tests                      ┐
│   ├── __init__.py            | Unit tests
|   └── test_package-name.py   ┘
```

## Pre-commits

[`black`](https://github.com/psf/black), [`isort`](https://github.com/PyCQA/isort) and [`flake8`](https://github.com/PyCQA/flake8) are run as pre-commits. Run `pre-commit install` to set these up.

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
