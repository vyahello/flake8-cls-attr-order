import ast
from typing import Tuple

import pytest

from flake8_cls_attr_order.plugin import CL100, CL101, ClassAttrOrder

pytestmark = pytest.mark.unit

_FOO = 'Foo'


def _plugin_results(py_content: str) -> Tuple[str, ...]:
    plugin = ClassAttrOrder(ast.parse(py_content))
    return tuple(
        f'{line}:{column + 1} {message}'
        for line, column, message, _ in plugin.run()
    )


def _out(line: int, column: int, msg: str) -> str:
    return f'{line}:{column} {msg}'


def test_good_cls_name():
    assert not _plugin_results(f'class {_FOO}:\n    ...')


def test_bad_cls_name():
    assert _plugin_results(f'class {_FOO.lower()}:\n    ...') == (
        _out(line=1, column=1, msg=CL100.format(name=_FOO.lower())),
    )


def test_good_cls_attrib_order():
    assert not _plugin_results(f'class {_FOO}:\n    ABRA: int\n    BAR: int\n')


def test_bad_cls_attrib_order():
    assert _plugin_results(f'class {_FOO}:\n    BAR: int\n    ABRA: int\n') == (
        _out(
            line=1,
            column=1,
            msg=CL101.format(name=_FOO, sv='ABRA, BAR'),
        ),
    )
