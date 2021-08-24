#!/usr/bin/env python3
"""Parameterize a unit test
"""
from parameterized import parameterized, parameterized_class
import unittest
import utils


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
