#!/usr/bin/env python3
"""Generic utilities for github org client.
"""
import unittest
from parameterized import parameterized
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

    @parameterized.expand([
        (
            {"a": 1},
            ("a",),
            1
        ),
        (
            {"a": {"b": 2}},
            ("a",),
            {"b": 2}
        ),
        (
            {"a": {"b": 2}},
            ("a", "b"),
            2
        )
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """
        Test the access_nested_map function.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        (
            {},
            ("a",),
            KeyError,
        ),
        (
            {"a": 1},
            ("a", "b"),
            KeyError,
        ),
    ])
    def test_access_nested_map_exception(self, nested_map, path, exceptions):
        """
        Test the access_nested_map function with exceptions.
        """
        with self.assertRaises(exceptions):
            access_nested_map(nested_map, path)
