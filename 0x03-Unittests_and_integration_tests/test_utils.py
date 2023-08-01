#!usr/bin/env python3
"""
TestCase for TestCase
"""
import unittest

from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    def test_access_nested_map(self):
        """
        Test of Accessing a NestedMap
        """

        # Test with a nested map
        nested_map = {"a": {"b": {"c": 1}}}
        self.assertEqual(access_nested_map(nested_map, ["a", "b", "c"]), 1)

        # Test with a deeper nested map
        nested_map = {"x": {"y": {"z": {"value": 42}}}}
        self.assertEqual(
            access_nested_map(nested_map, ["x", "y", "z", "value"]), 42
        )

    def test_invalid_key(self):
        """
        Test for invalid key
        """

        # Test with an invalid key
        nested_map = {"a": {"b": {"c": 1}}}
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, ["a", "x", "y"])

        # Test with an invalid path
        nested_map = {"a": {"b": {"c": 1}}}
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, ["a", "b", "c", "d"])


if __name__ == "__main__":
    unittest.main()
