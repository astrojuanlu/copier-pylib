# copier-pylib

[Copier](https://github.com/copier-org/copier) template for pure Python libraries.

_As simple as possible. No magic._

## Features

- [flit] for simple packaging.
- [pytest] for testing.
- [tox] for automation of test runners and other stuff.
- [Sphinx] for documentation
- [GitHub Actions] for continuous integration and publishing to PyPI.
- [Read the Docs] for continuous documentation.
- [mypy] for type checks.
- [black] for automatic Python code formatting.
- [flake8], [isort] and [pydocstyle] for style checks.
- [pre-commit] for optional automation of style checks.

## Usage

Install `copier`:

```
pipx install copier
```

Generate a Python package:

```
copier gh:astrojuanlu/copier-pylib path/to/destination
```

## License

[MIT License](LICENSE)

[copier]: https://github.com/copier-org/copier/
[mypy]: http://mypy.readthedocs.io/
[flit]: https://flit.readthedocs.io/
[pytest]: https://docs.pytest.org/
[Sphinx]: http://www.sphinx-doc.org/
[tox]: https://tox.readthedocs.io/
[black]: https://black.readthedocs.io/
[flake8]: https://flake8.pycqa.org/
[isort]: https://pycqa.github.io/isort/
[pydocstyle]: http://www.pydocstyle.org/
[pre-commit]: https://github.com/pre-commit/pre-commit
[GitHub Actions]: https://github.com/features/actions
[Read the Docs]: https://readthedocs.org
