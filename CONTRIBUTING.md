# Contributing

First off, thanks for taking the time to contribute! 🎉

The following is a set of guidelines for contributing to e-lims-core. These are mostly guidelines, not rules. Use your best judgment, and feel free to propose changes to this document in a pull request.

## Code of Conduct

This project and everyone participating in it is governed by the code of conduct. By participating, you are expected to uphold this code. Please report unacceptable behavior.

## Bug report

This section guides you through submitting a bug report. Following these guidelines helps maintainers and the community understand your report, reproduce the behavior, and find related reports.

- **Before submitting** a bug report, please check the [existing issues](https://github.com/FabienMeyer/e-lims-core/issues) to see if the issue has already been reported.
- If you find a **Closed** issue that seems like it is the same thing that you are experiencing, include a link to the original issue in your bug report.

[Follow the link](https://github.com/FabienMeyer/e-lims-core/issues/new?assignees=&labels=bug&projects=&template=bug_report.md&title=%5BBUG%5D+) and complete the template.

## Feature request

This section guides you through submitting an enhancement suggestion, including completely new features and minor improvements to existing functionality.

[Follow the link](https://github.com/FabienMeyer/e-lims-core/issues/new?assignees=&labels=bug&projects=&template=bug_report.md&title=%5BBUG%5D+) and complete the template.

## Development flow

### 1. Create a Branch
Create and switch to a new branch from the main.

``` bash
git checkout main
git pull
git checkout -b feat/name or fix/name or docs/name
```

### 2. Make your changes
Make the necessary changes to the codebase, ensuring your
   changes are well-documented and tested.

### 3. Run tests
``` bash
poetry run tox -e py311,py312
```

### 4. Run quality checks
ruff as formatter and linter, mypy as type checker

``` bash
poetry run tox -e quality
```

### 5. Build documentation
Build the mkdocs documentation and start the local server.

``` bash
poetry run tox -e documentation
mkdocs serve
```

### 6. Add and commit your changes
Add and commit your changes using Commitizen (Pre-commit will automatically run to check TOML, YAML, detect private keys).

``` bash
git add .
cz commit
```

### 7. Push your changes
Push your changes to your forked repository.

``` bash
git push origin feature-or-bugfix-name
```

### 8. Open a pull request
Navigate to the repository and click the "Pull requests" tab, then click "New merge request". Select your branch and the base branch (`main`) of the repository.

### 9. Describe your changes
Provide a clear description of the changes you have made, referencing any related issues or discussions.

### 10. Submit the pull request
Submit your pull request for review.

## Development Tools 

- Package template: [Cruft](https://cruft.github.io/cruft/)
- Packaging and dependency management: [Poetry](https://python-poetry.org/)
- Formatter: [Ruff formater](https://docs.astral.sh/ruff/formatter/)
- Linter: [Ruff Linter](https://docs.astral.sh/ruff/linter/)
- Type checker: [Mypy](https://mypy.readthedocs.io/en/stable/#)
- Tests framework: [Pytest](https://docs.pytest.org/en/stable/)
- Automate and standardize testing: [Tox](http://testrun.org/tox/)
- Documentation: [Mkdocs](https://www.mkdocs.org/)
- Pre-commit hooks: [Pre-commit](https://pre-commit.com/)
- Conventional commit: [Commitizen](https://github.com/commitizen-tools/commitizen)

## Style Guides

- Use [PEP 8](https://pep8.org/) for Python code style.
- Use [Google style docstrings](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings)
- Use [Conventional commit](https://www.conventionalcommits.org/en/v1.0.0/)
