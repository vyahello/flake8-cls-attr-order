[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![Coverage Status](https://coveralls.io/repos/github/vyahello/flake8-cls-attr-order/badge.svg?branch=master)](https://coveralls.io/github/vyahello/flake8-cls-attr-order?branch=master)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Checked with flake8](https://img.shields.io/badge/flake8-checked-blue)](http://flake8.pycqa.org/)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE.md)
[![PyPI version shields.io](https://img.shields.io/pypi/v/flake8-cls-attr-order.svg)](https://pypi.org/project/flake8-cls-attr-order/)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/flake8-cls-attr-order.svg)](https://pypi.org/project/flake8-cls-attr-order/)
[![PyPi downloads](https://img.shields.io/pypi/dm/flake8-cls-attr-order.svg)](https://pypi.python.org/pypi/flake8-cls-attr-order)
[![Downloads](https://pepy.tech/badge/flake8-cls-attr-order)](https://pepy.tech/project/flake8-cls-attr-order)
[![EO principles respected here](https://www.elegantobjects.org/badge.svg)](https://www.elegantobjects.org)

# flake8-cls-attr-order

> A flake8 plugin that checks class attributes for the proper alphabetical order.

## Tools

### Production
- python 3.7+
- [flake8](http://flake8.pycqa.org/en/latest/)

### Development

- [black](https://black.readthedocs.io/en/stable/)
- [isort](https://pycqa.github.io/isort)
- [flake8](http://flake8.pycqa.org/en/latest/)
- [pytest](https://docs.pytest.org/en/7.0.x/)
- [bats](https://github.com/bats-core/bats-core)

## Usage

```python
# cls.py

class Foo:
    BAR = ()
    ABRA = {}
```

```bash
flake8 cls.py
cls.py:1:1: CL200 wrong "Foo" class constants order, should be "ABRA, BAR"
```

### Installation

```bash
pip install flake8-cls-attr-order
✨ 🍰 ✨
```

### Source code

```bash
git clone git@github.com:vyahello/flake8-cls-attr-order.git
cd flake8-cls-attr-order
python3 -m venv venv 
. venv/bin/activate
pip install -e .
```

**[⬆ back to top](#flake8-cls-attr-order)**

## Warnings

- `CL100` - class name should start with upper case letter.
- `CL200` - wrong class constants order.

## Development notes

### Testing 

#### Unit tests

Please run the following script to start plugin unit tests:
```bash
pytest 
```

#### Package tests

Please run the following script to start plugin package tests:
```bash
bats test-package.bats 
```

### CI

To be able to run code analysis, please execute command below:
```bash
./analyse-source-code.sh
```

### Meta

Author – _Vladimir Yahello_.

Distributed under the `MIT` license. See [license](LICENSE.md) for more information.

You can reach out me at:
* [vyahello@gmail.com](vyahello@gmail.com)
* [https://twitter.com/vyahello](https://twitter.com/vyahello)
* [https://www.linkedin.com/in/volodymyr-yahello-821746127](https://www.linkedin.com/in/volodymyr-yahello-821746127)

### Contributing

I would highly appreciate any contribution and support. If you are interested to add your ideas into project please follow next simple steps:

1. Clone the repository
2. Configure `git` for the first time after cloning with your `name` and `email`
3. `pip install -r requirements.txt` to install all project dependencies
4. `pip install -r requirements-dev.txt` to install all development project dependencies
5. Create your feature branch (git checkout -b feature/fooBar)
6. Commit your changes (git commit -am 'Add some fooBar')
7. Push to the branch (git push origin feature/fooBar)
8. Create a new Pull Request

### What's next

All recent activities and ideas are described at project [issues](https://github.com/vyahello/flake8-cls-attr-order/issues) page. 
If you have ideas you want to change/implement please do not hesitate and create an issue.

**[⬆ back to top](#flake8-cls-attr-order)**
