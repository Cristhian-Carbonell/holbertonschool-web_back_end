#!/usr/bin/env python3
"""Parameterize a unit test
"""
from parameterized import parameterized, parameterized_class
import unittest
import utils
from utils import get_json
from unittest.mock import patch, Mock


class TestAccessNestedMap(unittest.TestCase):
    """TestAccessNestedMap class
    """
    @parameterized.expand([
        ({"a": 1}, ["a"], 1),
        ({"a": {"b": 2}}, ["a"], {"b": 2}),
        ({"a": {"b": 2}}, ["a", "b"], 2),
    ])
    def test_access_nested_map(self, nested_map: dict, path: list, expected):
        """method to test that the method returns what it is supposed to.
        """
        self.assertEqual(utils.access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ["a"], KeyError),
        ({"a": 1}, ["a", "b"], KeyError)
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """exception KeyError"""
        with self.assertRaises(KeyError):
            utils.access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """test get json class
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url: str, expected):
        """test_get_json method
        """
        with patch('utils.requests.get') as mock_get:
            mock_get.return_value = expected
            response = Mock()
            try:
                response = get_json(test_url)
            except AttributeError:
                response.loads(expected)
            response.loads.assert_called_once()
        self.assertEqual(mock_get(), expected)
