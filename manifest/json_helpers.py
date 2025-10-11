from collections import deque
from collections.abc import Iterator
from typing import Any, TypeGuard, overload

type JSONObject = dict[str, 'JSONAny']
type JSONArray = list['JSONAny']
type JSONScalar = None | bool | int | float | str
type JSONContainer = JSONArray | JSONObject
type JSONAny = JSONScalar | JSONArray | JSONObject
type JSONPath = tuple[int | str, ...]


def is_json_path(obj: Any, /) -> TypeGuard[JSONPath]:
    """
    Whether the given object is a JSON path.
    """
    return isinstance(obj, tuple) and all(isinstance(part, (str, int)) for part in obj)


def str_to_json_path(path: str, /) -> JSONPath:
    """
    Converts a string to a JSON path.

    >>> from manifest.json_helpers import str_to_json_path
    >>> str_to_json_path('a.b.v.1')
    ('a', 'b', 'v', '1')
    """
    return tuple(path.split('.'))


def json_path_to_str(path: JSONPath, /) -> str:
    """
    Converts a JSON path to a string.

    >>> from manifest.json_helpers import json_path_to_str
    >>> json_path_to_str(('a', 'b', 'v', 1))
    'a.b.v.1'
    """
    return '.'.join(map(str, path))


def json_search_old(
        obj: JSONAny,
        search_value: JSONAny,
        /,
        *path_parts: str | int
        ) -> Iterator[JSONPath]:
    """
    Recursively searches for the given search value inside the given JSON container.
    Returns an iterator over all JSON paths where the given search value is present.
    """
    if obj == search_value:
        yield path_parts
        return

    if isinstance(obj, dict):
        for key, value in obj.items():
            yield from json_search_old(value, search_value, *path_parts, key)

    elif isinstance(obj, list):
        for i, value in enumerate(obj):
            yield from json_search_old(value, search_value, *path_parts, i)


def json_search(obj: JSONContainer, search_value: JSONAny, /) -> Iterator[JSONPath]:
    """
    Recursively searches for the given search value inside the given JSON container.
    Returns an iterator over all JSON paths where the given search value is present.
    """
    stack: deque[tuple[JSONPath, JSONAny]] = deque()
    stack.append(((), obj))
    while stack:
        path_parts, obj = stack.popleft()  # type: ignore[assignment]
        if obj == search_value:
            yield path_parts
            continue

        if isinstance(obj, dict):
            stack.extend(
                ((*path_parts, key), value)
                for key, value in obj.items()
                )

        elif isinstance(obj, list):
            stack.extend(
                ((*path_parts, i), value)
                for i, value in enumerate(obj)
                )


def json_lookup(obj: JSONContainer, path: JSONPath, /) -> JSONAny:
    """
    Returns a value situated at the given path in the given JSON container.

    Raises :class:`TypeError` if scalar is met at some point in the path.
    Can also raise :class:`KeyError` and :class:`IndexError`
    if the path contains wrong dict keys and list indexes respectively.
    """
    current: JSONAny = obj
    for i, part in enumerate(path, 1):
        if isinstance(part, str) and '.' in part:
            raise ValueError(
                'a valid JSONPath cannot contain string parts with dots, '
                f'part {part!r} at index {i} is invalid'
                )

        if isinstance(current, dict):
            current = current[str(part)]
        elif isinstance(current, list):
            current = current[int(part)]
        else:
            raise TypeError(f'value at {json_path_to_str(path[:i])!r} is not subscriptable')

    return current


type JSONWrappedAny = JSONScalar | 'BaseJSONWrapper'


class BaseJSONWrapper:
    """
    A convenience wrapper around JSON objects and arrays.

    Supports functions ``len``, ``iter`` and ``reversed``,
    operator ``in`` and subscript notation to get nested values.

    Subscript notation supports JSON paths, strings and integers.
    For example, ``wrapper['a.1.c']``, ``wrapper['a', 1, 'c']`` and ``wrapper['a', '1', 'c']``
    represent the same nested value.

    Whether a nested value is returned via methods, subscripting or iterating,
    it is always wrapped into this class unless it is a scalar value.
    """
    __slots__ = '_container', '_lookup_cache'

    def __init__(self, container: JSONContainer, /) -> None:
        if self.__class__ is BaseJSONWrapper:
            raise TypeError(f"can't instantiate abstract class {BaseJSONWrapper.__name__}")

        self._container = container
        self._lookup_cache: dict[JSONPath, JSONWrappedAny] = {}

    def search(self, value: JSONAny, /) -> Iterator[JSONPath]:
        """
        Searches for a value inside the wrapped container
        and returns an iterator over all JSON path where the given value is found.
        """
        return json_search(self._container, value)

    def __contains__(self, item, /) -> bool:
        return item in self._container

    def __iter__(self, /) -> Iterator:
        raise NotImplementedError

    def __reversed__(self, /) -> Iterator:
        raise NotImplementedError

    def __len__(self, /) -> int:
        return len(self._container)

    def __getitem__(self, item: int | str | JSONPath, /) -> JSONWrappedAny:
        path: JSONPath
        if isinstance(item, int):
            path = (item,)
        elif isinstance(item, str):
            path = str_to_json_path(item)
        elif is_json_path(item):
            path = item
        else:
            raise TypeError(
                f'subscript notation supports integers, strings and JSON paths, '
                f'got {type(item)}'
                )

        if path:
            result = self._lookup_cache.get(path, ...)
            if result is ...:
                result = wrap_json_value(json_lookup(self._container, path))
                self._lookup_cache[path] = result

            return result

        return self

    def clear_lookup_cache(self, /) -> None:
        """
        Clears lookup cache of this wrapper.
        """
        self._lookup_cache.clear()

    def keys(self, /) -> Iterator:
        """
        Returns an iterator over keys of the wrapped container.
        If the container is an array, returns an iterator over its indices.
        If the container is an object, returns an iterator over its attributes.
        """
        raise NotImplementedError

    def values(self, /) -> Iterator[JSONWrappedAny]:
        """
        Returns an iterator over values of the wrapped container.
        """
        raise NotImplementedError

    def items(self, /) -> Iterator:
        """
        Returns an iterator over items of the wrapped container.
        If the container is an array, returns an iterator over tuples ``(index, value)``.
        If the container is an object, returns an iterator over tuples ``(attribute, value)``.
        """
        raise NotImplementedError


