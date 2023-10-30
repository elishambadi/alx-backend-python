#!usr/bin/env python3
"""Unittest Module"""
import unittest
from unittest.mock import patch
from parameterized import parameterized
from typing import Any, Dict, Tuple, Union

from utils import access_nested_map, get_json


class TestAccessNestedMap(unittest.TestCase):
    """
        Class for Testing Access to Nested Map
        Extends: unittest.TestCase
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self,
                               nested_map: Dict[str, Any],
                               path: Tuple[str, ...],
                               result: Union[int, Dict[str, Any]]) -> None:
        """
        Test for access_nested_map
        """
        self.assertEqual(access_nested_map(nested_map, path), result)


if __name__ == "__main__":
    unittest.main()
