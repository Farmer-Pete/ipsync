# pylint: disable=C0111,R0903
import unittest
from unittest.mock import patch

from ipsync import main


class TestMain(unittest.TestCase):
    @patch('requests.get')
    def test_resolve_ip(self, request_mock):
        request_mock.return_value.status_code = 200
        request_mock.return_value.text = '127.0.0.1\n'

        self.assertEquals(main.resolve_ip(), '127.0.0.1')

    @patch('requests.get')
    def test_resolve_ip_returns_none_on_error(self, request_mock):
        request_mock.return_value.status_code = 500
        request_mock.return_value.text = 'An error occurred'

        self.assertEquals(main.resolve_ip(), None)

    @patch('requests.get')
    def test_resolve_ip_returns_none_on_invalid_data(self, request_mock):
        request_mock.return_value.status_code = 200
        request_mock.return_value.text = 'some random data\n'

        self.assertEquals(main.resolve_ip(), None)
