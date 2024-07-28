#!/usr/bin/env python3
"""
Generic utilities for github org client.
"""
import unittest
from parameterized import parameterized
from typing import (
    Mapping,
    Sequence,
    Any,
    Union,
)


access_nested_map = __import__('utils').access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """
    Test the access_nested_map function.
    """

    @parameterized.expand([
        (
            {"a": 1},
            ("a",),
            1,
        ),
        (
            {"a": {"b": 2}},
            ("a",),
            {"b": 2}
        ),
        (
            {"a": {"b": 2}},
            ("a", "b"),
            2,
        ),
    ])
    def test_access_nested_map(self,
                               nested_map: Mapping, path: Sequence,
                               expected: Union[Mapping, int]) -> None:
        """
        Test the access_nested_map function.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)
