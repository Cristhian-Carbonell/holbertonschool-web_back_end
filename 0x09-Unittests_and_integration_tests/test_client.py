#!/usr/bin/env python3
"""test client modules
"""
from client import GithubOrgClient
import client
from parameterized import parameterized
from unittest.mock import PropertyMock, patch, Mock
import unittest


class TestGithubOrgClient(unittest.TestCase):
    """Github org client class
    """
    @parameterized.expand([
        ("google", {"google": True}),
        ("abc", {"abc": True}),
    ])
    @patch('client.get_json')
    def test_org(self, org, expected, mock_request):
        """test org method
        """
        mock_request.return_value = expected
        org_client = GithubOrgClient(org)
        self.assertEqual(org_client.org, expected)
        mock_request.assert_called_once()

    def test_public_repos_url(self):
        """test public repos url method
        """
        expected = "www.yes.com"
        payload = {"repos_url": expected}
        with patch('client.GithubOrgClient.org',
                   PropertyMock(return_value=payload)):
            org_client = GithubOrgClient("x")
            self.assertEqual(org_client._public_repos_url, expected)

    @patch('client.get_json')
    def test_public_repos(self, get_json_mock):
        """ test the public repos """
        jeff = {"name": "Jeff", "license": {"key": "a"}}
        bobb = {"name": "Bobb", "license": {"key": "b"}}
        suee = {"name": "Suee"}
        to_mock = 'client.GithubOrgClient._public_repos_url'
        get_json_mock.return_value = [jeff, bobb, suee]
        with patch(to_mock, PropertyMock(return_value="www.yes.com")) as y:
            x = GithubOrgClient("x")
            self.assertEqual(x.public_repos(), ['Jeff', 'Bobb', 'Suee'])
            self.assertEqual(x.public_repos("a"), ['Jeff'])
            self.assertEqual(x.public_repos("c"), [])
            self.assertEqual(x.public_repos(45), [])
            get_json_mock.assert_called_once_with("www.yes.com")
            y.assert_called_once_with()
