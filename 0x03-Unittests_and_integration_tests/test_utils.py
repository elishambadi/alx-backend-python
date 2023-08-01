#!usr/bin/env python3

import unittest
from unittest.mock import patch
from parameterized import parameterized

from utils import access_nested_map, get_json


class TestAccessNestedMap(unittest.TestCase):

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        """
        Test for access_nested_map
        """
        self.assertEqual(access_nested_map(nested_map, path), expected_result)


class TestGetJson(unittest.TestCase):

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])

    @patch("requests.get")
    def test_get_json(self, test_url, test_payload, mock_get):
        # Set up the mock response
        mock_response = unittest.mock.Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response

        # Call the function under test
        result = get_json(test_url)

        # Assert the mocked get method was called exactly once with the test_url
        mock_get.assert_called_once_with(test_url)

        # Assert the output of get_json is equal to test_payload
        self.assertEqual(result, test_payload)


if __name__ == "__main__":
    unittest.main()