class JSONArrayWrapper(BaseJSONWrapper):
    """
    A convenience wrapper around JSON arrays.

    Check documentation of the base class
    to learn about supported builtin functions and operators.
    """
    __slots__ = ()

    def __init__(self, container: JSONArray, /) -> None:
        if not isinstance(container, list):
            raise TypeError(f'container must be a list, got {type(container)}')

        super().__init__(container)
        self._container: JSONArray

    def __contains__(self, item: JSONAny, /) -> bool: ...  # type: ignore[empty-body]
    del __contains__

    def __iter__(self, /) -> Iterator[JSONWrappedAny]:
        return map(self.__getitem__, range(len(self._container)))

    def __reversed__(self, /) -> Iterator[JSONWrappedAny]:
        return map(self.__getitem__, range(len(self._container) - 1, -1, -1))

    def keys(self, /) -> Iterator[int]:
        """
        Returns an iterator over indices of the wrapped array.
        """
        return iter(range(len(self._container)))

    def values(self, /) -> Iterator[JSONWrappedAny]:
        """
        Returns an iterator over values of the wrapped array.
        """
        return self.__iter__()

    def items(self, /) -> Iterator[tuple[int, JSONWrappedAny]]:
        """
        Returns an iterator over items of the wrapped array.
        An item is a tuple of an index and respective value.
        """
        return enumerate(self.__iter__())


class JSONObjectWrapper(BaseJSONWrapper):
    """
    A convenience wrapper around JSON objects.

    Check documentation of the base class
    to learn about supported builtin functions and operators.
    """
    __slots__ = ()

    def __init__(self, container: JSONObject, /) -> None:
        if not isinstance(container, dict):
            raise TypeError(f'container must be a dict, got {type(container)}')

        super().__init__(container)
        self._container: JSONObject

    def __contains__(self, item: str, /) -> bool: ...  # type: ignore[empty-body]
    del __contains__

    def __iter__(self, /) -> Iterator[str]:
        return iter(self._container)

    def __reversed__(self, /) -> Iterator[str]:
        return reversed(self._container)

    def keys(self, /) -> Iterator[str]:
        """
        Returns an iterator over attributes of the wrapped object.
        """
        return iter(self._container)

    def values(self, /) -> Iterator[JSONWrappedAny]:
        """
        Returns an iterator over values of the wrapped object.
        """
        return map(self.__getitem__, self._container)

    def items(self, /) -> Iterator[tuple[str, JSONWrappedAny]]:
        """
        Returns an iterator over items of the wrapped object.
        An item is a tuple of an attribute and respective value.
        """
        return zip(self._container, self.values(), strict=True)


@overload
def wrap_json_value(value: JSONArray, /) -> JSONArrayWrapper: ...


@overload
def wrap_json_value(value: JSONObject, /) -> JSONObjectWrapper: ...


@overload
def wrap_json_value[T: JSONWrappedAny](value: T, /) -> T: ...


def wrap_json_value(value, /) -> Any:
    """
    If the given value is a JSON container, wraps it in the respective wrapper.
    Otherwise, returns the value unchanged.
    """
    if isinstance(value, list):
        return JSONArrayWrapper(value)

    if isinstance(value, dict):
        return JSONObjectWrapper(value)

    return value


__all__ = (
    'JSONObject',
    'JSONArray',
    'JSONScalar',
    'JSONContainer',
    'JSONAny',
    'JSONPath',
    'JSONWrappedAny',
    'is_json_path',
    'str_to_json_path',
    'json_path_to_str',
    'json_search',
    'json_lookup',
    'BaseJSONWrapper',
    'JSONArrayWrapper',
    'JSONObjectWrapper',
    )
