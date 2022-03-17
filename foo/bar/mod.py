from __future__ import annotations

from typing import (
    Any,
    TYPE_CHECKING,
    TypeVar,
)

if TYPE_CHECKING:
    from typing_extensions import ParamSpec

    from ..fred import CoroMaybeMethod

__all__ = (
    'D', 'E', 'F'
)

if TYPE_CHECKING:
    P = ParamSpec('P')
else:
    P = TypeVar('P')

T = TypeVar('T')


class D:
    ...

class E(Exception):
    ...

class F:
    ...

DT = TypeVar('DT', bound=D)

if TYPE_CHECKING:
    Error = CoroMaybeMethod[DT, [F, E], Any]



