# Publishing rp2040link to PyPI

This project is ready for PyPI publication. Two recommended paths are provided:

## Option A — Trusted Publishing (recommended)

Trusted Publishing uses GitHub Actions + OIDC (no long-lived API token stored).

1. Create the project on GitHub (repo name: `rp2040link`).
2. Create accounts on **PyPI** and (optional) **TestPyPI**.
3. On PyPI: go to your project (or create it on first upload) → **Settings** → **Trusted Publishers**
   and add your GitHub repository + workflow.
4. Push a tag like:

```bash
git tag v0.1.2
git push origin v0.1.2
```

The workflow `.github/workflows/publish.yml` will build and publish.

> Tip: Use GitHub environments to restrict which branches/tags can publish.

## Option B — Manual upload with Twine (API token)

1. Install tools:

```bash
python -m pip install --upgrade build twine
```

2. Build:

```bash
python -m build
python -m twine check dist/*
```

3. Upload to TestPyPI first (optional):

```bash
python -m twine upload -r testpypi dist/*
```

4. Upload to PyPI:

```bash
python -m twine upload dist/*
```

When the upload succeeds, users can install with:

```bash
pip install rp2040link
```

## Name availability

PyPI package names are unique. If `rp2040link` is already taken, rename the project in:
- `pyproject.toml` → `[project].name`
- `src/rp2040link/` folder and imports (or choose a different distribution name but keep module name)


## Exact Trusted Publisher settings for this repo

On PyPI → **Manage project** → **Publishing** → **Add trusted publisher** (GitHub Actions), set:

- **Owner**: `okhtaymp`
- **Repository**: `rp2040link`
- **Workflow name**: `publish.yml`
- **Environment**: `pypi`

This locks publishing to the specific workflow file and environment.
