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
        with patch('client.GithubOrgClient.org') as mock_org:
            mock_org.PropertyMockreturn_value=payload
            org_client = GithubOrgClient("x")
            self.assertEqual(org_client._public_repos_url, expected)
