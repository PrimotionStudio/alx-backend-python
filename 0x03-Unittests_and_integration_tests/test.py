#!/usr/bin/env python3
"""Generic utilities for github org client.
"""
import unittest
from parameterize import parameterize
from typing import (
    Mapping,
    Sequence,
    Any
)


def access_nested_map(nested_map: Mapping, path: Sequence) -> Any:
    for key in path:
        if not isinstance(nested_map, Mapping):
            raise KeyError(key)
        nested_map = nested_map[key]
    return nested_map

class TestAccessNestedMap(unittest.TestCase):
    """
    Test the access_nested_map function.
    """

    @parameterize.expand([
        (
            {"a": 1},
            ("a",),
            None
        )
        (
            {"a": {"b": 2}},
            ("a",),
            None
        ),
        (
            {"a": {"b": 2}},
            ("a", "b"),
            None
        )
    ])
    def test_access_nested_map(self, nested_map, key_list, expected):
        """
        Test the access_nested_map function.
        """
        self.assertEqual(access_nested_map(nested_map, key_list), expected)