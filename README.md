# pypi-cookiecutter

A [`cookiecutter`](https://github.com/cookiecutter/cookiecutter) template for a [PyPI](https://pypi.org/)-ready Python package.

[`Poetry`](https://python-poetry.org/) is used for build and dependency management, [`pytest`](https://github.com/pytest-dev/pytest) for unit testing and [`sphinx`](https://www.sphinx-doc.org) for documentation. The template is based on [Python Packages](https://py-pkgs.org/) and was developed for my use so may need tweaking.

## Project structure

Creates a Python project with the following structure:

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
└── tests                           ┐ Unit
    └── test_[package-name].py      ┘ tests
```

Add your code to the `src/[package-name]/` directory. All objects in `[package-name].py` are imported as `[package-name].[object]` and `utils.py` is an example utility function module.

The project uses Python 3.8. This can be changed by entering a different version when initialising the project *and* by updating the `black` and `isort` sections of `pyproject.toml` plus the CI matrix and CD environment variable in `.github/workflows/build.yml`.

## Pre-commits

The following are run as pre-commit hooks:

* [`black`](https://github.com/psf/black) to lint code
* [`isort`](https://github.com/PyCQA/isort) to sort imports
* [`flake8`](https://github.com/PyCQA/flake8) to check PEP 8 compliance
* [`trailing-newline`](https://github.com/philipdarke/trailing-newline) to ensure files end with a blank newline*
* [`mixed-line-ending`](https://github.com/pre-commit/pre-commit-hooks) to use consistent CRLF or LF line endings
* [`name-tests-test`](https://github.com/pre-commit/pre-commit-hooks) to ensure the filenames of test scripts start "test"

Run `pre-commit install` to set these up.

\* Update `args` in `.pre-commit-config.yaml` to ignore specific file extensions. See the [documentation](https://github.com/philipdarke/trailing-newline).

## Continuous integration and deployment

Uses Github Actions for continuous integration and deployment. The workflow:

1. Checks code formatting with `black`, `isort` and `flake8`.
2. Runs `pytest` and generates a code coverage `.xml` file using [`pytest-cov`](https://github.com/pytest-dev/pytest-cov).
3. Builds the package documentation using `sphinx` and checks any code examples with `doctest`.
4. Generates a code coverage badge using [`genbadge`](https://github.com/smarie/python-genbadge/).

If a new version has been tagged:

5. Pushes the documentation to GitHub Pages using the [peaceiris/actions-gh-pages@v3.7.3](https://github.com/peaceiris/actions-gh-pages) action.
6. Creates a release if a tag is pushed using the [git-release](https://github.com/marketplace/actions/git-release) action. This generates a new DOI if the repository has been linked to your Zenodo account.
7. Publishes the package to PyPI using the [pypa/gh-action-pypi-publish@v1.5.0](https://github.com/pypa/gh-action-pypi-publish) action.

You may need to update the default permissions for GitHub Actions to "Read and write permissions" under Repository -> Settings -> Actions -> General -> Workflow permissions.

## Creating a release

1. Update `CHANGELOG.md`.
2. Update the version number in `pyproject.toml`. This can be automated by running `poetry version patch/minor/major` accordingly (see [Semantic Versioning](https://semver.org/)).
3. Update `CITATION.cff` if your reference style includes the version number (see [below](#generating-a-doi)).
4. Commit the changes and push to GitHub.
5. Tag the release with the same version using `git tag [version]`.
6. Push the tag using `git push --tags` to trigger the release.

## Publishing to PyPI

Create an account at [PyPI](https://pypi.org/), generate an API token and add this to the GitHub repository as `PYPI_API_TOKEN`. The GitHub Actions workflow will publish the package when a new release is tagged.

For the first release, manually publish a package using `Poetry`:

* To test the package, run `poetry build` and `poetry publish -r test-pypi` to publish the package to [TestPyPi](https://test.pypi.org/) (you will need to set up a separate account). You may need to first run `poetry config repositories.test-pypi https://test.pypi.org/legacy/` to add the TestPyPI repository.

* Check the package can be installed with `pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple [package-name]`. The `--extra-index-url` argument is needed to install dependencies from PyPI.

* Once the package has been tested, run `poetry publish` to publish to PyPI.

## Generating a DOI

Create an account at [Zenodo](https://zenodo.org/) and link your GitHub account. Enable the package repository in Account -> GitHub and a DOI will be generated following each release. Once a DOI is available, `README.md` and `CITATION.cff` should be updated accordingly.

This approach is not ideal as the DOI is assigned after creating a release. This can be managed in part by using the Concept DOI which always points to the most recent version of the package. See the Zenodo [FAQ](https://help.zenodo.org/#versioning) for more information.

If you use the Concept DOI in `CITATION.cff` I suggest you do not include the package version.

## Resources

The following are good resources for Python package development:

* [Python Packages](https://py-pkgs.org/)
* [Hypermodern Python](https://cjolowicz.github.io/posts/hypermodern-python-01-setup/)

## License

Released under the MIT license.

The template project also uses the MIT License. This can be changed by entering a different license when initialising a project *and* updating the LICENSE file accordingly.
