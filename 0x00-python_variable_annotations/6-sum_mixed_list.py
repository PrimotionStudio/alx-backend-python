#!/usr/bin/env python3
import typing
"""Returns the sum of all elements
    in the input list."""


def sum_mixed_list(mxd_lst: list[typing.Union[int, float]]) -> float:
    """Returns the sum of all elements
    in the input list."""
    return sum(n for n in mxd_lst)