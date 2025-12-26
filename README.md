{{ project_name }}
{{ "=" * project_name|length }}

![PyPI](https://img.shields.io/pypi/v/{{ project_slug }}?logo=pypi&color=brightgreen)
![Python Version](https://img.shields.io/pypi/pyversions/{{ project_slug }}?logo=python)
![Tests](https://img.shields.io/github/actions/workflow/status/{{ github_username }}/{{ project_slug }}/workflow.yml?branch={{ default_branch }}&logo=github)
[![Copier](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/copier-org/copier/master/img/badge/badge-grayscale-inverted-border-purple.json)](https://github.com/copier-org/copier)
![License](https://img.shields.io/github/license/{{ github_username }}/{{ project_slug }})

{{ project_description }}

## Features
- Package at repo root (`{{ package_name }}`) with dynamic versioning from Git tags via `setuptools_scm`
- GitHub Actions CI for lint/test and PyPI publishing on version tags
- PyPI-friendly metadata with README and license ready to ship
- Minimal default test to keep CI green, even with no custom tests
- Copier-powered customization (name, package folder, author, remotes, Python version)

## Getting started

1. Install Copier if needed: `pip install copier`.
2. Generate a new project:
   ```bash
   copier copy {{ repository_url }} new-project
   ```
3. Answer the prompts (project/package names, author, GitHub info, remote).
4. Enter the project directory, initialize git, and set your remote:
   ```bash
   cd new-project
   git init
   git remote add origin {{ git_remote }}
   ```

## Development

- Install dev dependencies and run tests:
  ```bash
  python -m pip install --upgrade pip
  pip install -e .[dev]
  pytest || if [ $? -eq 5 ]; then echo \"No tests collected\"; fi
  ```

- Versioning is tag-driven via `setuptools_scm`. Create tags like `v0.1.0`:
  ```bash
  git tag v0.1.0 && git push origin v0.1.0
  ```

## Continuous Integration

- CI runs on pushes and pull requests to `{{ default_branch }}`.
- Publishing to PyPI triggers when pushing tags that start with `v`. Set `PYPI_API_TOKEN` in repository secrets.

## Project layout

```
.
├─ {{ package_name }}/              # Your package code
├─ tests/                           # Pytest tests (default sample included)
├─ .github/workflows/workflow.yml   # CI + publish workflow
├─ pyproject.toml                   # PEP 621 metadata with setuptools_scm
└─ README.md                        # You are here
```

## License

Distributed under the {{ license }} license. See `LICENSE` for details.
