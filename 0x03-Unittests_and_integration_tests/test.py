#!/usr/bin/env python3
"""Generic utilities for github org client.
"""
import requests
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from typing import (
    Mapping,
    Sequence,
    Any,
    Dict
)


def access_nested_map(nested_map: Mapping, path: Sequence) -> Any:
    for key in path:
        if not isinstance(nested_map, Mapping):
            raise KeyError(key)
        nested_map = nested_map[key]
    return nested_map

def get_json(url: str) -> Dict:
    """Get JSON from remote URL.
    """
    response = requests.get(url)
    return response.json()

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


class TestGetJson(unittest.TestCase):
    """
    Test the get_json function.
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('requests')
    def test_get_json(self, test_url, test_payload, mock_requests):
        """
        Test the get_json function.
        """
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_requests.get.return_value = mock_response

        self.assertEqual(get_json(test_url), test_payload)
