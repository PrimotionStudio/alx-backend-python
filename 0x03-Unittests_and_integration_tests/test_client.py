#!/usr/bin/env python3
"""
"""
import unittest
from unittest.mock import patch
from parameterized import parameterized


GithubOrgClient = __import__('client').GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
    """
    @parameterized.expand([
        ('google',),
        ('abc',)
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """
        """
        client = GithubOrgClient(org_name)
        client.org()
        mock_get_json.return_value = {'key', 'value'}
        mock_get_json.assert_called_once_with(f"https://api.github.com/orgs/{org_name}")
