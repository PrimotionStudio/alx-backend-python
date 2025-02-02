#!/usr/bin/env python3
"""python variable annotations"""
import typing


def element_length(lst: typing.Iterable[typing.Sequence]
                   ) -> typing.List[typing.Tuple[typing.Sequence, int]]:
    """python variable annotations"""
    return [(i, len(i)) for i in lst]
