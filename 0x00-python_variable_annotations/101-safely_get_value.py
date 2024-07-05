#!/usr/bin/env python3
"""python variable annotations"""
from typing import Any, TypeVar, Union, Mapping


type newType = TypeVar('T')
type ret = Union[Any, newType]
type arg = Union[newType, None]


def safely_get_value(dct: Mapping, key: Any, default: arg = None) -> ret:
    """python variable annotations"""
    if key in dct:
        return dct[key]
    else:
        return default