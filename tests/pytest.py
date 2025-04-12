import unittest
from Core.server.helpers import *

class TestBuildURL(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(build_url("http://example.com", "api"), "http://example.com/api")

    def test_trailing_slash_base(self):
        self.assertEqual(build_url("http://example.com/", "api"), "http://example.com/api")

    def test_leading_slash_path(self):
        self.assertEqual(build_url("http://example.com", "/api"), "http://example.com/api")

    def test_both_slashes(self):
        self.assertEqual(build_url("http://example.com/", "/api"), "http://example.com/api")

    def test_multiple_slashes(self):
        self.assertEqual(build_url("http://example.com///", "///api"), "http://example.com/api")

    def test_empty_path(self):
        self.assertEqual(build_url("http://example.com", ""), "http://example.com/")

    def test_nested_path(self):
        self.assertEqual(build_url("http://example.com", "api/v1/user"), "http://example.com/api/v1/user")

    def test_with_query_params(self):
        self.assertEqual(build_url("http://example.com", "api?name=test"), "http://example.com/api?name=test")

if __name__ == "__main__":
    unittest.main()
