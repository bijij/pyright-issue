from __future__ import annotations

from typing import Any, Callable, Coroutine, TypeVar, Union

from typing_extensions import ParamSpec, Concatenate

T = TypeVar('T')
U = TypeVar('U')
P = ParamSpec('P')


Method = Callable[Concatenate[T, P], U]

MaybeMethod = Union[
    Method[T, P, U],
    Callable[P, U],
]

Coro = Coroutine[Any, Any, T]
MaybeCoro = Union[T, Coro[T]]

CoroFunc = Callable[P, Coro[T]]

CoroMethod = Method[T, P, Coro[U]]

CoroMaybeMethod = Union[
    CoroMethod[T, P, U],
    CoroFunc[P, U],
]