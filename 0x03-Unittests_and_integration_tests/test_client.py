#!/usr/bin/env python3
"""
lorem ipsum dolor latom
"""
import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized


GithubOrgClient = __import__('client').GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
    lorem ipsum dolor latom
    """
    @parameterized.expand([
        ('google',),
        ('abc',)
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """
        lorem ipsum dolor latom
        """
        client = GithubOrgClient(org_name)
        client.org()
        mock_get_json.return_value = {'key': 'value'}
        mock_get_json.assert_called_once_with(f"https://api.github.com/orgs/{org_name}")

    @parameterized.expand([
        (
            'github',
            {'repos_url': 'https://api.github.com'},
        ),
        (
            'gitlab',
            {'repos_url': 'https://api.gitlab.com'},
        ),
    ])
    @patch('client.GithubOrgClient.org', new_callable=PropertyMock)
    def test_public_repos_url(self, org_name, repo_url, mock_org):
        """
        lorem ipsum dolor latom
        """
        mock_org.return_value = repo_url
        client = GithubOrgClient(org_name)
        # print("=>", repo_url) 
        self.assertEqual(client._public_repos_url, repo_url['repos_url'])