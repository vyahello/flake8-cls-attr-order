import _ast
import ast
from dataclasses import dataclass
from typing import Any, Generator, List, Optional, Tuple, Type

from flake8_cls_attr_order.meta import Meta

_TIssues = List['Issue']
_Tout = Generator[Tuple[int, int, str, Type[Any]], None, None]

# class namespace
CL100 = 'CL100 "{name}" class name should start with upper case letter'
CL101 = 'CL101 wrong "{name}" class constants order, should be "{sv}"'

# methods namespace
CL200 = (
    'CL200 "{name}" @staticmethod is detected, '
    'should be converted to function'
)


@dataclass
class Issue:
    lineno: int
    col_offset: int
    message: str


class ClassVisitor(ast.NodeVisitor):
    def __init__(self) -> None:
        self._issues: _TIssues = []

    @property
    def issues(self) -> _TIssues:
        return self._issues

    def visit_ClassDef(self, node: ast.ClassDef) -> None:
        if isinstance(node, ast.ClassDef):
            self._check_cls_name(node)
            self._check_cls_attrib_order(node)
            self._check_static_method(node)

    def _check_static_method(self, node: ast.ClassDef) -> None:
        for attrib in node.body:  # type: _ast.stmt
            if isinstance(attrib, ast.FunctionDef):
                decorator_list = attrib.decorator_list
                if decorator_list:
                    for dec_obj in decorator_list:
                        if dec_obj.id == 'staticmethod':
                            self._issues.append(
                                Issue(
                                    attrib.lineno,
                                    attrib.col_offset,
                                    message=CL200.format(name=attrib.name),
                                )
                            )

    def _check_cls_name(self, node: ast.ClassDef) -> None:
        if not node.name.istitle():
            self._issues.append(
                Issue(
                    node.lineno,
                    node.col_offset,
                    message=CL100.format(name=node.name),
                )
            )

    def _check_cls_attrib_order(self, node: ast.ClassDef) -> None:
        def consts(indata: List[Tuple[str, int]], separator: str = ',') -> str:
            return f'{separator} '.join(sv[0] for sv in indata)

        actual_const_line: List[Tuple[str, int]] = []
        for attrib in node.body:  # type: _ast.stmt
            if isinstance(attrib, (ast.Assign, ast.AnnAssign)):
                try:
                    ast_name: ast.Name = attrib.targets[0]
                except AttributeError:
                    ast_name: ast.Name = attrib.target
                actual_const_line.append((ast_name.id, ast_name.lineno))

        sorted_const_line = sorted(actual_const_line, key=lambda p: p[0])
        if actual_const_line != sorted_const_line:
            self._issues.append(
                Issue(
                    node.lineno,
                    node.col_offset,
                    message=CL101.format(
                        name=node.name, sv=consts(sorted_const_line)
                    ),
                )
            )


class ClassAttrOrder:
    name: str = Meta.name
    version: str = Meta.version

    def __init__(
        self, tree: ast.Module, filename: Optional[str] = None
    ) -> None:
        self._tree = tree
        self._filename = filename

    def run(self) -> _Tout:
        cls_visitor = ClassVisitor()
        cls_visitor.visit(self._tree)
        for issue in cls_visitor.issues:  # type: Issue
            yield issue.lineno, issue.col_offset, issue.message, type(self)
