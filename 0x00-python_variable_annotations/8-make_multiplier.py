#!/usr/bin/env python3
"""python variable annotations"""
import typing


def make_multiplier(multiplier: float) -> typing.Callable[[float], float]:
    """python variable annotations"""
    return lambda x: x * multiplier
    