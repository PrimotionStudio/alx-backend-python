#!/usr/bin/env python3
"""
lorem ipsum dolor latom
"""
import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized, parameterized_class


TEST_PAYLOAD = __import__("fixtures").TEST_PAYLOAD
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
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}")

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

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """
        lorem ipsum
        """
        mock_repos_payload = [
            {"name": "repo1"},
            {"name": "repo2"},
            {"name": "repo3"}
        ]
        mock_get_json.return_value = mock_repos_payload
        with patch(
                   'client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_public_repos_url:
            mock_public_repos_url.return_value = 'https://api.github.com'
            self.assertEqual(GithubOrgClient('github').public_repos(), [
                             "repo1", "repo2", "repo3"])
            mock_public_repos_url.assert_called_once()
            mock_get_json.assert_called_once()

    @parameterized.expand([
        (
            {"license": {"key": "my_license"}},
            "my_license",
            True
        ),
        (
            {"license": {"key": "other_license"}},
            "my_license",
            False
        ),
    ])
    def test_has_license(self, license, key, boolean):
        """
        lorem ipsum
        """
        self.assertEqual(GithubOrgClient.has_license(license, key), boolean)


class MockResponse:
    """
    lorem ipsum
    """
    def __init__(self, json_data):
        """
        lorem ipsum
        """
        self.json_data = json_data

    def json(self):

        """
        lorem ipsum
        """
        return self.json_data


@parameterized_class([
    {
        "org_payload": TEST_PAYLOAD[0][0]['repos_url'],
        "repos_payload": TEST_PAYLOAD[0][1],
        "expected_repos": TEST_PAYLOAD[0][2],
        "apache2_repos": TEST_PAYLOAD[0][3]
    }
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """
    lorem ipsum
    """
    @classmethod
    def setUpClass(cls):
        """
        lorem ipsum
        """
        cls.get_patcher = patch('request.get')
        cls.mock_get = cls.get_patcher.start()

        def get_side_effect(url):
            """
            lorem ipsum
            """
            if url == cls.org_payload:
                return MockResponse(cls.repos_payload)
            return MockResponse({})
        
        cls.mock_get.side_effect = get_side_effect

    @classmethod
    def tearDownClass(cls):
        """
        lorem ipsum
        """
        cls.get_patcher.stop()