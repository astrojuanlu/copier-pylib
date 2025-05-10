# copier-pylib

[Copier](https://github.com/copier-org/copier) template for pure Python libraries.

_As simple as possible. No magic._

## Features

- [uv] for project management and build backend.
- [pytest] for testing.
- [tox] for automation of test runners and other stuff.
- [Sphinx] for documentation
- [GitHub Actions] for continuous integration and publishing to PyPI.
- [Read the Docs] for continuous documentation.
- [mypy] for type checks.
- [ruff] for style checks and automatic Python code formatting.
- [pre-commit] for optional automation of style checks.

## Usage

Install `copier`:

```
uv tool install copier
```

Generate a Python package:

```
copier copy gh:astrojuanlu/copier-pylib path/to/destination
```

## License

[MIT License](LICENSE)

[uv]: https://github.com/astral-sh/uv
[copier]: https://github.com/copier-org/copier/
[mypy]: http://mypy.readthedocs.io/
[pytest]: https://docs.pytest.org/
[Sphinx]: http://www.sphinx-doc.org/
[tox]: https://tox.readthedocs.io/
[ruff]: https://docs.astral.sh/ruff/
[pre-commit]: https://github.com/pre-commit/pre-commit/
[GitHub Actions]: https://github.com/features/actions/
[Read the Docs]: https://readthedocs.org/
