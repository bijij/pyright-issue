from typing import Any, TYPE_CHECKING, TypeVar, Union


T = TypeVar('T')

if TYPE_CHECKING:
    from typing_extensions import ParamSpec

    from ..fred import CoroMaybeMethod

    P = ParamSpec('P')
else:
    Concatenate = Union
    P = TypeVar('P')


class A:
    ...

class B:
    ...

class C:
    ...


BT = TypeVar('BT', bound=B)


if TYPE_CHECKING:
    Something = CoroMaybeMethod['A', ['BT', 'C'], Any]
    reveal_type(Something)
