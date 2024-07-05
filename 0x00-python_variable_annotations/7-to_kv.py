#!/usr/bin/env python3
"""python variable annotations"""
import typing


def to_kv(k: str, v: typing.Union[int, float]) -> typing.Tuple[str, float]:
    """python variable annotations"""
    return (k, v ** 2)
