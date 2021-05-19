![Tests](https://github.com/Informasjonsforvaltning/skolemizer/workflows/Tests/badge.svg)
[![codecov](https://codecov.io/gh/Informasjonsforvaltning/skolemizer/branch/main/graph/badge.svg)](https://codecov.io/gh/Informasjonsforvaltning/skolemizer)
[![PyPI](https://img.shields.io/pypi/v/skolemizer.svg)](https://pypi.org/project/skolemizer/)
[![Read the Docs](https://readthedocs.org/projects/skolemizer/badge/)](https://skolemizer.readthedocs.io/)
# skolemizer
A library with utils for performing Skolemization on blank nodes (RDF)

## Development
### Requirements
- [pyenv](https://github.com/pyenv/pyenv) (recommended)
- [pipx](https://github.com/pipxproject/pipx) (recommended)
- [poetry](https://python-poetry.org/)
- [nox](https://nox.thea.codes/en/stable/)
- [nox-poetry](https://github.com/cjolowicz/nox-poetry)

```
% pipx install poetry==1.1.6
% pipx install nox==2020.12.31
% pipx inject nox nox-poetry
```
### Install
```
% git clone https://github.com/Informasjonsforvaltning/skolemizer.git
% cd skolemizer
% pyenv install 3.9.4
% pyenv local 3.9.4
% poetry install
```
### Run all sessions
```
% nox
```
### Run all tests with coverage reporting
```
% nox -rs tests
```
### Debugging
You can enter into [Pdb](https://docs.python.org/3/library/pdb.html) by passing `--pdb` to pytest:
```
nox -rs tests -- --pdb
```
You can set breakpoints directly in code by using the function `breakpoint()`.
