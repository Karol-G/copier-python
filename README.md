# copier-python

Copier template for a modern Python package with CI, tag-based versioning, and PyPI publishing.

## Quick start

1) Install Copier (one-time):
```bash
pipx install copier  # or: pip install copier
```

2) Generate a project from this template:
```bash
copier copy https://github.com/Karol-G/copier-python your-project --trust
```

3) Answer the prompts. Copier will:
- Scaffold a repo-root package folder
- Set up GitHub Actions for tests and PyPI publish on `v*` tags
- Use `setuptools_scm` for versions from Git tags
- Initialize git and make the initial commit

4) Configure a trusted publisher for the project repository on PyPi

5) Add remote, tag and push to publish:
```bash
git remote add origin git@github.com:ACCOUNT/PROJECT.git
git push -u origin main
git tag v0.0.1
git push origin v0.0.1
```



## Template notes

- Adjust the defaults in `copier.yml` as needed.
- The project README is rendered from `README.project.md` into `README.md` during generation; the template README stays in this repo only.
- PyPI publishing expects a trusted publisher configuration. No twine or pypi api key secrets need to be added to this repository.

## Links

- Template repo: https://github.com/Karol-G/copier-python
- Copier docs: https://copier.readthedocs.io/
