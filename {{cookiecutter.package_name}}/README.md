# {{ cookiecutter.package_short_description }}

[![PyPi](https://img.shields.io/pypi/v/{{ cookiecutter.package_name }})](https://pypi.org/project/{{ cookiecutter.package_name }})
[![Build status](https://img.shields.io/github/workflow/status/{{ cookiecutter.github_username }}/{{ cookiecutter.package_name }}/build.svg)](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.package_name }}/actions/workflows/build.yml)
![Coverage](https://{{ cookiecutter.website }}/{{ cookiecutter.package_name }}/assets/coverage-badge.svg?dummy=8484744)
[![License](https://img.shields.io/github/license/{{ cookiecutter.github_username }}/{{ cookiecutter.package_name }}.svg)](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.package_name }}/blob/main/LICENSE)
[![DOI](https://zenodo.org/badge/DOI/{{ cookiecutter.doi }}}.svg)](https://doi.org/{{ cookiecutter.doi }})

## Installation

```bash
$ pip install {{ cookiecutter.package_name }}
```

## Get started

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

## Citing this work

If you use this software, please cite it as below:

```
@software{ {{ cookiecutter.author_surname }}_{{ cookiecutter.package_name }}_{{ cookiecutter.year }},
    author = { {{ cookiecutter.author_surname }}, {{ cookiecutter.author_firstname }} },
    title = "{ {{ cookiecutter.package_name }}: {{ cookiecutter.package_short_description }} }",
    month = { {{ cookiecutter.month }} },
    year = { {{ cookiecutter.year }} },
    doi = { {{ cookiecutter.doi }} },
    url = { https://doi.org/{{ cookiecutter.doi }} },
}
```

The DOI above points to the latest version of the package. To reference a particular release, look up the DOI [here](https://doi.org/{{ cookiecutter.doi }}). You may also want to add `version = x.y.z` to the reference.

## License

Released under the {{ cookiecutter.license }} license.
