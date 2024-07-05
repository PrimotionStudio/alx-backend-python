#!/usr/bin/env python3
"""python variable annotations"""
from typing import Any, TypeVar, Union, Mapping


NewType = TypeVar('T')
Return = Union[Any, NewType]
Default = Union[NewType, None]


def safely_get_value(dct: Mapping, key: Any, default: Default = None) -> Return:
    """python variable annotations"""
    if key in dct:
        return dct[key]
    else:
        return default
