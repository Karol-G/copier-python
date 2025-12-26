{{ project_name }}
{{ "=" * project_name|length }}

![PyPI](https://img.shields.io/pypi/v/{{ project_slug }}?logo=pypi&color=brightgreen)
![Python Version](https://img.shields.io/pypi/pyversions/{{ project_slug }}?logo=python)
![Tests](https://img.shields.io/github/actions/workflow/status/{{ github_username }}/{{ project_slug }}/workflow.yml?branch={{ default_branch }}&logo=github)
![Copier Template](https://img.shields.io/badge/copier-template-blue?logo=jinja)
![License](https://img.shields.io/github/license/{{ github_username }}/{{ project_slug }})

{{ project_description }}

## Installation

You can install {{ project_slug }} via [pip](https://pypi.org/project/{{ project_slug }}/):
```bash
pip install {{ project_slug }}
```

## Usage

```python
from {{ package_name }} import __version__

print(__version__)
```

## Contributing

Contributions are welcome! Please open a pull request with clear changes and add tests when appropriate.

## Issues

Found a bug or have a request? Open an issue at {{ repository_url }}/issues.

## License

Distributed under the {{ license }} license. See `LICENSE` for details.
