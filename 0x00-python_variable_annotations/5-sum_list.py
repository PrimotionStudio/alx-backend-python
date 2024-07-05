#!/usr/bin/env python3
"""Returns the sum of all elements
    in the input list."""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Returns the sum of all elements
    in the input list."""
    return sum(n for n in input_list)