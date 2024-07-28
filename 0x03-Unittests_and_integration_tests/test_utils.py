#!/usr/bin/env python3
"""
Generic utilities for github org client.
"""
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from typing import (
    Mapping,
    Sequence,
    Any,
    Union,
)


access_nested_map = __import__('utils').access_nested_map
get_json = __import__('utils').get_json
memoize = __import__('utils').memoize


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
    @patch('utils.requests')
    def test_get_json(self, test_url, test_payload, mock_requests):
        """
        Test the get_json function.
        """
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_requests.get.return_value = mock_response

        self.assertEqual(get_json(test_url), test_payload)


class TestMemoize(unittest.TestCase):
    """
    Test the memoize function.
    """
    def test_memoize(self):
        """
        Test the memoize function.
        """
        class TestClass:
            """
            Test class.
            """
            def a_method(self):
                """
                Test method.
                """
                return 42

            @memoize
            def a_property(self):
                """
                Test property.
                """
                return self.a_method()

        test_instance = TestClass()
        with patch.object(TestClass, 'a_method',
                          return_value=42) as mock_a_method:
            first_call = test_instance.a_property
            second_call = test_instance.a_property
            self.assertEqual(first_call, 42)
            self.assertEqual(second_call, 42)
            mock_a_method.assert_called_once()
