from importlib.metadata import version as get_version

# Project information
project = "{{ cookiecutter.package_name }}"
copyright = "{% now 'local', '%Y' %}, {{ cookiecutter.author_firstname }} {{ cookiecutter.author_surname }}"
author = "{{ cookiecutter.author_firstname }} {{ cookiecutter.author_surname }}"
version = get_version("{{ cookiecutter.package_name }}")
release = version

# General
extensions = [
    "sphinx.ext.autodoc",  
    "sphinx.ext.doctest",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "myst_parser",
    "sphinx_autodoc_typehints",
    "sphinx_copybutton",
]

# sphinx.ext.autodoc settings
autodoc_member_order = "bysource"
exclude_patterns = ["_build"]

# sphinx_copybutton settings
copybutton_prompt_text = ">>> "
copybutton_line_continuation_character = "\\"
copybutton_image_svg = """
<svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-file" width="44" height="44" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <path stroke="none" d="M0 0h24v24H0z" fill="none"/>
  <path d="M14 3v4a1 1 0 0 0 1 1h4" />
  <path d="M17 21h-10a2 2 0 0 1 -2 -2v-14a2 2 0 0 1 2 -2h7l5 5v11a2 2 0 0 1 -2 2z" />
</svg>
"""

# HTML output
html_theme = "sphinx_rtd_theme"
html_theme_options = {
    "navigation_depth": 2,
}
html_context = {
    "display_github": True,
    "github_user": "{{ cookiecutter.github_username }}",
    "github_repo": "{{ cookiecutter.package_name }}",
    "github_version": "main",
    "conf_py_path": "/docs/source/",
    "source_suffix": ".md",
}
html_title = "{{ cookiecutter.package_name }}"
html_static_path = ["_static"]
html_extra_path = ["README.md"]
html_css_files = ["custom.css"]
pygments_style = "friendly"
html_show_sphinx = False
